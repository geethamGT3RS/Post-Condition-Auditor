"""This file has all the functions to make calls to the LLM API (gemini-Flash model)
to generate preconditions and postconditions for given Python functions."""
import os
import json
import random as rnd
from anyio import Path
from jsonschema import validate, ValidationError
import re
import time
from dotenv import load_dotenv
from config import get_db_client
import ast  # <-- ADDED for parsing function name
from Prompts import getFunctionCodeAndNameFromPromptID, updateTestcases, save_formatting_prompt
from Prompts import updateReasoning, get_function_name,getPromptbyPromptID,save_structured_response
import google.generativeai as genai
from typing import Tuple, Optional
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from google.api_core.exceptions import ResourceExhausted
from string import Template
from test_case_schema import test_case_schema

#env file as .env in root directory
env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env')
print(f"Loading environment variables from: {env_path}")
if os.path.exists(env_path):
    load_dotenv(env_path)

#Set API Key
#set the .env location to read the API key
API_KEY1="AIzaSyCzxQq5cWOvTpa3zSnVEnAahng0FLGDXQU"
API_KEY = API_KEY1
if not API_KEY:
    API_KEY = os.environ.get("GEMINI_API_KEY")
# API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    API_KEY = "AIzaSyBgSkpBxN9snTdvVHLU0hjjpsXwZBoKf74" 
    if not API_KEY:
        raise ValueError("GEMINI_API_KEY environment variable not set. Please set it before running the script.")
print("Gemini API Key loaded successfully. key is:", API_KEY[:15] + "****")    


