"""This file contains functions to test the correctness of generated post-conditions against original function implementations using hypothesis testing."""

import json
import re
import ast
import os
import math
import shutil
from jsonschema import validate, ValidationError
from hypothesis import given, settings, strategies as st
from hypothesis import Phase
from hypothesis.errors import Flaky, NoSuchExample
from config import get_db_client
from Prompts import getPromptbyPromptID, getFunctionCodeAndNameFromPromptID, updateCorrectnessScore, updateTestcases
import inspect
from hypothesis import HealthCheck
from test_case_schema import test_case_schema
from hypothesis.errors import Flaky, NoSuchExample, DeadlineExceeded, Unsatisfiable
from func_timeout import func_timeout, FunctionTimedOut
import traceback
from hypothesis import assume
from typing import Any
import string
import collections, itertools, functools, heapq, statistics, string, random

def has_critical_crash(details: list) -> bool:
    """Checks if the details list contains any unrecoverable errors (crashes or timeouts)."""
    if not isinstance(details, list):
        return True # Treat global error (string) as critical

    CRITICAL_PHRASES = ("Implementation Crashed", "TIMEOUT", "LOAD_ERROR", "SETUP_ERROR", "ZeroDivisionError")
    
    for detail in details:
        reason = detail.get("reason", "")
        status = detail.get("status", "")
        
        # If status is FAIL AND the reason contains one of the critical words (crash/timeout)
        if status == 'FAIL' and any(phrase in reason for phrase in CRITICAL_PHRASES):
            return True
            
    return False

# ==========================================
# 1. SCHEMA DEFINITION
# ==========================================
SCHEMA_DEF = test_case_schema
accepted_errors = [
    "math domain error",
    "Infinite Loop Detected",
    "integer modulo by zero",
    "maximum recursion depth exceeded",
    "Max retries exhausted",
    "Assertion Failed:"
]
# ======================================================
# 1. STRATEGY FACTORY (The Builder)
# ======================================================
class ConstraintStrategyFactory:
    """
    Parses type strings and applies standard + custom constraints.
    Handles safe defaults, regex patterns, and recursion.
    """
    # 1. NEW HELPER: Generates random mixed data