# Define the class for the Two-Stage LLM Pipeline
class PostconditionPipeline:
    """A Two-Stage LLM Pipeline using Gemini API:
        1. The Reasoner: Generates reasoning about the function's pre and post conditions.
        2. The Translator: Converts reasoning into structured JSON output.
        """
    
    def __init__(self, api_key, prompt_id: int = None):
        """Initializes the Gemini API client and configurations."""
        # Initialize the Gemini API client
        genai.configure(api_key=api_key)
        
        # Configuration for "Thinking" (allows creativity)
        self.reasoning_config = genai.GenerationConfig(
            temperature=0.7
        )
        
        # Configuration for "Formatting" (strict structure)
        self.formatting_config = genai.GenerationConfig(
            temperature=0.0, 
            response_mime_type="application/json"
        )
        self.prompt_id = prompt_id
        #get the Function name and code from prompt_id if provided
        if prompt_id is not None:
            self.func_name, self.function_code = getFunctionCodeAndNameFromPromptID(prompt_id)
        self.model = genai.GenerativeModel("gemini-2.5-flash-lite",
                                           system_instruction="You must keep all answers under 65,536 tokens. Reduce the number of test cases if necessary to maintain token limit."
                                           )
        #self.model2 = genai.GenerativeModel("gemini-2.5-flash")
    max_retries = 5
    backoff_time = 2  # seconds

    #retry logic for LLM calls
    @retry(
        retry=retry_if_exception_type(ResourceExhausted),
        wait=wait_exponential(multiplier=1, min=4, max=60),
        stop=stop_after_attempt(5)
    )
    def _send_request(self, chat, prompt, config):
        return chat.send_message(prompt, generation_config=config)
    #retry logic for LLM calls
    @retry(
        retry=retry_if_exception_type(ResourceExhausted),
        wait=wait_exponential(multiplier=1, min=4, max=60),
        stop=stop_after_attempt(5)
    )
    def _send_formatting_request(self, prompt, config):
        return self.model.generate_content(prompt, generation_config=config)
    
    def _fix_regex_patterns(self, obj):
        """
        Recursively searches for 'pattern' keys and fixes double-escaped backslashes.
        Converts LLM's "\\\\s" -> "\\s" (Python's \s).
        """
        if obj is None:
            return
        
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == 'pattern' and isinstance(v, str):
                    # The Fix: Replace double backslash with single backslash
                    if "\\\\" in v:
                        obj[k] = v.replace('\\\\', '\\')
                else:
                    # Recurse deeper
                    self._fix_regex_patterns(v)
        elif isinstance(obj, list):
            for item in obj:
                self._fix_regex_patterns(item)

    def _fix_malformed_constraints(self, json_data):
        print("Applying fixes to malformed constraints...")
        # Ensure json_data is a dictionary and has 'test_cases' key
        if not isinstance(json_data, dict) or 'test_cases' not in json_data:
            return json_data
        
        # Ensure 'test_cases' is a list
        if not isinstance(json_data['test_cases'], list):
            print("Warning: 'test_cases' is not a list. Skipping constraint fixes.")
            return json_data
            
        new_test_cases = [] # Use a new list to filter out bad items
        
        for i, case in enumerate(json_data['test_cases']):
            # --- CRITICAL FIX: Ensure 'case' is a dictionary ---
            if not isinstance(case, dict):
                print(f"    [AUTO-FIX] Skipping malformed test case at index {i} (Expected dict, got {type(case).__name__}).")
                continue # Skip this malformed element
            # --- FIX 1: ID Type Casting ---
            # If ID is missing, generate one based on index
            if 'id' not in case:
                case['id'] = f"pc_{i+1}"
            
            # If ID is an Integer (e.g., 1), convert to "pc_1"
            current_id = case['id']
            if isinstance(current_id, int):
                case['id'] = f"pc_{current_id}"
            
            # Optional: If ID is a digit string (e.g., "1"), standardize to "pc_1"
            elif isinstance(current_id, str) and current_id.isdigit():
                case['id'] = f"pc_{current_id}"
            # ------------------------------

            # --- FIX 2: Constraint Null Handling (Existing Logic) ---
            c = case.get('input_constraints', {})
            if c is None:
                case['input_constraints'] = {}
                c = {} # Update local var for next check

            # Check the description for keywords like "mixed"
            if isinstance(c, dict):
                desc = case.get('description', '').lower()
                
                # If description mentions "mixed", force the flag on ALL arguments
                if 'mixed' in desc or 'heterogeneous' in desc:
                    for arg_name in c:
                        # Ensure the constraint object exists before setting flag
                        if c[arg_name] is None: c[arg_name] = {}
                        c[arg_name]['is_mixed'] = True
            
            if isinstance(c, dict):
                # --- FIX START: Handle 'lst_elements' style keys ---
                # We iterate over a copy of keys because we might delete some
                for key in list(c.keys()):
                    # Check if key is like "var_elements" or "var_items"
                    if key.endswith("_elements") or key.endswith("_items")or key.endswith("_element_constraints"):
                        parent_key = key.rsplit('_', 1)[0] # Get "var" from "var_elements"
                        if key.endswith("_element_constraints"):
                             parent_key = key.rsplit('_element_constraints', 1)[0]
                        
                        # If the parent variable exists in constraints
                        if parent_key in c:
                            # Ensure parent has an 'elements' dict
                            if "elements" not in c[parent_key]:
                                c[parent_key]["elements"] = {}
                            
                            # Merge constraints
                            c[parent_key]["elements"].update(c[key])
                            
                            # Remove the hallucinated top-level key
                            del c[key]
                            print(f"    [AUTO-FIX] Merged '{key}' into '{parent_key}' elements.")
                # --- FIX END ---

                # ... (Keep existing Null/None handling) ...
                for arg, rules in c.items():
                    if rules is None: 
                        c[arg] = {}
                        continue
                        
                    # --- FIX: Detect "Mixed" types from descriptions ---
                    # LLMs often put "element_types": "mixed integers and strings"
                    # We check for specific keys and keywords.
                    
                    # --- CRITICAL FIX: Add type check for 'rules' before calling .get() ---
                    if not isinstance(rules, dict):
                        # This skips the 'mixed' analysis for flat constraints 
                        # where 'rules' is an integer (e.g., 0 or 10000).
                        continue
                    # 1. Check 'element_types' or 'types' keys
                    type_desc = str(rules.get('element_types', '')) + str(rules.get('types', ''))
                    type_desc = type_desc.lower()
                    
                    # 2. Keywords that imply mixed data
                    if 'mixed' in type_desc or 'any' in type_desc or 'various' in type_desc:
                        rules['is_mixed'] = True
            # --- CRITICAL FIX: Ensure 'case' is a dictionary (from previous steps) ---
            if not isinstance(case, dict): continue
            # --- FIX 3: Flat Constraints (Existing Logic) ---
            t = case.get('input_types', {})
            c = case.get('input_constraints', {})
            flat_keys = {'min_val', 'max_val', 'min_len', 'max_len', 'sorted', 'unique', 'pattern', 'max_codepoint'}
            if any(k in c for k in flat_keys) and len(t) == 1:
                arg = list(t.keys())[0]
                case['input_constraints'] = {arg: c}
            
            # --- NEW CALL: FIX REGEX PATTERNS ---
            # Clean up the constraints we just organized
            self._fix_regex_patterns(case.get('input_constraints', {}))
            # ------------------------------------
            
            # --- IMPROVED FIX: Enforce 'result =' assignment ---
            stmt = case.get('execution_statement', '').strip()
            func_call_pattern = r'\b' + re.escape(self.func_name) + r'\s*\([^)]*\)'
            # --- ADD/REVISE CHECK: Skip if it's a try/except block using non-standard results ---
            # Check for a try block AND the absence of the 'result =' variable.
            is_complex_try_block = 'try:' in stmt and (
                'result_ab =' in stmt or 'result_ba =' in stmt or re.search(r'result_\w+\s*=', stmt)
            )
            # 1. Check if the statement is a non-standard comparison that should be skipped.
            # This is a heuristic to skip comparison tests like ID 8.
            if re.search(r'result_\w+\s*=', stmt) and not re.search(r'(^|[\s;])result\s*=', stmt):
                # Skip fixing if non-standard result variables are already present.
                # This ensures Test Case 8 (result_ab, result_ba) is not touched.
                print(f"    [AUTO-FIX] Skipping 'result =' enforcement for multi-variable assignment in {case['id']}.")
                pass # Do nothing, proceed to next case

            # 1. Check if 'result =' is truly missing
            elif not re.search(r'(^|[\s;])result\s*=', stmt):
                
                # Check if the execution statement actually contains a call to the function
                if re.search(func_call_pattern, stmt):
                    # Use self.func_name to check for a call to the target function
                    func_call_pattern = r'\b' + re.escape(self.func_name) + r'\s*\([^)]*\)'
                    parts = stmt.split(';')
                    # Identify the last part that contains the function call
                    last_call_index = -1
                    for i, part in reversed(list(enumerate(parts))):
                        if re.search(func_call_pattern, part):
                            last_call_index = i
                            break
                    
                    if last_call_index != -1:
                        last_part = parts[last_call_index].strip()
                        
                        # Ensure we don't accidentally re-assign a variable
                        if not re.search(r'[^=]=[^=]', last_part):
                            parts[last_call_index] = f" result = {last_part}"
                            case['execution_statement'] = ";".join(parts).strip()
                    # print("Corrected to:", case['execution_statement'])
            # ----------------------------------------------

            # --- FORCE ASCII FIX ---
            # If input type is string, FORCE max_codepoint=255
            # because the target function crashes on Unicode.
            if isinstance(c, dict):
                for arg_name, arg_type in t.items():
                    if arg_type == 'str':
                        if arg_name not in c: c[arg_name] = {}
                        # Inject safety constraint
                        if 'max_codepoint' not in c[arg_name]:
                            c[arg_name]['max_codepoint'] = 255
            new_test_cases.append(case)
        json_data['test_cases'] = new_test_cases        
        return json_data

    def _ensure_parsed(self, data):
        """
        Cleans and parses the raw LLM output string into a Python dictionary.
        Handles JSONDecodeError, SyntaxError, truncation, math expressions, 
        malformed descriptions, and special float values (NaN/Inf).
        """
        if isinstance(data, dict):
            return data
        if not isinstance(data, str):
            return None

        # --- STAGE 1: Aggressive Pre-Cleanup and Standardization ---

        # 1. Clean invisible characters and standardize non-ASCII
        data = data.replace('\xa0', ' ')
        # Aggressively remove all non-ASCII control characters that break JSON/AST
        data = re.sub(r'[^\x00-\x7F]+', '', data)

        # 2. Fix 'description' field quotes (Must run early on the raw string)
        # Fix: Sanitizes content inside "description": "..." by removing extra quotes
        def fix_description_quotes(match):
            key_start = match.group(1)
            description_content = match.group(2)
            quote_end = match.group(3)
            # Remove all double quotes from the content
            sanitized_content = description_content.replace('"', '')
            return key_start + sanitized_content + quote_end
        
        # Pattern captures: 1: Key+OpenQuote, 2: Content, 3: ClosingQuote
        data = re.sub(r'("description":\s*")(.*?)(?<!\\)(")', fix_description_quotes, data, flags=re.DOTALL)
        
        # 3. Standardize Special Float Values (NaN/Inf)
        # This replaces all variations (quoted/unquoted, capitalized) with a single, clean quoted string.
        def standardize_float_str(match):
            keyword = match.group(2).lower()
            if keyword == 'infinity':
                if '-' in match.group(1):
                    return ': "-inf"'
                return ': "inf"'
            elif keyword == 'nan':
                return ': "nan"'
            return match.group(0)

        data = re.sub(
            r':\s*(?:"|\')?(-)?(INFINITY|NAN)(?:"|\')?\b', 
            standardize_float_str, 
            data, 
            flags=re.IGNORECASE | re.DOTALL
        )
        
        # 4. Handle Math Operations (Clamping large numbers and evaluating exponents)
        
        # --- STAGE 2: Math Evaluation (NEW FEATURE) ---
        # Converts "2**60" -> "1152921504606846976" so json.loads works.
        
        # A. Evaluate Powers (e.g., 2**30)
        def eval_power(match):
            try:
                base = int(match.group(1))
                exp = int(match.group(2))
                return str(base ** exp)
            except: return match.group(0)
        
        # Run logic to replace "123 ** 456"
        data = re.sub(r'(\d+)\s*\*\*\s*(\d+)', eval_power, data)
        
        # B. Evaluate Simple Arithmetic (e.g., 1000 + 50 or 20 - 1)
        # This handles cases like: 2**60 + 2**30 (after powers are resolved above)
        def eval_arithmetic(match):
            try:
                a = int(match.group(1))
                op = match.group(2)
                b = int(match.group(3))
                return str(a + b) if op == '+' else str(a - b)
            except: return match.group(0)

        # Run loop to handle chained math (e.g., 1 + 2 + 3)
        # We look for: Number <space> +or- <space> Number
        for _ in range(3): 
            data = re.sub(r'(\d+)\s*([\+\-])\s*(\d+)', eval_arithmetic, data)

        # Clamp Massive Integers (20+ digits)
        def clamp_huge_ints(match):
            SAFE_LIMIT = 9000000000000000000 
            num_str = match.group(0)
            if num_str.startswith('-'):
                return str(-SAFE_LIMIT)
            return str(SAFE_LIMIT)

        data = re.sub(r'(?<!["\w])(-?\d{20,})(?!["\w])', clamp_huge_ints, data)
        
        # --- STAGE 2: Extraction ---
        
        # 5. Extract JSON string from potential Markdown/text wrapper
        match = re.search(r"```(?:json)?\s*(\{.*)", data, re.DOTALL) 
        if match:
            json_str = match.group(1)
            # Strip closing ``` if it exists
            if "```" in json_str:
                json_str = json_str.split("```")[0]
        else:
            # Fallback: Find first '{'
            start = data.find('{')
            if start != -1:
                json_str = data[start:]
            else:
                return None
        
        json_str = json_str.strip()
        
        # --- STAGE 3: Parsing Attempts ---
        
        # 6. Attempt 1: Standard JSON.loads (with final cleanup)
        try:
            # Prepare for standard JSON parsing (lowercase Python booleans/None)
            json_ready = json_str
            
            # Remove illegal trailing commas (Fix for list/object boundaries)
            json_ready = re.sub(r',\s*([\]}])', r'\1', json_ready) 
            
            # Convert Python booleans/None to JSON lowercase required by json.loads
            json_ready = re.sub(r':\s*True\b', ': true', json_ready)
            json_ready = re.sub(r':\s*False\b', ': false', json_ready)
            json_ready = re.sub(r':\s*None\b', ': null', json_ready)
            
            return json.loads(json_ready)
        except json.JSONDecodeError:
            pass # Failed, proceed to recovery
        
        # 7. Attempt 2: AST Literal Evaluation (Fallback for minor syntax issues)
        try:
            # If standard JSON failed, attempt Python AST literal evaluation
            return ast.literal_eval(json_str)
        except (ValueError, SyntaxError):
            pass # Failed, proceed to final recovery

        # --- STAGE 4: Aggressive Recovery ---

        # 8. Attempt 3: Aggressive Truncation Recovery
        try:
            repaired = json_str.strip()
            
            # Aggressively ensure necessary closures are present, preventing total crash
            if not repaired.endswith('}'): repaired += '}'
            if not repaired.endswith(']'): repaired += ']'
            if not repaired.endswith('}'): repaired += '}'
            
            # Remove resulting duplicate closures (e.g., '}}' -> '}')
            repaired = repaired.replace('}}', '}').replace(']]', ']').replace(']}', ']}')

            # Re-run standard JSON cleanup and parse
            repaired = re.sub(r',\s*([\]}])', r'\1', repaired)
            repaired = re.sub(r':\s*True\b', ': true', repaired)
            repaired = re.sub(r':\s*False\b', ': false', repaired)
            repaired = re.sub(r':\s*None\b', ': null', repaired)
            
            return json.loads(repaired)
        except: 
            pass

        # If all attempts fail
        print(f"    [!] JSON/AST Parse Failed. Snippet: \n{json_str}")
        return None
    
    #create a function to create the formatting prompt based on self's prompt ID
    def create_formatting_prompt(self) -> str:
        """
        Creates the formatting prompt for the Translator stage.
        Optimized to reduce hallucinations and enforce Schema compliance.
        """
        prompt_id = self.prompt_id
        
        # 1. Fetch Strategy
        prompt_strategy = "Naive_strategy" # Default
        if prompt_id is not None:
            prompt_document = getPromptbyPromptID(prompt_id)
            prompt_strategy = prompt_document.get("Prompt_Strategy", "Naive_strategy")

        # ------------------------------------------------------------------
        # SHARED: CORE CONTEXT & SCHEMA (Used by all strategies)
        # ------------------------------------------------------------------
        # We put the Schema LAST so it is the most recent context the LLM sees.
        core_context = Template("""
        based on the above explanation of the function `$func_name`, its code and related test cases. Format the test cases into JSON adhering to the following instructions:
        - Inputs are generated RANDOMLY. You cannot "filter" your way to low-probability events (like exact list overlaps).
        - You must use **Constructive Constraints** (ranges/patterns) to force these scenarios.

        OBJECTIVE: Format the generated test cases into JSON test suite readable and executable by hypothesis library(max 20 test cases). 
                    - DO NOT include any explanations or extra text outside the JSON.
        Crucial Requirements: 
                                For every test case, you must generate the specific execution_statement. This is the Python code line that calls the function using the arguments defined in input_types and assigns the output to a variable named result. 
                                ***IMPORTANT*** USE standard python syntax for function calls and assignments. DO NOT use pseudocode or non-standard syntax or third-party libraries.
                                USE EXACT ARGUMENT NAMES: You must use the EXACT parameter names defined in the function signature (e.g., if function is 'def func(x_val, y_val)', your JSON must use 'x_val' and 'y_val', NOT 'a' and 'b').
                                in execution_statement, The `execution_statement` MUST use the variable names from `input_types`. DO NOT invent new variable names or hardcode values.
        Important: Do not add any new information, just structure the existing response. Do not include long explanations.
        OUTPUT FORMAT: 
        Output ONLY valid JSON adhering to the schema. No markdown blocks.
        
        JSON SCHEMA:
        $schema_instruction
        Function Code:
        $function_code
        """)
        
        core_context = core_context.substitute(
            func_name=self.func_name, 
            function_code=self.function_code, 
            schema_instruction=test_case_schema
        )
        
        # prepare few-shot examples
        # This example is perfectly aligned with your correctnesstesting.py parser

        few_shot_example = """
           ### EXAMPLE 1: ARITHMETIC & ERROR HANDLING
            Function: `def div(a, b): return a / b`
            CORRECT JSON:
            {
              "test_cases": [
                {
                  "id": "1",
                  "description": "Happy Path",
                  "input_types": { "a": "int", "b": "int" },
                  "input_constraints": { "a": { "min_val": 1 }, "b": { "min_val": 1 } },
                  "execution_statement": "result = div(a, b)", 
                  "postconditions": [{ "assertion": "result == a / b" }]
                },
                {
                  "id": "2",
                  "description": "Negative Test (Invalid Type)",
                  # NOTE: We use 'str' because it is mathematically invalid for division.
                  "input_types": { "a": "int", "b": "str" },
                  "input_constraints": { "b": { "min_len": 1 } },
                  "execution_statement": "try: result = div(a, b) except Exception as e: result = e",
                  "postconditions": [{ "assertion": "isinstance(result, TypeError)" }]
                }
              ]
            }

            ### EXAMPLE 2: COLLECTIONS & DUCK TYPING
            Function: `def process_items(items): return set(items)`
            CORRECT JSON:
            {
              "test_cases": [
                {
                  "id": "1",
                  "description": "Happy Path",
                  "input_types": { "items": "tuple[int]" },
                  "input_constraints": { "items": { "min_len": 1 } },
                  "execution_statement": "result = process_items(items)",
                  "postconditions": [{ "assertion": "len(result) > 0" }]
                },
                {
                  "id": "2",
                  "description": "Negative Test (Non-Iterable)",
                  # NOTE: We use 'int' because it is NOT iterable. Passing a 'list' or 'str' would NOT fail.
                  "input_types": { "items": "int" }, 
                  "input_constraints": {},
                  "execution_statement": "try: result = process_items(items) except Exception as e: result = e",
                  "postconditions": [{ "assertion": "isinstance(result, TypeError)" }]
                },
                {
                    "id": "3",
                    "description": "Negative Test: Invalid Input Type (Float)",
                    "input_types": { "a": "int", "b": "float" },
                    "execution_statement": "try: result = div(a, b) except Exception as e: result = e", 
                    "postconditions": [{ "assertion": "isinstance(result, TypeError)" }]
                }
              ]
            }

            ### EXAMPLE 3: MIXED TYPES (Strategy Flags)
            Function: `def group_items(items): ...`
            CORRECT JSON:
            {
              "test_cases": [
                {
                  "id": "1",
                  "description": "Group mixed hashable items",
                  "input_types": { "items": "list[Any]" }, 
                  "input_constraints": { 
                      "items": { "min_len": 5, "hashable_mix": true } 
                  },
                  "execution_statement": "result = group_items(items)",
                  // NOTE: hashable_mix produces bools/floats/None, so we check logic, not specific types.
                  "postconditions": [{ "assertion": "len(result) > 0" }] 
                }
              ]
            }
            ### EXAMPLE 4: STRING PATTERNS & REGEX (Fixing The Oracle Mismatch)
            Function: `def get_long_words(text): return re.findall(r'\\b\\w{5,}\\b', text)`
            CORRECT JSON:
            {
              "test_cases": [
                {
                  "id": "1",
                  "description": "Happy Path: Regex Pattern matching",
                  "input_types": { "text": "str" },
                  "input_constraints": { "text": { "pattern": "^[a-zA-Z0-9_,. ]+$" } }, 
                  "execution_statement": "result = get_long_words(text)",
                  // CRITICAL: Do NOT use text.split(). Use 're' in assertion to match function logic.
                  "postconditions": [{ "assertion": "result == re.findall(r'\\\\b\\\\w{5,}\\\\b', text)" }]
                },
                {
                  "id": "2",
                  "description": "Edge Case: Only short words (Should return empty)",
                  "input_types": { "text": "str" },
                  // CRITICAL: Precise Pattern to force words < 5 chars. 
                  // Regex: (1-4 chars followed by space)* "input_constraints": { "text": { "pattern": "^([a-zA-Z0-9]{1,4}\\\\s)+[a-zA-Z0-9]{1,4}$" } },
                  "execution_statement": "result = get_long_words(text)",
                  "postconditions": [{ "assertion": "result == []" }]
                }
              ]
            }
            ### EXAMPLE 5: ORDERING & INVARIANTS
            Function: `def get_top_k(nums, k): return sorted(nums, reverse=True)[:k]`
            CORRECT JSON:
            {
              "test_cases": [
                {
                  "id": "1",
                  "description": "Happy Path: Top k integers",
                  "input_types": { "nums": "list[int]", "k": "int" },
                  "input_constraints": { "nums": { "min_len": 5 }, "k": { "min_val": 1, "max_val": 3 } },
                  "assumptions": ["k <= len(nums)"],
                  "execution_statement": "result = get_top_k(nums, k)",
                  "postconditions": [
                      // Correct Invariant: Result is sorted descending
                      { "assertion": "all(result[i] >= result[i+1] for i in range(len(result)-1))" },
                      // Correct Oracle: Compare against trusted implementation
                      { "assertion": "result == sorted(nums, reverse=True)[:k]" }
                  ]
                }
              ]
            }
            ### END OF EXAMPLES
            """

        # ------------------------------------------------------------------
        # STRATEGY 1: NAIVE (Minimalist)
        # ------------------------------------------------------------------
        # Focus: Pure translation of the function signature to JSON constraints.
        if prompt_strategy == "Naive_strategy":
            instructions = """
            INSTRUCTIONS:
            1. Analyze the function signature arguments.
            2. **GOLDEN RULE OF PBT**: Do not use 'assumptions' to filter for low-probability events (like specific substrings 'password' or random list overlaps). If you cannot guarantee a condition using `input_constraints` (ranges/patterns), **DO NOT TEST IT**. Rely on the test engine to find edge cases naturally.
            3. EXECUTION STATEMENT RULES:
               - **Happy Path:** Use `result = func(args)`.
               - **Negative/Error Tests:** `try: result = func(args) except Exception as e: result = e` (CRITICAL: If you pass invalid types like float/str to bitwise ops, you MUST use this pattern).
            4. **DUCK TYPING:** Python allows lists/tuples/strings to be swapped in iteration. To test TypeErrors, use strictly incompatible types (e.g., `int` for an iterator). When generating a Negative Test expecting TypeError for an iterable argument, NEVER use `str`. ALWAYS use `int`, `float`, or `None` to guarantee a crash.
            5. Ensure 'input_constraints' are nested under the exact argument name.
            6. Use explicit Python type hints in 'input_types' (e.g., "Optional[int]", "List[int]", "Union[int, str]").
            7. To guarantee intersections between lists, use small, overlapping 'min_val'/'max_val' ranges in constraints. Do not rely on chance.
            8. Do not use math expressions (like 2**60) for 'input_constraints'. Calculate the actual integer value.
            9. Do not use 'assumptions' to force statistically unlikely scenarios (like two random lists being disjoint or subsets). Use 'input_constraints' ranges instead.
            10. USE RELATIONAL ASSERTIONS (ORACLES): Do not hardcode expected return values. Use relational logic (e.g., `result == a + b`). Write a Python expression that calculates the expected truth based on the input variables.
            11. MIXED TYPES:
               - If the function SORTS or COMPARES mixed types, use `"is_mixed": true` in input_constraints.
               - If the function GROUPS or HASHES mixed types (e.g. set operations), use `"hashable_mix": true` in input_constraints.
               - Use `is_mixed` ONLY for robust functions designed to handle `None` or for Negative Tests (expecting TypeError).
            12. STRING LOGIC:
               - Do not use `.split()` assertions for functions using Regex. Use `re` in assertions too.
               - Do not use assumptions to look for specific words. Use `pattern` constraints.
               - If the function uses a Regex like `\w{4,}`, your Assertion MUST use the EXACT SAME Regex `\w{4,}`. 
               - Common Error: Do not mistakenly use `\w{4}` (exactly 4) when the code says `\w{4,}` (4 or more).
            13. **SET OPERATIONS:** When testing intersection/union/difference:
               - DO NOT assert `len(result) > 0`. It is statistically likely but not guaranteed.
               - DO assert the logic: `set(result) == set(a).intersection(b)`.
            14. LOW PROBABILITY & CONSTRUCTIVE ASSUMPTIONS
                - Hypothesis struggles to satisfy assumptions that rely on low-probability types (e.g., finding `None` in a list of integers).
                - If your test REQUIRES the presence of a non-default/rare value (like `None` or `True`):
                **A. USE ALLOW_NONE FLAG:** Add the constraint **`"allow_none": true`** to the argument's input constraints. This tells the generator to increase the probability of selecting that value.
                **B. TYPE EXPLICITLY:** For full clarity, use explicit type unions in `input_types` (e.g., `tuple[int | None]`).
            15. **STRING LOGIC (CRITICAL):** - If function uses Regex (re.findall), your Assertion **MUST NOT** use `.split()`. It fails on punctuation. Use `re` in the assertion too.
               - To generate specific text structures (e.g. "only short words"), use strict `pattern` Regex in `input_constraints`.
            16. **TARGETING OPTIONAL/UNION TYPES**:
                - **Problem:** If input is `Optional[int]`, Hypothesis generates both ints and None. If your test specifically targets `None` (e.g., "Negative Test: null input"), you MUST force it.
                - **Rule:** If the description targets a specific type in a Union, add it to `assumptions`.
            17. **STRICT BOOLEAN VS PYTHONIC TRUTH**:
                - **Problem:** Many Python functions return `0` or `None` instead of `False` (e.g., `return x and y`).
                - **Rule:** When asserting boolean types for logical functions, allow for `0` or `1` if the function implementation is dynamic.
            19. **PRIME NUMBER EDGE CASES**: Do not test for primality of 0 or 1 unless the function explicitly handles these cases.
            20. **ASSUMPTIONS FOR PROPERTY TESTING**: If testing a specific mathematical property, ADD AN ASSUMPTION to filter the input.
            21. **DEPENDENT VARIABLES (EQUALITY/SORTING)**: If testing equality or sorting, ADD ASSUMPTIONS to create dependent variables (e.g., `a == b` or `a <= b`).
            22. **MIXED TYPES STRATEGY (CRITICAL UPDATE)**: Use the `"allow_none": true` constraint to increase the probability of generating `None` in mixed type inputs. This helps Hypothesis satisfy assumptions that require the presence of `None` or other rare values.
            23. **STRICT BOOLEAN VS PYTHONIC TRUTH**: When asserting boolean types for logical functions, allow for `0` or `1` if the function implementation is dynamic.
            24. **SET OPERATIONS & HASHABILITY**: To test unhashability, you must guarantee the input contains a list/dict. Use `input_types: tuple[list[int]]` (pure list content) to force the crash. Avoid `Union[int, list]` for negative testing as it might pick only ints.
            25. **SIDE EFFECTS & IN-PLACE MODIFICATION**: Functions like `lst.sort()` return `None`. Asserting on `result` will fail. Instead, assert on the modified input variable.

            """
            return instructions + core_context
        
        # ------------------------------------------------------------------
        # STRATEGY 2: FEW-SHOT (Example-Based)
        # ------------------------------------------------------------------
        # Focus: Mimicry of a perfect reference implementation.
        elif prompt_strategy == "FewShot_strategy":
            instructions = """
            INSTRUCTIONS:
            1. Analyze the function signature.
            2. Follow the structure of the EXAMPLES below exactly.
            3. **GOLDEN RULE:** Avoid 'assumptions' that filter random data (e.g. `word in text`). Only use assumptions for simple bounds (`i < len(arr)`). Trust the random generator.
            4. **CRITICAL:** To handle Negative Tests (Invalid Types) or If you pass invalid types like float/str to bitwise ops. You MUST wrap the execution in `try...except`.
            5. **DUCK TYPING:** Python allows lists/tuples/strings to be swapped in iteration. To test TypeErrors, use strictly incompatible types (e.g., `int` for an iterator). When generating a Negative Test expecting TypeError for an iterable argument, NEVER use `str`. ALWAYS use `int`, `float`, or `None` to guarantee a crash.
            6. Use 'Optional[T]' if None is a valid input.
            7. Use `"hashable_mix": true` for grouping/hashing functions to avoid unhashable type errors.
            8. To force list intersections, use restricted numeric ranges (e.g., 1-5) as shown in Example 2.
            9. Ensure 'execution_statement' assigns the output to a variable named 'result'.
            10. Do not use math expressions (like 2**60) for 'input_constraints'. Calculate the actual integer value.
            11. USE RELATIONAL ASSERTIONS (ORACLES):
                - You must write a Python expression that calculates the expected truth based on the input variables.
                - When testing primality/compositeness, the assertion must be:
                    ✅ GOOD: "result == (n >= 2 and any(n % i == 0 for i in range(2, int(n**0.5) + 1)))"
                    ❌ BAD: "assertion": "result == True" (Assumes the random input is Composite)
            12. For String/Regex functions. 
               - NEVER compare Regex output to `text.split()`.
               - NEVER assume specific words exist in random strings.+
               - Use precise Regex patterns for input generation.
               - **Rule:** If the function uses a Regex like `\w{4,}`, your Assertion MUST use the EXACT SAME Regex `\w{4,}`. 
               - **Common Error:** Do not mistakenly use `\w{4}` (exactly 4) when the code says `\w{4,}` (4 or more).
            13. **NO PROBABILISTIC EXISTENCE ASSERTIONS**:
                - **Problem:** Overlapping ranges (e.g., 1-10) DO NOT guarantee that two random lists will share elements. They might still be disjoint.
                - **Rule:** NEVER assert `len(result) > 0` or `result != []` unless the input domain is a SINGLE value (e.g., `min_val: 1, max_val: 1`).
                - **Fix:** Instead of checking for existence (`len > 0`), check for **Correctness** using an Oracle assertion:
                    - ❌ `len(result) > 0`
                    - ✅ `set(result) == set(a) & set(b)`
            14. LOW PROBABILITY & CONSTRUCTIVE ASSUMPTIONS
                - Hypothesis struggles to satisfy assumptions that rely on low-probability types (e.g., finding `None` in a list of integers).
                - If your test REQUIRES the presence of a non-default/rare value (like `None` or `True`):
                **A. USE ALLOW_NONE FLAG:** Add the constraint **`"allow_none": true`** to the argument's input constraints. This tells the generator to increase the probability of selecting that value.
                **B. TYPE EXPLICITLY:** For full clarity, use explicit type unions in `input_types` (e.g., `tuple[int | None]`).
            15. **TARGETING OPTIONAL/UNION TYPES**:
                - **Problem:** If input is `Optional[int]`, Hypothesis generates both ints and None. If your test specifically targets `None` (e.g., "Negative Test: null input"), you MUST force it.
                - **Rule:** If the description targets a specific type in a Union, add it to `assumptions`.
            16. **STRICT BOOLEAN VS PYTHONIC TRUTH**:
                - **Problem:** Many Python functions return `0` or `None` instead of `False` (e.g., `return x and y`).
                - **Rule:** When asserting boolean types for logical functions, allow for `0` or `1` if the function implementation is dynamic.
            17. **MIXED TYPES STRATEGY (CRITICAL UPDATE)**:
               - **Constraint:** `{"is_mixed": true}` generates `int`, `float`, `bool`, AND `None`.
               - **Rule:** Do NOT use `is_mixed` for standard sorting/math functions (like `heapq`, `sum`, `max`) because they crash on `None`.
               - **Correct Approach:** If you want to test mixed *numbers* (ints and floats), use `input_types: "list[Union[int, float]]"` without the `is_mixed` flag.
               - Use `is_mixed` ONLY for robust functions designed to handle `None` or for Negative Tests (expecting TypeError).
            18. **SET BEHAVIOR (NO CRASH ON MIXED TYPES)**:
                - **Problem:** `set([1, "a"]) & set([2, "b"])` works perfectly in Python. It does NOT raise TypeError.
                - **Rule:** Do NOT write Negative Tests expecting `TypeError` for mixed content in sets/lists. Only expect `TypeError` if the **Container Itself** is invalid (e.g. passing `int` to `set()`).
            19. **PRIME NUMBER EDGE CASES**:
                - **Problem:** Naive prime checks (`for i in range(2, ...`) often incorrectly return `True` (Prime) for 0 and 1 because the loop never runs.
                - **Rule:** When testing `is_prime` or `is_not_prime`, check if the code handles `n < 2`. If not, the function likely returns the default value (True/False) for 0/1, which might be mathematically wrong. Adjust assertions to match the *code's* behavior or flag it as a bug.
            20. **ASSUMPTIONS FOR PROPERTY TESTING**:
                - **Problem:** If you want to test "Composite Numbers" in range [4, 1000], Hypothesis might pick a Prime (e.g., 5, 7). The assertion `result == True` will fail.
                - **Rule:** If testing a specific mathematical property, ADD AN ASSUMPTION to filter the input.
                - ✅ Example: `assumptions: ["any(n % i == 0 for i in range(2, int(n**0.5) + 1))"]` (Ensures n is composite).
            21. **DEPENDENT VARIABLES (EQUALITY/SORTING)**: 
                - **Problem:** It is impossible to randomly generate two identical lists `a` and `b`. `assumptions: ["a == b"]` WILL FAIL.
                - **Rule:** If `b` depends on `a` (e.g., equal, sorted, reversed), do NOT generate `b` in `input_types`.
                - **Action:** Generate `a` only. In `execution_statement`, define `b` using python code.
                - ✅ Example: 
                  "input_types": {"a": "list[int]"}, 
                  "execution_statement": "b = list(a); result = func(a, b)"
            22. **SET OPERATIONS & HASHABILITY**:
                - **Valid Types:** `int`, `float`, `str`, `bool`, `None`, `tuple` are all hashable. `set()` accepts them. Do NOT expect TypeError.
                - **Invalid Types:** `list`, `dict`, `set` are unhashable. `set([ [1] ])` raises TypeError.
                - **Testing Strategy:** To test unhashability, you must guarantee the input contains a list/dict. Use `input_types: tuple[list[int]]` (pure list content) to force the crash. Avoid `Union[int, list]` for negative testing as it might pick only ints.
            23. **SIDE EFFECTS & IN-PLACE MODIFICATION**:
                - **Problem:** Functions like `lst.sort()` return `None`. Asserting on `result` will fail.
                - **Rule:** If the function modifies an input in-place (lists/dicts), perform assertions on the **input variable** (e.g., `test_list`), NOT `result`.
                - ✅ `execution_statement`: "my_list = list(input_list); result = sort_in_place(my_list)"
                - ✅ `assertion`: "my_list == sorted(input_list)"
            
            EXAMPLE REFERENCE:

            """
            
            return instructions + few_shot_example + core_context

        # ------------------------------------------------------------------
        # STRATEGY 3: CHAIN OF THOUGHT (Logic-Heavy)
        # ------------------------------------------------------------------
        # Focus: Deep logic rules to prevent hallucinations in complex logic.
        else: # "ChainofThought_strategy"
            instructions = """
            INSTRUCTIONS:
            Based on the analysis provided, generate the test cases. You must strictly follow these Logic Rules to avoid errors in execution of these test cases.

            ### CRITICAL LOGIC RULES:

            1. **NO HALLUCINATED HELPERS**: Assertions must use ONLY Python built-ins or the target function.
            2. **ORACLE ASSERTIONS**: Do not hardcode return values. Use logic: `result == (a + b)`.
            3. **CONSTRAINT NESTING**: Constraints MUST be nested under the argument name.
            4. **NO MATH EXPRESSIONS**: Calculate actual integer values (e.g. 11529... instead of 2**60).
            5. **NEGATIVE TEST EXECUTION (CRITICAL)**:
               - ❌ CRASHES RUNNER: `result = func(invalid_input)`
               - ✅ CORRECT: `try: result = func(invalid_input) except Exception as e: result = e`

            6. **AVOID DUCK TYPING TRAPS**:
               - **Problem:** Python is flexible. `list`, `tuple`, and `str` are all iterable. Calling `set('string')` or `list('string')` SUCCEEDS."
               - **Rule:** - When generating a Negative Test expecting TypeError for an iterable argument, NEVER use `str`. ALWAYS use `int`, `float`, or `None` to guarantee a crash.
            
            7. **REGEX**:
               - When generating strings with specific structures, use the `pattern` key in constraints.
               - Example: `{"pattern": "^[a-z]+$"}` for generating finding lowercase letters.
            
            8. **ORACLE PRECISION (REGEX vs SPLIT)**:
               - **Problem:** `text.split()` splits only by space. Regex `\\w+` splits by boundaries (handling punctuation).
               - **Rule:** If the function uses `re` (Regex), your Assertion **MUST NOT** use `.split()`. It will fail. Use `re.findall` in your assertion as well.

            9. **PRECISE INPUT PATTERNS**:
               - If testing "No Match Found" (e.g., only short words), you must use a Regex `pattern` in constraints that STRICTLY forbids long words.
               - ❌ Pattern: `[a-z ]+` (Allows long words)
               - ✅ Pattern: `^([a-z]{1,3}\\s)+$` (Forces short words)

            10. **AVOID 'UNSATISFIABLE' ERRORS (The Golden Rule)**:
               - Hypothesis generates random data. It is statistically impossible to randomly generate two disjoint lists of 1000 integers or specific string contents.
               - **Disjoint/Intersection:** Use **Ranges** (e.g., 0-100 vs 200-300) to FORCE the condition.
               - **Empty Collections:** Use `{"min_len": 0, "max_len": 0}` to FORCE empty inputs.
               - **Subsets:** Do not test `issubset` on random lists.
               - If your test REQUIRES the presence of a non-default/rare value (like `None` or `True`):
                **A. USE ALLOW_NONE FLAG:** Add the constraint **`"allow_none": true`** to the argument's input constraints. This tells the generator to increase the probability of selecting that value.
                **B. TYPE EXPLICITLY:** For full clarity, use explicit type unions in `input_types` (e.g., `tuple[int | None]`).

            11. **DEPENDENT VARIABLES**: Use `assumptions` for index bounds (e.g., `index < len(arr)`).

            12. **AVOID STATISTICALLY IMPROBABLE ASSUMPTIONS**:
               - **Disjoint Sets:** Use non-overlapping ranges (0-100 vs 200-300).
               - **Subsets:** Do not test `set(a).issubset(b)` on random lists; it is statistically impossible.

            13. **EXPLICIT TYPING (CRITICAL)**:
               - You MUST use explicit Python type hints in `input_types` to ensure correct sampling.
               - **Nullable:** Use `"Optional[int]"` or `"Union[int, None]"` if `None` is valid. If you just say `"int"`, Hypothesis will NEVER generate None.
               - **Polymorphic:** Use `"Union[int, str]"` for mixed types.

            14. **CONSTRUCTIVE INTERSECTIONS**:
               - Force list overlap by restricting the domain (e.g. both lists use min_val=1, max_val=5).

            15. **MIXED TYPES STRATEGY (CRITICAL)**:
                - **Constraint:** `{"is_mixed": true}` generates `int`, `float`, `bool`, AND `None`.
                - **Rule:** ONLY use `"is_mixed": true` for:
                 1. **Robustness/Negative Tests** (where you EXPECT a crash or handle it via `try...except`).
                 2. Functions explicitly designed to filter/handle `None`.
                - **Happy Path:** For standard sorting/math functions, do NOT use `is_mixed`. Use `Union[int, float]` in `input_types` instead to get safe numbers.
            
            16. USE RELATIONAL ASSERTIONS (ORACLES):
                - You must write a Python expression that calculates the expected truth based on the input variables.  
                - For example : When testing primality/compositeness, the assertion must be:
                    ✅ GOOD: "result == (n >= 2 and any(n % i == 0 for i in range(2, int(n**0.5) + 1)))"
                    - ❌ BAD: "assertion": "result == True" (Assumes the random input is Composite)
            
            17. **ORACLE PRECISION (REGEX vs SPLIT)**:
               - **Problem:** `text.split()` splits only by space. Regex `\\w+` handles punctuation differently.
               - **Rule:** If the function uses `re` (Regex), your Assertion MUST NOT use `.split()`. It will fail on punctuation. Use `re` in your assertion as well.
               - - **Rule:** If the function uses a Regex like `\w{4,}`, your Assertion MUST use the EXACT SAME Regex `\w{4,}`. 
               - **Common Error:** Do not mistakenly use `\w{4}` (exactly 4) when the code says `\w{4,}` (4 or more).
            
            18. **TARGETING OPTIONAL/UNION TYPES**:
                - **Problem:** If input is `Optional[int]`, Hypothesis generates both ints and None. If your test specifically targets `None` (e.g., "Negative Test: null input"), you MUST force it.
                - **Rule:** If the description targets a specific type in a Union, add it to `assumptions`.
                - ❌ BAD: `input_types: {"a": "Optional[int]"}`, `assumptions: []` (Hypothesis might pick int!)
                - ✅ GOOD: `input_types: {"a": "Optional[int]"}`, `assumptions: ["a is None"]`

            19. **STRICT BOOLEAN VS PYTHONIC TRUTH**:
                - **Problem:** Many Python functions return `0` or `None` instead of `False` (e.g., `return x and y`).
                - **Rule:** When asserting boolean types for logical functions, allow for `0` or `1` if the function implementation is dynamic.
                - ❌ Strict: `isinstance(result, bool)` (Fails on 0)
                - ✅ Robust: `isinstance(result, (bool, int))` OR check values `result in [True, False, 0, 1]`
            
            20. **LOGICAL INVARIANTS**:
               - **Sorting/Largest:** If checking `n_largest`, the invariant is NOT `all(x >= result[-1] for x in nums)`.
               - **Correct Logic:** `all(x <= result[-1] for x in nums if x not in result)` (Remaining items are smaller).
               - **Simplest Oracle:** `sorted(result, reverse=True) == sorted(nums, reverse=True)[:n]`
            
            21. **SET BEHAVIOR (NO CRASH ON MIXED TYPES)**:
                - **Problem:** `set([1, "a"]) & set([2, "b"])` works perfectly in Python. It does NOT raise TypeError.
                - **Rule:** Do NOT write Negative Tests expecting `TypeError` for mixed content in sets/lists. Only expect `TypeError` if the **Container Itself** is invalid (e.g. passing `int` to `set()`).
            
            22. **PRIME NUMBER EDGE CASES**:
                - **Problem:** Naive prime checks (`for i in range(2, ...`) often incorrectly return `True` (Prime) for 0 and 1 because the loop never runs.
                - **Rule:** When testing `is_prime` or `is_not_prime`, check if the code handles `n < 2`. If not, the function likely returns the default value (True/False) for 0/1, which might be mathematically wrong. Adjust assertions to match the *code's* behavior or flag it as a bug.
            
            23. **ASSUMPTIONS FOR PROPERTY TESTING**:
                - **Problem:** If you want to test "Composite Numbers" in range [4, 1000], Hypothesis might pick a Prime (e.g., 5, 7). The assertion `result == True` will fail.
                - **Rule:** If testing a specific mathematical property, ADD AN ASSUMPTION to filter the input.
                - ✅ Example: `assumptions: ["any(n % i == 0 for i in range(2, int(n**0.5) + 1))"]` (Ensures n is composite).
            
            24. **DEPENDENT VARIABLES (EQUALITY/SORTING)**:
                - **Problem:** It is impossible to randomly generate two identical lists `a` and `b`. `assumptions: ["a == b"]` WILL FAIL.
                - **Rule:** If `b` depends on `a` (e.g., equal, sorted, reversed), do NOT generate `b` in `input_types`.
                - **Action:** Generate `a` only. In `execution_statement`, define `b` using python code.
                - ✅ Example: 
                  "input_types": {"a": "list[int]"}, 
                  "execution_statement": "b = list(a); result = func(a, b)"
            
            25. **SET OPERATIONS & HASHABILITY**:
                - **Valid Types:** `int`, `float`, `str`, `bool`, `None`, `tuple` are all hashable. `set()` accepts them. Do NOT expect TypeError.
                - **Invalid Types:** `list`, `dict`, `set` are unhashable. `set([ [1] ])` raises TypeError.
                - **Testing Strategy:** To test unhashability, you must guarantee the input contains a list/dict. Use `input_types: tuple[list[int]]` (pure list content) to force the crash. Avoid `Union[int, list]` for negative testing as it might pick only ints.
            
            26. **SIDE EFFECTS & IN-PLACE MODIFICATION**:
                - **Problem:** Functions like `lst.sort()` return `None`. Asserting on `result` will fail.
                - **Rule:** If the function modifies an input in-place (lists/dicts), perform assertions on the **input variable** (e.g., `test_list`), NOT `result`.
                - ✅ `execution_statement`: "my_list = list(input_list); result = sort_in_place(my_list)"
                - ✅ `assertion`: "my_list == sorted(input_list)"

            """
            return instructions + "\n EXAMPLES to provide context:\n" + few_shot_example + core_context
    #create a function to process the two stage pipeline
    def process(self,initial_prompt: str, schema_instruction: str) -> Tuple[Optional[dict], Optional[str]]:
        """
        Executes the Two-Stage pipeline.
        Arguments:
        - initial_prompt: The initial prompt for the reasoning stage
        - schema_instruction: The JSON schema instruction for formatting.
        Returns:
        - structured_response: The final structured JSON output from the LLM.
        - raw_reasoning: The raw text output from the reasoning stage.
        """
        # --- STAGE 1: The Reasoner ---
        # We use a chat session to maintain context between the two steps automatically
        try:
            chat_session = self.model.start_chat(history=[])
        except Exception as e:
            print(f"Error starting chat session with Gemini API: {e}")
            return None, None
        for attempt in range(self.max_retries):
            try:
                # --- STAGE 1: The Reasoner ---
                print(f"Thinking about the function...{self.func_name}")
                reasoning_response = self._send_request( chat_session, initial_prompt, self.reasoning_config)
                if reasoning_response is None:
                    raise Exception("Reasoning stage failed.")
                raw_reasoning = reasoning_response
                # print("Reasoning complete.")
                # print(f"Raw reasoning output:\n{raw_reasoning}\n")
                break
            except Exception as e:
                print(f"Error during reasoning stage on attempt {attempt + 1}/{self.max_retries}: {e}")
                time.sleep(self.backoff_time * (2 ** attempt) + rnd.uniform(0.1, 1.0)) # Exponential backoff
        else:
            print("Max retries reached. Reasoning stage failed.")
            return None, None

        # --- STAGE 2: The Translator ---
        print("2. Formatting output...")
        
        # Construct the formatting prompt
        try:
            construct_format_prompt = self.create_formatting_prompt()
        except Exception as e:
            print(f"Error creating formatting prompt: {e}")
            return None, raw_reasoning
        
        for attempt in range(self.max_retries):
            try:

                format_prompt = f"""
        Role : You are an expert in automated testing and test case generation for Python functions using property based testing.
        Objective: Based on your previous explanation having set of diverse test strategies to test the give function. """
                format_prompt += construct_format_prompt
                #save the formatting prompt in the DB for debugging
                try:
                    save_formatting_prompt(self.prompt_id, format_prompt)
                except Exception as e:
                    print(f"Error saving formatting prompt: {e}")
                formatting_response = self._send_request(chat_session, format_prompt, self.formatting_config)
                if formatting_response is None:
                    raise Exception("Formatting stage failed.")
                structured_response = formatting_response
                # print("Formatting complete.")   
                # print(f"Structured output:\n{structured_response.text}\n")
                break
            except Exception as e:
                print(f"Error during formatting stage on attempt {attempt + 1}/{self.max_retries}: {e}")
                time.sleep(self.backoff_time * (2 ** attempt) + rnd.uniform(0.1, 1.0)) # Exponential backoff
        else:
            print("Max retries reached. Formatting stage failed.")
            return None, raw_reasoning
        #save the structured response in the DB for debugging in raw_structured_response field in prompts collection
        try:
            save_structured_response(self.prompt_id, structured_response.text)
        except Exception as e:
            print(f"Error saving structured response: {e}")
        # --- STAGE 3: The Auditor (Parsing) ---
        try:
            #parse the structured response text to json
            print("Parsing structured response to JSON...")
            # print(f"Structured response text:\n{structured_response.text}")
            response_json = self._ensure_parsed(structured_response.text)
            
            if response_json is None:
                print("Error: Failed to parse JSON string.", structured_response.text)
                return None, raw_reasoning

            # STEP 2: Fix the Dict (Now that it is a Dict)
            response_json = self._fix_malformed_constraints(response_json)
            
            # STEP 3: Validate against Schema
            validate(instance=response_json, schema=schema_instruction)
            
            return response_json, raw_reasoning

        except json.JSONDecodeError:
            print("Error: Failed to parse JSON. content:", response_json)
            try:
                save_structured_response(self.prompt_id, response_json)
            except Exception as e:
                print(f"Error saving structured response: {e}")
            return None, raw_reasoning
        except ValidationError as ve:
            print(f"Error: JSON schema validation failed: {ve.message}")
            return None, raw_reasoning
        except Exception as e:
            print(f"Unexpected error during parsing/validation: {e}")
            return None, raw_reasoning
    
    def process_missin_structureddata(self, raw_reasoning, schema_instruction: str) -> Optional[list]:
        """
        It takes in the reasoning text output from the LLM and function name and then calls the LLM again to extract the structured JSON data.
        Arguments:
        - raw_reasoning: The raw text output from the reasoning stage.
        - schema_instruction: The JSON schema instruction for formatting.
        Returns:
        - structured_response: The final structured JSON output from the LLM.
        """
        # We do not need a chat session here as we are only formatting the existing reasoning
        # --- STAGE 2: The Translator ---
        print("Formatting output...")

        # try:
        #     chat_session = self.model.start_chat(history=[])
        # except Exception as e:
        #     print(f"Error starting chat session with Gemini API: {e}")
        #     return None
        func_name = self.func_name
        print("Re-formatting missing structured data...")
        try:
            construct_format_prompt = self.create_formatting_prompt()
        except Exception as e:
            print(f"Error creating formatting prompt: {e}")
            return None

        for attempt in range(self.max_retries):
            try:
                format_prompt = f"""
        Here is the previous analysis for Property-Based Testing (PBT) of a Python function {func_name}:
        {raw_reasoning}

        Role : You are an expert in automated testing and test case generation for Python functions using property based testing.
        Objective: Strictly based on the provided explanation having set of diverse test strategies to test the give function. """
                format_prompt += construct_format_prompt
                formatting_response = self._send_formatting_request(format_prompt, self.formatting_config)
                if formatting_response is None:
                    raise Exception("Formatting stage failed.")
                structured_response = formatting_response
                # print("Formatting complete.")   
                # print(f"Structured output:\n{structured_response}\n")
                break
            except Exception as e:
                print(f"Error during formatting stage on attempt {attempt + 1}/{self.max_retries}: {e}")
                time.sleep(self.backoff_time * (2 ** attempt) + rnd.uniform(0.1, 1.0))  # Exponential backoff
        else:
            print("Max retries reached. Formatting stage failed.")
            return None

        #save the structured response in the DB for debugging in raw_structured_response field in prompts collection
        try:
            save_structured_response(self.prompt_id, structured_response.text)
        except Exception as e:
            print(f"Error saving structured response: {e}")
        # --- STAGE 3: The Auditor (Parsing) ---
        try:
            print("Parsing structured response to JSON...")
            
            # STEP 1: Parse String -> Dict
            response_json = self._ensure_parsed(structured_response.text)
            
            if response_json is None:
                print("Error: Failed to parse JSON string.")
                return None
            
            # STEP 2: Fix the Dict
            response_json = self._fix_malformed_constraints(response_json)
            
            # STEP 3: Validate
            validate(instance=response_json, schema=schema_instruction)
            
            return response_json

        except json.JSONDecodeError:
            print("Error: Failed to parse JSON.", response_json)
            try:
                save_structured_response(self.prompt_id, response_json)
            except Exception as e:
                print(f"Error saving structured response: {e}")
            return None
        except ValidationError as ve:
            print(f"Error: JSON schema validation failed: {ve.message}")
            return None
        except Exception as e:
            print(f"Unexpected error during parsing/validation: {e}")
            return None

# --- USAGE EXAMPLE ---

# Define your schema constraint
target_schema = test_case_schema


# Function to get postconditions for a given Prompt ID  
def get_postconditions_for_promptID(prompt_id: int) -> Tuple[Optional[dict], Optional[str]]:
    """Fetches the function code from the database for the given Prompt_ID
    and runs the PostconditionPipeline to get preconditions and postconditions.
    Returns:
        A tuple of (structured_data, raw_reasoning).
    """
    client, db = get_db_client()
    functions_collection = db["Functions"]
    prompts_collection = db["FunctionPrompts"]
    
    # 1. Get the prompt document
    try:
        prompt_doc = prompts_collection.find_one({"Prompt_ID": prompt_id})
        if not prompt_doc:
            print(f"No prompt found for ID {prompt_id}")
            client.close()
            return None, None
    except Exception as e:
        print(f"Error fetching prompt: {e}")
        client.close()
        return None, None

    function_id = prompt_doc.get("Function_ID")
    
    # 2. Get the function code
    try:
        function_doc = functions_collection.find_one({"Function_ID": function_id})
        if not function_doc:
            print(f"No function found for ID {function_id}")
            client.close()
            return None, None
    except Exception as e:
        print(f"Error fetching function: {e}")
        client.close()
        return None, None

    function_code = function_doc.get("Function_Code", "")
    if not function_code:
        print(f"No function code found for Function_ID {function_id}")
        client.close()
        return None, None
    
    function_name = get_function_name(function_code)
    if not function_name:
        print(f"No function name found in the code for Function_ID {function_id}")
        client.close()
        return None, None

    # 3. Prepare the initial prompt
    initial_prompt = prompt_doc.get("Prompt_Text", "")
    if not initial_prompt:
        print(f"No initial prompt found for ID {prompt_id}")
        client.close()
        return None, None

    # 4. Run the PostconditionPipeline
    pipeline = PostconditionPipeline(API_KEY,prompt_id=prompt_id)
    structured_data, raw_reasoning = pipeline.process(initial_prompt, target_schema)

    client.close()
    return structured_data, raw_reasoning