# NEW HELPER: For general set/hashing tests where comparison is not the main goal.
    def _get_any_hashable_mix(self):
        """Returns a strategy that generates all basic, hashable, but incomparable types."""
        return st.one_of(
            st.integers(min_value=-50, max_value=50),
            st.floats(min_value=-50.0, max_value=50.0, allow_nan=False),
            st.booleans(),
            st.text(max_size=10, alphabet=string.printable), # Sequence 1
            st.tuples(st.integers(), st.booleans()),         # Sequence 2 (Hashable)
            st.frozensets(st.integers()),                    # Hashable Collection
            st.none()
        )

    # UPDATED: Rename existing helper for clarity (Used for sorting functions)
    # In correctnesstesting.py -> ConstraintStrategyFactory class

    def _get_mixed_strategy(self, allow_none=False):
        """
        Returns a stable, comparable numeric mix (numbers and bools).
        'allow_none' determines if None is included in the mix.
        """
        strategies = [
            st.integers(min_value=-100, max_value=100),
            st.floats(min_value=-100.0, max_value=100.0, allow_nan=False, allow_infinity=False),
            st.booleans()
        ]
        
        if allow_none:
            strategies.append(st.none())
            
        return st.one_of(*strategies)
    
    def get_strategy(self, type_str, constraints=None):
        if constraints is None: constraints = {}
        
        # Normalize bare types to safe defaults
        t_clean = type_str.strip().lower()

        # --- FIX START ---
        # Normalize aliases
        if t_clean == 'string': type_str = 'str'  # Fix for "string" -> "str"
        if t_clean == 'integer': type_str = 'int' # Fix for "integer" -> "int"
        # -----------------

        if t_clean == 'list': type_str = 'list[int]'
        if t_clean == 'tuple': type_str = 'tuple[int, int]'
        if t_clean == 'dict': type_str = 'dict[str, int]'
        if t_clean == 'set': type_str = 'set[int]'

        try:
            tree = ast.parse(type_str, mode='eval')
            strategy = self._parse_node(tree.body, constraints)
            
            # Global Modifiers
            sort_val = constraints.get("sorted")
            if sort_val:
                reverse_order = (sort_val == "descending")
                
                if 'tuple' in t_clean: 
                    strategy = strategy.map(lambda x: tuple(sorted(x, reverse=reverse_order)))
                elif 'list' in t_clean: 
                    strategy = strategy.map(lambda x: sorted(x, reverse=reverse_order))
                
            return strategy
        except Exception as e:
            print(f"    [!] Strategy Build Error ('{type_str}'): {e}")
            return st.integers() # Safe Fallback

    def _parse_node(self, node, constraints):
        # --- FIX: Handle bare container names (list, dict, tuple) recursively ---
        if isinstance(node, ast.Name):
             if node.id.lower() == 'list':
                 # Treat bare 'list' as 'list[int]'
                 return st.lists(st.integers())
             if node.id.lower() == 'dict':
                 return st.dictionaries(st.text(), st.integers())
             if node.id.lower() == 'tuple':
                 return st.lists(st.integers()).map(tuple)
             # Handle 'Any' type
             if node.id == 'Any': return self._get_any_hashable_mix()
        # -----------------------------------------------------------------------
        # # Handle "tuple" keyword used as a type (e.g. list[tuple])
        # if isinstance(node, ast.Name) and node.id.lower() == 'tuple':
        #      # Treat 'tuple' as 'tuple[int]' (variable length)
        #      # Generate a list of integers and convert to tuple
        #      return st.lists(st.integers()).map(tuple)
        
        # 1. Primitives (int, float, str)
        if isinstance(node, ast.Name):
            return self._get_primitive(node.id, constraints)
        
        # --- FIX START: Handle Constants (None) ---
        # "None" is parsed as a Constant in Python 3.8+
        elif isinstance(node, ast.Constant):
            if node.value is None:
                return st.none()
        # --- FIX END ---
        
        # 2. Containers (list[...], dict[...])
        elif isinstance(node, ast.Subscript):
            container = node.value.id.lower()
            inner = node.slice
            
            # --- NEW FIX: Handle Optional and Union ---
            if container == 'optional':
                # Optional[T] is Union[T, None]
                strategy = self._parse_node(inner, constraints)
                return st.one_of(st.none(), strategy)
            
            if container == 'union':
                # Handle Union[A, B]
                # inner is usually a Tuple of types
                if isinstance(inner, ast.Tuple):
                    strategies = [self._parse_node(elt, constraints) for elt in inner.elts]
                    return st.one_of(*strategies)
                else:
                    return self._parse_node(inner, constraints)
            # ------------------------------------------

            # Unwrap nested 'elements' constraint
            if 'elements' in constraints and isinstance(constraints['elements'], dict):
                child_constraints = constraints.copy()
                child_constraints.update(constraints['elements'])
            else:
                child_constraints = constraints

            # --- SIZE CALCULATION AND SAFETY CAP ---
            GLOBAL_MAX_CAP = 1500
            req_min = constraints.get("min_len", 0)
            req_max = constraints.get("max_len", 50) 
            safe_max = max(req_min, min(req_max, GLOBAL_MAX_CAP))
            uniq = constraints.get("unique", False)

            # --- FIX 2: MAX_LEN = 0 SAFETY CHECK ---
            if req_max == 0 and req_min == 0:
                # If constraints force length zero, return the constant empty container
                if container in ('list', 'set'):
                    return st.just([])
                elif container in ('tuple'):
                    return st.just(())
                elif container in ('dict'):
                    return st.just({})
            # ------------------------------------

            # --- DETERMINE BASE INNER STRATEGY ---
            elem_type = str(constraints.get('element_types', '')).lower()
            
            # Check if None is explicitly allowed by other constraints
            should_allow_none = (
                constraints.get('allow_none', False) or 
                'none' in elem_type or 
                'null' in elem_type or
                container == 'optional' # logic from the wrapper handles this, but good for safety
            )

            # 1. Check for Hashable Mix (Highest Priority)
            if constraints.get('is_hashable_mix', False):
                base_strategy = self._get_any_hashable_mix() # <--- CALL HERE
            
            # 2. Check for Numeric/Comparison Mix (Existing 'is_mixed' flag)
            elif constraints.get('is_mixed'):
                base_strategy = self._get_mixed_strategy(allow_none=should_allow_none)
            elif 'str' in elem_type:
                base_strategy = self._get_primitive('str', child_constraints)
            elif 'int' in elem_type:
                base_strategy = self._get_primitive('int', child_constraints)
            # ... (add other explicit types like 'float', 'bool', etc. here if needed)
            else:
                # Fallback to AST parsing
                base_strategy = self._parse_node(inner, child_constraints)

            # --- FIX 1: FORCE NONE GENERATION ---
            # If 'none' or 'null' is requested in the element types, wrap the strategy in st.one_of(None)
            if 'none' in elem_type or 'null' in elem_type or constraints.get('allow_none', False):
                final_inner_strategy = st.one_of(st.none(), base_strategy)
            else:
                final_inner_strategy = base_strategy
            # ------------------------------------


            # --- CONTAINER MAPPING ---
            if container == 'list':
                return st.lists(final_inner_strategy, min_size=req_min, max_size=safe_max, unique=uniq)

            elif container == 'tuple':
                # Fixed size tuple handling goes here if inner is ast.Tuple
                if isinstance(inner, ast.Tuple):
                    strategies = [self._parse_node(elt, child_constraints) for elt in inner.elts]
                    return st.tuples(*strategies)
                else:
                    # Variable size tuple
                    return st.lists(final_inner_strategy, min_size=req_min, max_size=safe_max, unique=uniq).map(tuple)

            elif container == 'set':
                return st.sets(final_inner_strategy, min_size=req_min, max_size=safe_max)
            
            elif container == 'dict':
                # Requires explicit key/value strategy handling
                if isinstance(inner, ast.Tuple):
                    k_node, v_node = inner.elts[0], inner.elts[1]
                    val_strategy = final_inner_strategy # Use the final strategy for values
                    # FIX: Separate constraints. Keys usually shouldn't inherit 'min_val' meant for values.
                    # Pass empty dict for keys unless you have specific key logic (complex to implement generically)
                    # or filter child_constraints to only pass safe keys.
                    key_constraints = {} 
                    
                    return st.dictionaries(keys=self._parse_node(k_node, key_constraints), 
                                           values=val_strategy,
                                           min_size=req_min, max_size=safe_max)
                return st.dictionaries(keys=st.text(), values=final_inner_strategy, min_size=req_min, max_size=safe_max)
            
        return st.integers() # Final fallback

    def _parse_val(self, val):
        """Parses JSON values (including special strings) to Python numbers."""
        if isinstance(val, (int, float)): return val
        if isinstance(val, str):
            val = val.lower()
            if 'inf' in val: return float('-inf') if '-' in val else float('inf')
            if 'nan' in val: return float('nan')
        return None

    def _get_primitive(self, type_name, c):
        t = type_name.lower()
        
        min_v = self._parse_val(c.get("min_val"))
        max_v = self._parse_val(c.get("max_val"))

        if t == 'int':
            # FIX 1: Tighten the default domain to force collisions
            DEFAULT_COLLISION_MAX = 100
            # 2. Heuristic for Overlap (Check if it will cause a crash)
            req_min_len = c.get('min_len', 0)
            
            # --- FIX: Only force tiny pool if bounds are NOT explicit ---
            # This fixes pc_2 where explicit bounds (51-100) were ignored
            has_explicit_bounds = (min_v is not None or max_v is not None)
            req_min_len = c.get('min_len', 0)
            is_low_prob_overlap = (req_min_len > 1 and c.get('unique', False))

            if is_low_prob_overlap and not has_explicit_bounds:
                 pool_size = max(6, c.get('min_len', 0))
                 return st.integers(min_value=0, max_value=pool_size)
            # ------------------------------------------------------------

            # # If minimum required length is large AND unique is required, we CANNOT use the tiny pool.
            # if c.get('unique', False) and req_min_len > 6:
            #      # If the user requires 10 unique items, we must provide a large pool.
            #      # Skip the tiny pool and rely on the robust final_min/max logic.
            #      is_low_prob_overlap = False 
            # else:
            #      is_low_prob_overlap = c.get('min_len', 0) > 1 and c.get('unique', False)

            # if is_low_prob_overlap:
            #      # ONLY APPLY TINY POOL IF IT WON'T VIOLATE MIN_LEN > 6
            #      return st.integers(min_value=0, max_value=6) # 7 elements in the pool
            # FIX: Lower the default domain range drastically for stability
            # We cap the default min/max at a small number (e.g., 50) 
            # unless the LLM specified a larger bound.
            # 2. Determine bounds (prioritizing explicit constraints over default)
            req_min = min_v if min_v is not None else -DEFAULT_COLLISION_MAX
            req_max = max_v if max_v is not None else DEFAULT_COLLISION_MAX

            # --- CODE INTERVENTION: Ensure Domain satisfies Uniqueness ---
            req_len = c.get('min_len', 0)
            if c.get('unique', False) and req_len > 0:
                current_range = (req_max - req_min) + 1
                if current_range < req_len:
                    # Automatically widen the max value to allow satisfying uniqueness
                    req_max = req_min + req_len + 5 
            # -----------------------------------------------------------

            # 3. CRITICAL FIX: Handle Logical Inconsistency (max < min)
            if req_min > req_max:
                req_max = req_min
            
            # 4. Sanitize and build base strategy (using 32-bit limit as final escape)
            safe_min = int(req_min) if math.isfinite(req_min) else -2000000000 
            safe_max = int(req_max) if math.isfinite(req_max) else 2000000000
            strategy = st.integers(min_value=safe_min, max_value=safe_max)
           
            # --- NEW FIX: Handle 'step' constraint ---
            step = c.get("step")
            if step and isinstance(step, (int, float)) and step > 1:
                step = int(step)
                # Filter numbers so they match the 'step' stride starting from safe_min
                strategy = strategy.filter(lambda x: (x - safe_min) % step == 0)
            # -----------------------------------------
            
            if c.get('is_none_check', False) or c.get('allow_none', False) or 'none' in c.get('element_types', ''):
                 # This strategy is designed to frequently return None or a small int.
                 return st.one_of(st.none(), strategy)

            if c.get('perfect_square'):
                strategy = strategy.filter(lambda x: x >= 0 and math.isqrt(x)**2 == x)
            if c.get('even'): strategy = strategy.filter(lambda x: x % 2 == 0)
            if c.get('odd'): strategy = strategy.filter(lambda x: x % 2 != 0)
            return strategy

        elif t == 'float':
            # Assign and check bounds (must also check max < min)
            final_min = min_v if min_v is not None else -1e6
            final_max = max_v if max_v is not None else 1e6
            
            if final_min > final_max: # Apply consistency check to floats too
                final_max = final_min
            
            # ... (Special float handling remains here) ...
            if (min_v is not None and math.isnan(min_v)) or (max_v is not None and math.isnan(max_v)):
                return st.just(float('nan'))
            if final_min == float('inf') or final_max == float('inf'): return st.just(float('inf'))
            if final_min == float('-inf') or final_max == float('-inf'): return st.just(float('-inf'))

            return st.floats(min_value=final_min, max_value=final_max, allow_nan=False, allow_infinity=False)

        elif t == 'str':
            # 1. Regex Pattern (Highest Priority)
            # If a pattern is provided, we let the regex define the allowed characters
            pattern = c.get('pattern')
            if pattern:
                # --- CODE INTERVENTION: Sanitize Regex ---
                # Remove unsupported \p{...} and replace with generic word char \w
                # This prevents the "bad escape \p" crash.
                if "\\p" in pattern:
                    # Replace \p{L} or \p{...} with \w (best effort fallback)
                    pattern = re.sub(r'\\p\{[^\}]+\}', r'\\w', pattern)
                
                try: 
                    return st.from_regex(pattern, fullmatch=True)
                except Exception: 
                    # If regex is still invalid, fall back to standard text strategy 
                    # instead of crashing the whole test runner.
                    print(f"    [WARN] Invalid Regex '{pattern}' ignored. Using default text.")
                    return st.text(alphabet=string.ascii_letters + string.digits, min_size=1, max_size=20)
            
            # 2. Alphabet Restriction (max_codepoint)
            # --- OPTIMIZATION ---
            max_cp = c.get("max_codepoint")
            if max_cp == 255:
                # Use a pre-defined simple alphabet for ASCII (More stable than max_codepoint)
                alphabet_strategy = string.printable
            elif max_cp is not None:
                alphabet_strategy = st.characters(max_codepoint=max_cp)
            else:
                alphabet_strategy = st.characters()
            # --------------------

            # 3. Length Constraints
            min_l = c.get("min_len", 0)
            max_l = c.get("max_len", 50)
            
            return st.text(alphabet=alphabet_strategy, min_size=min_l, max_size=max_l)
            
        elif t == 'bool':
            return st.booleans()
        
        # --- FIX START: Handle explicit None type ---
        elif t == 'none' or t == 'null':
            return st.none()
        # --- FIX END ---

        return st.integers()