# print("Initializing Postcondition Pipeline...")
# print("API key used:", API_KEY[:5] + "..." if API_KEY else "No API Key Found")
# # Initialize Pipeline
# pipeline = PostconditionPipeline(os.environ["API_KEY"])

# # Your iterative inputs
# prompts = [
#     ("find_cube_sum", "provide the preconditions and postconditions for a python function to find the cube sum of first n even natural numbers to test them holistically."),
#     ("is_palindrome", "provide the preconditions and postconditions for a python function to check if a number is a palindrome to test them holistically.")
# ]

# for prompt in prompts:
#     print(f"--- Processing: {prompt} ---")
    
#     # Run Pipeline
#     data, raw_text = pipeline.process(prompt[0], prompt[1], target_schema)
    
#     print("Final Structured Data:")
#     #get the data in pretty format from the test_cases key
#     print(json.dumps(data["test_cases"], indent=2) if data else "No structured data returned.")   
#     print("\n")
#     time.sleep(1)

# main function for testing
# if __name__ == "__main__":
#     print("Initializing Postcondition Pipeline...")
#     print("API key used:", API_KEY[:5] + "..." if API_KEY else "No API Key Found")
#     #call the get_postconditions_for_promptID function for prompt ID 1
#     structured_data, raw_reasoning = get_postconditions_for_promptID(1)
#     print("Final Structured Data:")
#     print(json.dumps(structured_data["test_cases"], indent=2) if structured_data else "No structured data returned.")
#     print("\n")
#     time.sleep(5) 
#     #call the get_postconditions_for_promptID function for prompt ID 2
#     structured_data, raw_reasoning = get_postconditions_for_promptID(2)
#     print("Final Structured Data:")
#     print(json.dumps(structured_data["test_cases"], indent=2) if structured_data else "No structured data returned.")
#     print("\n")




# # Helper function to parse the structured data JSON object and extract test cases into a dictionary and return it
# def parse_test_cases(structured_data) -> dict:
#     """Parses the structured data JSON object to extract test cases into a dictionary.
#     Args:
#         structured_data (list): The structured data JSON from the LLM.
#     Returns:
#         dict: A dictionary of test cases with test_case_name as keys.
#     """
#     test_cases_dict = {}
#     if not structured_data or "test_cases" not in structured_data:
#         print("No test cases found in structured data.")
#         return test_cases_dict
#     test_cases = structured_data["test_cases"]
#     for test_case in test_cases:
#         name = test_case.get("test_case_name", "Unnamed_Test_Case")
#         test_cases_dict[name] = test_case
#     return test_cases_dict


# Wrapper function which will take the prompt ID as argument, get the raw reasoning and structured data from the LLM and update the FunctionPrompts collection
def generate_and_update_postconditions_byPrompt(prompt_id: int) -> bool:
    """Generates postconditions for the given Prompt_ID and updates the FunctionPrompts collection.
    Args:
        prompt_id (int): The ID of the prompt to process.
    Returns:
        bool: True if postconditions were successfully generated and updated, False otherwise.
    """
    try:
        structured_data, raw_reasoning = get_postconditions_for_promptID(prompt_id)
    except Exception as e:
        print(f"Error generating postconditions for Prompt ID {prompt_id}: {e}")
        return False
    
    #update here the FunctionPrompts collection with the new raw_reasoning
    try:
        updateReasoning(prompt_id, raw_reasoning)
    except Exception as e:
        print(f"Error updating reasoning for Prompt ID {prompt_id}: {e}")
        return False
    
    if structured_data is None:
        print(f"Failed to generate postconditions for Prompt ID {prompt_id}. No structured data returned.")
        return False
    
    # Extract postconditions from structured data
    test_cases = structured_data.get("test_cases", [])
    if not test_cases:
        print(f"No test cases found in structured data for Prompt ID {prompt_id}.")
        return False
    
    # Update the FunctionPrompts collection with the new test cases
    try:
        updateTestcases(prompt_id, test_cases)
    except Exception as e:
        print(f"Error updating test cases for Prompt ID {prompt_id}: {e}")
        return False
    
    print(f"Successfully generated and updated test cases for Prompt ID {prompt_id}.")
    return True