# ======================================================
# 3. VALIDATOR ENGINE (The Controller)
# ======================================================
class ValidatorEngine:
    def __init__(self):
        self.factory = ConstraintStrategyFactory()

    def _ensure_parsed(self, data):
        if isinstance(data, dict): return data
        if isinstance(data, str):
            try: return json.loads(data)
            except: return None
        return None
    
    def _reduce_constraints_for_retry(self, case):
        """
        Aggressively reduces container size limits (max_len) to combat Unsatisfiable errors.
        This forces Hypothesis to find simpler, smaller inputs.
        """
        critical_reduction = False
        constraints = case.get('input_constraints', {})
        
        # Helper function to recursively lower limits
        def reduce_dict_limits(d):
            nonlocal critical_reduction
            
            if isinstance(d, dict):
                # 1. Lower max_len/max_size by 50%
                for key in ['max_len', 'max_size', 'max_val']:
                    if key in d and isinstance(d[key], int) and d[key] > 2:
                        d[key] = max(2, d[key] // 2)
                        critical_reduction = True
                # --- CODE INTERVENTION: Relax Strict Min/Unique ---
                # 2. Relax min_len if it's causing pressure
                if 'min_len' in d and d['min_len'] > 0:
                    d['min_len'] = 0  # Allow empty/small inputs
                    critical_reduction = True
                
                # 3. Disable Uniqueness if it's likely the cause
                if 'unique' in d and d['unique'] is True:
                    d['unique'] = False
                    critical_reduction = True
                # --------------------------------------------------    
                # 2. Recurse into nested structures (elements, arg_name)
                for key, value in d.items():
                    if key in ('elements', 'items', 'inner') or key not in ('min_val', 'max_val', 'min_len'):
                         reduce_dict_limits(value)
            
            # 3. Recursion on lists (for safety/nested arrays)
            elif isinstance(d, list):
                for item in d:
                    reduce_dict_limits(item)
                
        # Start the reduction process on the main constraints dict
        reduce_dict_limits(constraints)

        if critical_reduction:
            print(f"    [RETRY] Reduced constraints by 50%. Max_len limits are now smaller.")
        return critical_reduction
    
    def _sanitize_execution_stmt(self, stmt):
        """
        Robustly cleans execution statements.
        Handles semicolons, one-line try/except, and indentation rebuilding.
        """
        stmt = stmt.strip()
        
        # 1. Global Semicolon Fix: Treat ';' as a newline
        if ";" in stmt:
            stmt = stmt.replace(";", "\n")
            
        # 2. Ensure 'except' / 'finally' starts on a new line
        if "try:" in stmt and ("except" in stmt or "finally" in stmt):
            import re
            # Add newline before 'except' and 'finally' if not present
            stmt = re.sub(r'([^\n])\s+(except)', r'\1\n\2', stmt)
            stmt = re.sub(r'([^\n])\s+(finally)', r'\1\n\2', stmt)

        # 3. Rebuild Indentation Line-by-Line
        lines = [L.strip() for L in stmt.split('\n') if L.strip()]
        fixed_lines = []
        indent_level = 0
        
        for line in lines:
            # A. Dedent for keywords that close a block
            if line.startswith(("except", "finally", "else", "elif")):
                indent_level = max(0, indent_level - 1)
            
            # B. Handle "Header: Body" on one line (e.g. "try: result=1")
            # We force split them to ensure consistent indentation structure
            if ":" in line:
                import re
                # Check if it starts with a block keyword
                if re.match(r'^(try|if|elif|else|for|while|except|finally|def|class)\b', line):
                    parts = line.split(":", 1)
                    header = parts[0].strip() + ":"
                    body = parts[1].strip()
                    
                    # Append Header
                    fixed_lines.append("    " * indent_level + header)
                    
                    # If there is body code, indent it on next line
                    if body:
                        indent_level += 1
                        fixed_lines.append("    " * indent_level + body)
                        # Note: We generally stay indented after this
                    else:
                        # No body, just prep indent for next loop iteration
                        indent_level += 1
                    
                    continue # Skip the standard append below

            # C. Standard Append
            fixed_lines.append("    " * indent_level + line)
            
            # Increase indent if this line ended a block starter (e.g. "try:")
            if line.endswith(":"):
                indent_level += 1

        return "\n".join(fixed_lines)

    def _fix_regex_patterns(self, obj):
        r"""
        Recursively searches for 'pattern' keys and fixes double-escaped backslashes.
        Converts LLM's "\\\\s" -> "\\s" (Python's \s).
        """
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == 'pattern' and isinstance(v, str):
                    if "\\\\" in v: obj[k] = v.replace('\\\\', '\\')
                else:
                    self._fix_regex_patterns(v)
        elif isinstance(obj, list):
            for item in obj:
                self._fix_regex_patterns(item)

    def _fix_malformed_constraints(self, json_data):
        """
        Master Fixer: Auto-corrects null/flat constraints, regex patterns, 
        merges dot/suffix notation, enforces ASCII safety, and fixes execution statements.
        """
        if 'test_cases' not in json_data: return json_data
        
        for i, case in enumerate(json_data['test_cases']):
            # -------------------------------------------------------
            # 1. Fix IDs (Ensure "pc_N" format)
            # -------------------------------------------------------
            if 'id' not in case: 
                case['id'] = f"pc_{i+1}"
            elif isinstance(case['id'], (int, str)) and str(case['id']).isdigit(): 
                case['id'] = f"pc_{case['id']}"

            # --- FIX: Ensure 'assumptions' field is present and a list ---
            assumptions = case.get('assumptions')
            if assumptions is None:
                case['assumptions'] = []
            elif not isinstance(assumptions, list):
                # If LLM wrote "assumptions": "n <= len(arr)" (a string), convert it to a list
                case['assumptions'] = [str(assumptions)]
            # -----------------------------------------------------------
            # -------------------------------------------------------
            # 2. Fix Null/None Constraints
            # -------------------------------------------------------
            c = case.get('input_constraints', {})
            if c is None: 
                case['input_constraints'] = {}
                c = {} # Local reference
            
            if isinstance(c, dict):
                for k, v in c.items():
                    if v is None: c[k] = {}

            # -------------------------------------------------------
            # 3. Fix Structure (Suffixes & Dot Notation)
            #    Matches: arg_elements, arg.elements, arg_element_constraints
            # -------------------------------------------------------
            if isinstance(c, dict):
                # Iterate over a copy of keys because we modify dictionary size
                for key in list(c.keys()):
                    parent = None
                    
                    # Case A: Suffixes (_elements, _items)
                    if key.endswith("_elements") or key.endswith("_items") or key.endswith("_element_constraints"):
                        # Extract "arg" from "arg_elements"
                        if "_element_constraints" in key:
                            parent = key.rsplit('_element_constraints', 1)[0]
                        else:
                            parent = key.rsplit('_', 1)[0]
                            
                    # Case B: Dot Notation (arg.elements)
                    elif "." in key:
                        parts = key.split(".", 1)
                        if parts[1] == "elements":
                            parent = parts[0]

                    # Apply Merge if parent found
                    if parent:
                        if parent not in c: c[parent] = {}
                        if "elements" not in c[parent]: c[parent]["elements"] = {}
                        
                        # Merge constraints into the parent's 'elements' dict
                        c[parent]["elements"].update(c[key])
                        del c[key]
                        # print(f"    [AUTO-FIX] Merged '{key}' into '{parent}' elements.")

            # -------------------------------------------------------
            # 4. Fix Flat Constraints (Root level min_val etc.)
            # -------------------------------------------------------
            t = case.get('input_types', {})
            flat_keys = {'min_val', 'max_val', 'min_len', 'max_len', 'sorted', 'unique', 'pattern', 'max_codepoint', 'is_mixed'}
            
            # If constraints contains keys usually meant for args, AND there is only 1 arg
            if any(k in c for k in flat_keys) and len(t) == 1:
                arg = list(t.keys())[0]
                # Wrap the entire constraint object under the argument name
                case['input_constraints'] = {arg: c}
                # Refresh reference 'c' for subsequent steps
                c = case['input_constraints']

            # -------------------------------------------------------
            # 5. Fix Regex Patterns (Double Escaping)
            # -------------------------------------------------------
            self._fix_regex_patterns(c)

            # -------------------------------------------------------
            # 6. ASCII Enforcement (Prevent Unicode Crashes)
            # -------------------------------------------------------
            if isinstance(c, dict) and isinstance(t, dict):
                for arg, type_str in t.items():
                    if 'str' in str(type_str).lower():
                        # Ensure constraint dict exists for this arg
                        if arg not in c: c[arg] = {}

                        # A. Check Root Level
                        # If no specific unicode range/pattern requested, force ASCII
                        if 'max_codepoint' not in c[arg] and 'pattern' not in c[arg]:
                             c[arg]['max_codepoint'] = 127 
                        
                        # B. Check Nested Level (for list[str])
                        if 'elements' in c[arg]:
                             if 'max_codepoint' not in c[arg]['elements'] and 'pattern' not in c[arg]['elements']:
                                  c[arg]['elements']['max_codepoint'] = 127

            # -------------------------------------------------------
            # 7. Fix Execution Statement (Missing 'result =')
            # -------------------------------------------------------
            stmt = case.get('execution_statement', '').strip()
            if stmt:
                # Use regex to check if 'result =' is missing (ignoring whitespace)
                if not re.search(r'(^|[\s;])result\s*=', stmt):
                    
                    # Scenario A: Semicolon separated (setup; call)
                    if ";" in stmt:
                        parts = stmt.split(";")
                        last_part = parts[-1].strip()
                        # If last part is a call "func()" without assignment
                        if "(" in last_part and "=" not in last_part:
                            parts[-1] = f" result = {last_part}"
                            case['execution_statement'] = ";".join(parts)
                            
                    # Scenario B: Single statement call "func()"
                    elif "(" in stmt and "=" not in stmt:
                        # Don't break try/except blocks
                        if not stmt.startswith("try:"):
                            case['execution_statement'] = f"result = {stmt}"
                
        return json_data

    def run_audit_from_source(self, source, function_name, raw_data):
        """Entry Point."""
        # 1. Parse & Fix JSON
        json_data = self._ensure_parsed(raw_data)
        if not json_data: 
            # FIX: Return details as a LIST of one object
            return {
                "metric": 0.0, 
                "status": "JSON_ERROR", 
                "details": [{"id": "GLOBAL", "status": "FAIL", "reason": "Invalid JSON Input"}]
            }
        
        json_data = self._fix_malformed_constraints(json_data)

        # 2. Validate Schema
        try:
            from test_case_schema import test_case_schema
            validate(instance=json_data, schema=test_case_schema)
        except ValidationError as e:
            # FIX: Return details as a LIST
            return {
                "metric": 0.0, 
                "status": "SCHEMA_ERROR", 
                "details": [{"id": "GLOBAL", "status": "FAIL", "reason": f"Schema Validation Failed: {e.message}"}]
            }

        # 3. Load Code
        try:
            func_impl, global_scope = self._load_dynamic_function(source, function_name)
        except Exception as e:
            # FIX: Return details as a LIST
            return {
                "metric": 0.0, 
                "status": "LOAD_ERROR", 
                "details": [{"id": "GLOBAL", "status": "FAIL", "reason": f"Code Loading Failed: {str(e)}"}]
            }
            
        # 4. Run Tests
        return self._execute_audit_logic(func_impl, json_data, global_scope)

    def _load_dynamic_function(self, source, function_name):
        code_content = ""
        if os.path.exists(source) and os.path.isfile(source):
            with open(source, 'r') as f: code_content = f.read()
        else:
            code_content = source

        def flatten_list_helper(lst):
            for item in lst:
                if isinstance(item, list):
                    yield from flatten_list_helper(item)
                else:
                    yield item
        def is_prime(n):
            if n < 2: return False
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True

        global_scope = {
            'math': math, 
            're': re,
            'collections': collections,
            'itertools': itertools,
            'functools': functools,
            'heapq': heapq,
            'statistics': statistics,
            'string': string,
            'flatten': lambda lst: list(flatten_list_helper(lst)), 
            'is_prime': is_prime
        } # Add standard libs here
        try:
            exec(code_content, global_scope)
        except Exception as e:
            raise RuntimeError(f"Compilation Error: {e}")
        
        if function_name not in global_scope:
            raise ValueError(f"Function '{function_name}' not found.")
            
        return global_scope[function_name], global_scope
    
    # global_scope['Any'] = (int, float, str, bool, type(None), tuple, list)
    def _execute_audit_logic(self, function_impl, json_data, global_scope):
        """
        Executes the full Hypothesis audit for a single function.
        Incorporates dynamic strategy building, assumption filtering, and timeout protection.
        """
        results_log = []
        passed_cases = 0
        total_cases = len(json_data['test_cases'])
        global_scope['Any'] = (int, float, str, bool, type(None), tuple, list)

        # SAFETY NET: Get Actual Args
        try:
            sig = inspect.signature(function_impl)
            actual_args = {k for k in sig.parameters.keys()}
        except:
            actual_args = set()

        for case in json_data['test_cases']:
            case_id = case.get('id', 'unknown')
            execution_stmt = case.get('execution_statement', '')
            
            # Safety Net: Arg Mismatch Check
            json_args = set(case.get('input_types', {}).keys())
            if actual_args and json_args != actual_args:
                results_log.append({"id": case_id, "status": "SKIP", "reason": "Arg Mismatch"})
                continue

            # --- DYNAMIC RETRY LOOP START for Unsatisfiable Errors ---
            RETRY_LIMIT = 8
            attempt = 0
            case_passed = False
            failure_reason = None
            
            while attempt < RETRY_LIMIT:
                try:
                    # 1. BUILD STRATEGIES (Must be inside loop to pick up modified constraints)
                    strategies = {}
                    constraints = case.get('input_constraints', {})
                    for arg, type_str in case['input_types'].items():
                        strategies[arg] = self.factory.get_strategy(type_str, constraints.get(arg, {}))

                    # 2. Define Test Runner
                    @settings(
                        max_examples=200, 
                        deadline=1000, 
                        database=None, # Prevents cross-run state corruption
                        phases=[Phase.explicit, Phase.reuse, Phase.generate], # Disables shrinking
                        suppress_health_check=[HealthCheck.data_too_large, HealthCheck.filter_too_much, 
                                            HealthCheck.too_slow, HealthCheck.large_base_example]
                    )
                    @given(**strategies)
                    def test_runner(**kwargs):
                        # Prepare Scope (Includes inputs, helpers, and 'assume' for execution)
                        eval_scope = global_scope.copy()
                        eval_scope.update(kwargs)
                        eval_scope['assume'] = assume
                        eval_scope['Any'] = global_scope['Any'] # Assuming ANY_TYPE_UNION is defined globally
                        
                        # A. Run Assumptions (Filter dependent inputs)
                        assumptions = case.get('assumptions', [])
                        if isinstance(assumptions, list):
                            for cond in assumptions:
                                try:
                                    # We check the condition directly via eval. 
                                    assumption_holds = eval(cond, eval_scope)
                                    if not assumption_holds:
                                        assume(False) # Discard input
                                except Exception:
                                    # If assumption logic fails (e.g. NameError in 'len(arr)'), discard
                                    assume(False) 

                        # B. Execution Worker (Wrapped for Timeout)
                        def run_exec():
                            clean_stmt = self._sanitize_execution_stmt(execution_stmt)
                            exec(clean_stmt, eval_scope)

                        # C. Run with Timeout Protection (func_timeout)
                        try:
                            func_timeout(1.0, run_exec) 
                        except FunctionTimedOut:
                            raise AssertionError("TIMEOUT: Function execution took too long.")
                        except Exception as e:
                            raise AssertionError(f"Implementation Crashed: {e}")
                        
                        if 'result' not in eval_scope:
                            raise AssertionError("Execution did not assign 'result'")

                        # D. Assertion Check (for all postconditions)
                        for prop in case['postconditions']:
                            assertion_code = prop['assertion']
                            # --- NEW FIX: STRIP ASSERT KEYWORD ---
                            assertion_code = assertion_code.strip()
                            if assertion_code.startswith("assert "):
                                assertion_code = assertion_code[7:].strip()
                            # ------------------------------------
                            if " implies " in assertion_code: 
                                parts = assertion_code.split(" implies ")
                                assertion_code = f"not ({parts[0]}) or ({parts[1]})"

                            check = eval(assertion_code, eval_scope)
                            assert check, f"Assertion Failed: {assertion_code}"

                    # 3. Execute the defined test runner
                    test_runner()
                    
                    # If execution reaches here, all postconditions passed for 200 examples
                    case_passed = True
                    break 

                except Unsatisfiable as e:
                    # 4. Handle Unsatisfiable: Reduce constraints and retry
                    if attempt == RETRY_LIMIT - 1:
                        case_passed = False
                        failure_reason = f"Unsatisfiable: Max retries exhausted. (Reason: {e})"
                        break
                    
                    # Assume _reduce_constraints_for_retry is defined and modifies 'case' in place
                    self._reduce_constraints_for_retry(case) 
                    print(f"    [INFO] Unsatisfiable detected. Reducing constraints (Attempt {attempt+1}/{RETRY_LIMIT}).")
                    attempt += 1
                    continue 

                except (AssertionError, Flaky, NoSuchExample, DeadlineExceeded) as e:
                    # 5. Handle Assertion Failure or Timeout
                    case_passed = False
                    failure_reason = str(e)
                    break 
                
                except Exception as e:
                    # Catch any unexpected setup crash outside the test runner loop
                    case_passed = False
                    failure_reason = f"Unexpected Setup Error: {str(e)}"
                    break


            # 6. Final Logging
            status = "PASS" if case_passed and failure_reason is None else "FAIL"
            if case_passed: passed_cases += 1
            results_log.append({"id": case_id, "status": status, "reason": failure_reason})

        # 7. Calculate Metric
        metric = (passed_cases / total_cases) * 100 if total_cases > 0 else 0
        return {"metric": metric, "details": results_log}
    

# ==========================================
# function to run the engine for a prompt ID
# ==========================================
def run_validator_engine_for_prompt(prompt_id: int) -> bool:
    """
    Runs the Validator Engine for a given prompt_id.
    Arguments:
    prompt_id (int): The ID of the prompt to audit.
    Returns:
    bool: True if the audit was run successfully, False otherwise.
    """
    # --- FIX: CLEAR HYPOTHESIS CACHE ---
    print(f"Clearing Hypothesis cache for Prompt ID {prompt_id}...")
    if os.path.exists(".hypothesis"):
        try: shutil.rmtree(".hypothesis")
        except: pass
        # -----------------------------------
    # 1. Get the prompt document
    try:
        prompt_doc = getPromptbyPromptID(prompt_id)
    except Exception as e:
        print(f"Audit Error fetching prompt for ID {prompt_id}: {e}")
        return False
    if not prompt_doc:
        print(f"Audit Error: No prompt found for ID {prompt_id}")
        return False
    try:
        #get the function name and code from the prompt ID
        function_doc = getFunctionCodeAndNameFromPromptID(prompt_id)
    except Exception as e:
        print(f"Audit Error fetching function name and code for prompt ID {prompt_id}: {e}")
        return False


    if not function_doc[0] or not function_doc[1]:
        print(f"Audit Error: incorrect function definitions for the function from Prompt ID {prompt_id}")
        return False

    function_code = function_doc[1]
    function_name = function_doc[0]
    report_header = {"prompt_id": prompt_id, "function_name": function_name}
    print(f"Function name: {function_name}")
    # print(f"Function code: {function_code}")
    # print("end of function code")
    # Prepend imports to the function code for the AST parser
    full_code_context = function_code
    post_conditions = prompt_doc.get("test_cases", [])
    if not post_conditions:
        report = {"status": "ERROR", "reason": "No post-conditions found."}
        report = {**report_header, **report}
        # print(f"Error : Skipping audit for Prompt ID {prompt_id}: No post-conditions found.")
        return report
    # 3. Prepare LLM JSON data
    llm_json = {
        "test_cases": []
    }
    
    abc = enumerate(post_conditions)
    # print the enumerated post conditions in a readable JSON format
    # print(f"enumerated post conditions: {list(abc)}")


    for idx, pc in enumerate(post_conditions):
        # print(f"Post-condition {idx+1}: {pc}")
        test_case = {
            "id": f"pc_{idx+1}",
            "description": pc.get("description", f"Post-condition {idx+1}"),
            "execution_statement": pc.get("execution_statement", {"result = " + function_name + "(**inputs)"}),
            "input_types": pc.get("input_types", {}),
            "input_constraints": pc.get("input_constraints", {}),
            "postconditions": pc.get("postconditions", []),
            "assumptions": pc.get("assumptions", [])
        }
        llm_json["test_cases"].append(test_case)
    
    #print the llm_json data in readable format
    # print("LLM JSON Data:")
    # print(json.dumps(llm_json, indent=4))
    # 4. Run Engine
    engine = ValidatorEngine()
    #add heeder to the report with prompt ID
    report_header = {"prompt_id": prompt_id, "function_name": function_name}
    try:
        report = engine.run_audit_from_source(full_code_context, function_name=function_name, raw_data=llm_json)
    except Exception as e:
        # --- ADD THIS DEBUG BLOCK ---
        print(f"\n[!!!] CRITICAL ERROR for Prompt ID {prompt_id}:")
        traceback.print_exc()  # <--- This prints the line number and file causing the crash
        # -----------------------------
        #add status to the report
        return {**report_header, "status": "ERROR", "reason": str(e)}
    
    # --- ADD SAFETY CHECK HERE ---
    details = report.get("details", [])
    if not isinstance(details, list):
        print(f"Warning: 'details' is not a list. It is: {type(details)}")
        details = [] # Fallback to empty list to prevent crash
    # -----------------------------
    #get the test metric from the report

    # 1. Check for Crashes and Logic Errors
    critical_crash_found = has_critical_crash(report.get("details", []))
    
    test_metric = report.get("metric", 0.0)/100.0
    #update the correctness score in the database
    try:
        print(f"Updating correctness score for Prompt ID {prompt_id} to {test_metric:.4f}")
        update_success = updateCorrectnessScore(prompt_id, test_metric)
        # Set final status based on audit success
        if not critical_crash_found:
            report["status"] = "SUCCESS" # All tests ran without crashing
        else:
            report["status"] = "FAILURE" # Crashed found (critical bug)
        
    except Exception as e:
        report["status"] = "ERROR"
        report["warning"] = f"Error updating correctness score: {e}"
        update_success = False

    
    
    report = {**report_header, **report}
    
    #create analsysis logs for the test cases with status as fail and reason not as None and reason does not have reasons in accepted_errors
    analysis_logs = []
    for detail in details:
        if detail.get("status") == "FAIL" and detail.get("reason") and not any(err in detail.get("reason") for err in accepted_errors):
            analysis_logs.append({
                "test_case_id": detail.get("id"),
                "reason": detail.get("reason")
            })
    # Check if the analysis_logs is not empty            
    if analysis_logs:

        #dump the analysis logs in readable format in a error file
        error_dir = os.getcwd() + "/errors/errors_PBT"
        if not os.path.exists(error_dir):
            os.makedirs(error_dir)
        error_file_path = error_dir + f"/analysis_logs_prompt_{prompt_id}.log"
        with open(error_file_path , "w") as f:
            f.write(f"\nFunction name: {function_name}")
            f.write(f"\nFunction code: {function_code}")
            f.write("\nend of function code")
            f.write("\n\nAnalysis Logs:\n")
            for log in analysis_logs:
                f.write(f"Test Case ID: {log.get('test_case_id')}\n")
                f.write(f"Reason: {log.get('reason')}\n\n")
            #write enumerated JSON sent to the engine
            f.write(f"\nenumerated post conditions: {list(abc)}")
            #write the test cases results
            f.write("\nTest Cases Results:")
            f.write(json.dumps(report.get("details", [])))
    elif not critical_crash_found and update_success:
        # If the run was clean AND the score update worked, save the CLEANED JSON back.
        # llm_json["test_cases"] contains the array of test cases that were executed
        # (with fixed IDs, normalized constraints, and cleaned regexes).
        print(f"[DB UPDATE] No critical failures found. Saving clean test suite for ID {prompt_id}...")
        
        try:
            updateTestcases(prompt_id, llm_json["test_cases"])
            
        except Exception as e:
            report["warning"] = report.get("warning", "") + f" DB Save Error: {e}"
            report["status"] = "WARNING" # Mark as warning if save fails
    # 6. View Results
    return report
    # print(report)

def _audit_worker(prompt_id, return_dict):
    """
    Runs in a separate process. 
    Completely isolated from the main script's memory.
    """
    try:
        # Re-importing inside the process isn't strictly necessary on Windows 
        # (since it reloads modules on spawn), but it's safe.
        print(f"   [Process {os.getpid()}] Starting Audit for ID {prompt_id}...")
        
        # Run your existing logic
        report = run_validator_engine_for_prompt(prompt_id)
        
        # Store result in the shared dictionary
        return_dict['report'] = report
        
    except Exception as e:
        print(f"   [Process {os.getpid()}] CRASHED: {e}")
        return_dict['report'] = {"status": "ERROR", "reason": f"Process Crash: {e}"}

# ==========================================
# Function to run the audit for multiple prompt IDs and save the reports
def run_audit_for_multiple_prompts(min_prompt_id: int, max_prompt_id: int):

    working_directory = os.getcwd()
    print(f"Current working directory: {working_directory}")
    #delete existing error/error_PBT folder if it exists
    error_folder = os.path.join(working_directory, "errors/errors_PBT")
    try:
        if os.path.exists(error_folder):
            shutil.rmtree(error_folder)
    except Exception as e:
        print(f"Error deleting error folder: {e}")
    #Create a report folder if it does not exist
    report_folder = os.path.join(working_directory, "reports")
    if not os.path.exists(report_folder):
        os.makedirs(report_folder)
    #report file path
    report_file_path = os.path.join(report_folder, "validation_reports.json")
    print(f"Report file path: {report_file_path}")

    all_results = []

    #open the report file in write mode
    with open(report_file_path, "w") as f:
        #run the validator engine and write the report into a json file
        for i in range(min_prompt_id, max_prompt_id + 1):
            
            print(f"\n\n=== Running Validator Engine for Prompt ID {i} ===")
            report = run_validator_engine_for_prompt(i)
            print(report)
            try:
                json.dump(report, f, indent=4)
            except Exception as e:
                print(f"Error writing report for Prompt ID {i}: {e}")

# ==========================================

#main function for testing
if __name__ == "__main__":
    # Example usage: run audit for prompt IDs 208 to 299
    run_audit_for_multiple_prompts(208,299)


# # ==========================================
# # 4. USAGE EXAMPLE
# # ==========================================
# if __name__ == "__main__":
    
#     # 1. Define Function (or path to file)
#     code_source = """
# import math
# def is_not_prime(n):
#     if n < 2: return False
#     # Returns True if composite (not prime)
#     # Check if any number from 2 to sqrt(n) divides n
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             return True
#     return False
# """

#     # 2. Define Data (JSON response from LLM)
#     # Note: 'perfect_square': True is a custom constraint we enabled
#     llm_json = {
#         "test_cases": [
#             {
#                 "id": "perfect_squares_are_composite",
#                 "description": "Verifies that perfect squares > 1 are identified as non-prime.",
#                 "execution_statement": "result = is_not_prime(n)",
#                 "input_types": { "n": "int" },
#                 "input_constraints": { 
#                     "n": { "min_val": 4, "max_val": 1000, "perfect_square": True } 
#                 },
#                 "postconditions": [
#                     { "assertion": "result == True" }
#                 ]
#             }
#         ]
#     }

#     # 3. Run Engine
#     engine = ValidatorEngine()
#     report = engine.run_audit_from_source(code_source, "is_not_prime", llm_json)
    
#     # 4. View Results
#     # print(report)