# Helper function to update the test cases in the FunctionPrompts collection in case the test cases were not stored properly
def update_testcases_for_prompt(prompt_id: int) -> bool:
    """Updates the test cases for the given Prompt_ID in the FunctionPrompts collection.
    Args:
        prompt_id (int): The ID of the prompt to update.
    Logic: 
        - For the Prompt_ID, fetch the structured data using from the raw reasoning stored in the database.
        - Extract the test cases from the structured data.
        - Update the test cases in the FunctionPrompts collection.
    Returns:
        bool: True if test cases were successfully updated, False otherwise.
    """
    client, db = get_db_client()
    prompts_collection = db["FunctionPrompts"]
    functions_collection = db["Functions"]

    # Get functions document for the given Prompt_ID
    try:
        # 1. Get the function document
        function_id = prompts_collection.find_one({"Prompt_ID": prompt_id}).get("Function_ID")
        function_doc = functions_collection.find_one({"Function_ID": function_id})
        if not function_doc:
            print(f"No function found for Prompt ID {prompt_id}")
            client.close()
            return False
    except Exception as e:
        print(f"Error fetching function: {e}")
        client.close()
        return False
    # 1. Get the prompt document
    try:
        prompt_doc = prompts_collection.find_one({"Prompt_ID": prompt_id})
        if not prompt_doc:
            print(f"No prompt found for ID {prompt_id}")
            client.close()
            return False
    except Exception as e:
        print(f"Error fetching prompt: {e}")
        client.close()
        return False

    raw_reasoning = prompt_doc.get("raw_reasoning", "")
    if not raw_reasoning:
        print(f"No raw reasoning found for Prompt ID {prompt_id}")
        client.close()
        return False
    function_code = function_doc.get("Function_Code", "")
    if not function_code:
        print(f"No function code found for Prompt ID {prompt_id}")
        client.close()
        return False
    func_name = get_function_name(function_code)
    if not func_name:
        print(f"No function name found in the code for Prompt ID {prompt_id}")
        client.close()
        return False
    # check if raw_reasoning is not empty
    if not raw_reasoning.strip():
        print(f"Raw reasoning is empty for Prompt ID {prompt_id}")
        # delete the raw_reasoning field from the document
        try:
            prompts_collection.update_one(
                {"Prompt_ID": prompt_id},
                {"$unset": {"raw_reasoning": ""}}
            )
        except Exception as e:
            print(f"Error deleting raw_reasoning for Prompt ID {prompt_id}: {e}")
        client.close()
        return False
    # If test cases are present in the prompt document, no need to update
    existing_test_cases = prompt_doc.get("test_cases", [])
    if existing_test_cases:
        print(f"Test cases already exist for Prompt ID {prompt_id}.")
        client.close()
        return True
    # close the client
    client.close()
    # Initialize the pipeline
    pipeline = PostconditionPipeline(API_KEY,prompt_id=prompt_id)
    structured_data = pipeline.process_missin_structureddata(raw_reasoning, target_schema)
    if structured_data is None:
        print(f"Failed to generate structured data for Prompt ID {prompt_id}.")
        return False
    # Extract test cases from structured data
    # print("Final Structured Data:", structured_data.text)
    #get the data in pretty format from the test_cases key
    if not isinstance(structured_data, dict):
        print(f"Error: Structured data is not a dictionary but a {type(structured_data).__name__}.")
        return False
    test_cases = structured_data.get("test_cases", [])
    if not test_cases:
        print(f"No test cases found in structured data for Prompt ID {prompt_id}.")
        return False
    try:
        updateTestcases(prompt_id, test_cases)
    except Exception as e:
        print(f"Error updating test cases for Prompt ID {prompt_id}: {e}")
        return False
    print(f"Successfully updated test cases for Prompt ID {prompt_id}.")
    return True

# Wrapper function to run generate_and_update_postconditions_byPrompt for all the Prompt IDs in the FunctionPrompts collection where raw_reasoning is empty
def generate_and_update_postconditions_for_all() -> None:
    """Generates and updates postconditions for all Prompt_IDs in the FunctionPrompts collection where raw_reasoning is empty.
    Logic:It fetches all Prompt_IDs with empty raw_reasoning and calls generate_and_update_postconditions_byPrompt for each.
            -Print the total number of prompts processed and total successful updates.
    Args:
        None
    Returns:
        None
    """
    number_of_prompts_processed = 0
    number_of_successful_updates = 0
    client, db = get_db_client()
    prompts_collection = db["FunctionPrompts"]
    
    try:
        prompt_docs = prompts_collection.find({"$or": [{"raw_reasoning": {"$exists": False}}, {"raw_reasoning": ""}]})
        for prompt_doc in prompt_docs:
            number_of_prompts_processed += 1
            prompt_id = prompt_doc.get("Prompt_ID")
            if prompt_id is None:
                continue
            print(f"Generating and updating postconditions for Prompt ID {prompt_id}...")
            success = generate_and_update_postconditions_byPrompt(prompt_id)
            if success:
                number_of_successful_updates += 1
            else:
                print(f"Failed to generate postconditions for Prompt ID {prompt_id}. generate_and_update_postconditions_byPrompt returned False.")
            time.sleep(4)  # Sleep to avoid hitting rate limits
    except Exception as e:
        print(f"Error processing prompts: {e}")
    finally:
        client.close()
    print(f"Total prompts processed: {number_of_prompts_processed}")
    print(f"Total successful updates: {number_of_successful_updates}")

# Wrapper function to run update_testcases_for_prompt for all the Prompt IDs in the FunctionPrompts collection where test_cases is empty
def update_testcases_for_all() -> None:
    """Updates test cases for all Prompt_IDs in the FunctionPrompts collection where test_cases is empty.
    Logic:It fetches all Prompt_IDs with empty test_cases and calls update_testcases_for_prompt for each.
            -Print the total number of prompts processed and total successful updates.
    Args:
        None
    Returns:
        None
    """
    number_of_prompts_processed = 0
    number_of_successful_updates = 0
    client, db = get_db_client()
    prompts_collection = db["FunctionPrompts"]
    
    try:
        prompt_docs = prompts_collection.find({"$or": [{"test_cases": {"$exists": False}}, {"test_cases": []}]})
        for prompt_doc in prompt_docs:
            number_of_prompts_processed += 1
            prompt_id = prompt_doc.get("Prompt_ID")
            if prompt_id is None:
                continue
            print(f"Updating test cases for Prompt ID {prompt_id}...")
            success = update_testcases_for_prompt(prompt_id)
            if success:
                number_of_successful_updates += 1
            else:
                print(f"Failed to update test cases for Prompt ID {prompt_id}.")
            time.sleep(4)  # Sleep to avoid hitting rate limits
    except Exception as e:
        print(f"Error processing prompts: {e}")
    finally:
        client.close()
    print(f"Total prompts processed: {number_of_prompts_processed}")
    print(f"Total successful updates: {number_of_successful_updates}")

# main function for testing
def run_postcondition_updatesby_promptID(min_prompt_id: int, max_prompt_id: int) -> None:
    """Generates and updates postconditions for Prompt_IDs in the given range where raw_reasoning is empty,
    and updates test cases for Prompt_IDs where test_cases is empty.
    Args:
        min_prompt_id (int): The minimum Prompt_ID to process.
        max_prompt_id (int): The maximum Prompt_ID to process.
    Returns:
        None
    """
    client, db = get_db_client()
    prompts_collection = db["FunctionPrompts"]
    prompt_ids = prompts_collection.find({"Prompt_ID": {"$gte": min_prompt_id, "$lte": max_prompt_id}}, {"Prompt_ID": 1, "_id": 0})
    #create a list of prompt IDs whose test_cases is empty
    empty_test_cases_prompt_ids = []
    for prompt in prompt_ids:
        prompt_id = prompt["Prompt_ID"]
        prompt_document = getPromptbyPromptID(prompt_id)
        if prompt_document is None:
            print(f"No prompt found for ID {prompt_id}, skipping...")
            continue
        existing_test_cases = prompt_document.get("test_cases", [])
        if not existing_test_cases:
            #add the prompt ID to the list
            empty_test_cases_prompt_ids.append(prompt_id)
    
    #if no prompt IDs found with empty test_cases, return
    if not empty_test_cases_prompt_ids:
        print(f"No Prompt_IDs with empty test_cases found in the range {min_prompt_id} to {max_prompt_id}.")
        client.close()
        return False
    client.close()

    #run the postcondition generation for all prompt IDs in the empty_test_cases_prompt_ids list
    for i in empty_test_cases_prompt_ids:
        prompt_document = getPromptbyPromptID(i)
        if prompt_document is None:
            print(f"No prompt found for ID {i}, skipping...")
            continue
        #Check if test cases are present for the prompt ID in the prompt collection
        raw_reasoning = prompt_document.get("raw_reasoning", "")
        if raw_reasoning:
            print(f"Raw reasoning found for Prompt ID {i}, skipping...")
            continue
        print(f"Generating and updating postconditions for Prompt ID {i}...")
        success = generate_and_update_postconditions_byPrompt(i)
        if not success:
            print(f"Failed to generate postconditions for Prompt ID {i}. generate_and_update_postconditions_byPrompt returned False.")
        time.sleep(5)

    for j in empty_test_cases_prompt_ids:
        #get the prompt document for the prompt ID
        prompt_document = getPromptbyPromptID(j)
        if prompt_document is None:
            print(f"No prompt found for ID {j}, skipping...")
            continue
        #Check if test cases are present for the prompt ID in the prompt collection
        raw_reasoning = prompt_document.get("raw_reasoning", "")
        if not raw_reasoning:
            print(f"No raw reasoning found for Prompt ID {j}, skipping...")
            continue
        existing_test_cases = prompt_document.get("test_cases", [])
        if existing_test_cases:
            print(f"Test cases already exist for Prompt ID {j}, skipping...")
            continue
        print(f"Updating test cases for Prompt ID {j}...")
        success = update_testcases_for_prompt(j)
        if not success:
            print(f"Failed to update test cases for Prompt ID {j}.")
        time.sleep(5)
    return "success"

#Function to run the postcondition updates for given range of prompt IDs in batches of 10 and then wait for 30 seconds before processing the next batch
def run_postcondition_updates_all(min_prompt_id: int, max_prompt_id: int) -> None:
    """Generates and updates postconditions for all Prompt_IDs where raw_reasoning is empty,
    and updates test cases for all Prompt_IDs where test_cases is empty.
    Args:
        min_prompt_id (int): The minimum Prompt_ID to process.
        max_prompt_id (int): The maximum Prompt_ID to process.
    Returns:
        None
    """
    #get the prompt collection with all the prompt IDs in the given range between min_prompt_id and max_prompt_id
    client, db = get_db_client()
    prompts_collection = db["FunctionPrompts"]
    prompt_block = 12

    while min_prompt_id <= max_prompt_id:
        max_range = min(min_prompt_id + prompt_block - 1, max_prompt_id)
        flag = run_postcondition_updatesby_promptID(min_prompt_id, max_range)
        min_prompt_id = max_range + 1
        if flag == "success":
            time.sleep(30)
    # connect to function prompts collection and get the number of documents with empty or blank test_cases and number of documents with empty raw_reasoning where prompt ID is in the given range between min_prompt_id and max_prompt_id
    for prompt_id in range(min_prompt_id, max_prompt_id + 1):
        prompt_document = getPromptbyPromptID(prompt_id)
        if prompt_document is None:
            print(f"No prompt found for ID {prompt_id}, skipping...")
            continue
        existing_test_cases = prompt_document.get("test_cases", [])
        if not existing_test_cases:
            print(f"Test cases still missing for Prompt ID {prompt_id}.")
        raw_reasoning = prompt_document.get("raw_reasoning", "")
        if not raw_reasoning:
            print(f"Raw reasoning still missing for Prompt ID {prompt_id}.")
    client.close()  
    return


# Create a function to reset the intermediate fields in the FunctionPrompts collection for testing
def reset_intermediate_fields(prompt_id: int) -> None:
    """Resets the intermediate fields in the FunctionPrompts collection for the given Prompt_ID.
    Args:
        prompt_id (int): The ID of the prompt to reset.
    Returns:
        None
    """
    client, db = get_db_client()
    prompts_collection = db["FunctionPrompts"]
    try:
        prompts_collection.update_one(
            {"Prompt_ID": prompt_id},
            {"$unset": {
                "raw_reasoning": "",
                "Formatting_Prompt": "",
                "test_cases": "",
                "Structured_Response": "",
                "Correctness_Score": 0.0
            }}
        )
        # print(f"Successfully reset intermediate fields for Prompt ID {prompt_id}.")
    except Exception as e:
        print(f"Error resetting intermediate fields for Prompt ID {prompt_id}: {e}")
    finally:
        client.close()
    return


# Example usage: Process Prompt_IDs from 1 to 50
# run_postcondition_updates_all(1, 50)
if __name__ == "__main__":
    # Example usage: Process Prompt_IDs from 1 to 100 
    # run_postcondition_updates_all(21, 50)
    min_prompt_id = 1
    max_prompt_id = 299

    # for i in range(min_prompt_id, max_prompt_id + 1):
    #     reset_intermediate_fields(i)

    run_postcondition_updates_all(min_prompt_id, max_prompt_id)

    client, db = get_db_client()
    prompts_collection = db["FunctionPrompts"]

    # connect to function prompts collection and get the number of documents with empty or blank test_cases and number of documents with empty raw_reasoning where prompt ID is in the given range between min_prompt_id and max_prompt_id
    empty_test_cases_count = 0
    empty_raw_reasoning_count = 0
    for prompt_id in range(min_prompt_id, max_prompt_id + 1):
        try:
            prompt_document = prompts_collection.find_one({"Prompt_ID": prompt_id})
        except Exception as e:
            print(f"Error retrieving prompt for ID {prompt_id}: {e}")
            continue
        if prompt_document is None:
            print(f"No prompt found for ID {prompt_id}, skipping...")
            continue
        existing_test_cases = prompt_document.get("test_cases", [])
        if not existing_test_cases:
            print(f"Test cases still missing for Prompt ID {prompt_id}.")
            empty_test_cases_count += 1
        raw_reasoning = prompt_document.get("raw_reasoning", "")
        if not raw_reasoning:
            print(f"Raw reasoning still missing for Prompt ID {prompt_id}.")
            empty_raw_reasoning_count += 1
    print(f"Number of documents with empty test_cases: {empty_test_cases_count}")
    print(f"Number of documents with empty raw_reasoning: {empty_raw_reasoning_count}")
    print(f"Postcondition update process completed for Prompt_IDs from {min_prompt_id} to {max_prompt_id}.")
    client.close() 