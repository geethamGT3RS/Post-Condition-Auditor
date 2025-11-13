import json
import time
import asyncio
import httpx
import re
import os
import ast  # <-- ADDED for parsing function name
from pymongo import MongoClient

# Import from your existing project structure
import Prompts
from config import get_db_client

# --- Gemini API Configuration ---
API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    API_KEY = "AIzaSyCnZ4LOJQ0aezDIfBNdYvHinWgBSyYw6oo" 
    if not API_KEY:
        raise ValueError("GEMINI_API_KEY environment variable not set. Please set it before running the script.")

API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-09-2025:generateContent?key={API_KEY}"


# --- JSON Schema ---
JSON_SCHEMA = {
    "type": "OBJECT",
    "properties": {
        "preconditions": {
            "type": "ARRAY",
            "items": {
                "type": "OBJECT",
                "properties": {
                    "setup_statement": {"type": "STRING"}
                },
                "required": ["setup_statement"]
            }
        },
        "postconditions": {
            "type": "ARRAY",
            "items": {
                "type": "OBJECT",
                "properties": {
                    "description": {"type": "STRING"},
                    "assert_statement": {"type": "STRING"}
                },
                "required": ["description", "assert_statement"]
            }
        }
    },
    "required": ["preconditions", "postconditions"]
}

# ---!!! ADDED HELPER FUNCTION !!!---
def get_function_name(code_str: str) -> str | None:
    """
    Parses a string of Python code and returns the name
    of the first function defined in it.
    """
    try:
        tree = ast.parse(code_str)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                return node.name
    except Exception as e:
        print(f"Error parsing function name from code: {e}")
    return None

# ---!!! THIS FUNCTION IS UPDATED !!!---
async def call_gemini_api(prompt_text: str, strategy: str, func_name: str) -> str | None:
    """
    Calls the Gemini API with the given prompt and handles retries.
    Requests a JSON response based on the defined schema.
    
    Args:
        prompt_text: The user's original prompt.
        strategy: The prompt strategy.
        func_name: The *actual* function name from the database.
    """
    headers = {'Content-Type': 'application/json'}
    
    payload = {
        "contents": [{"parts": [{"text": ""}]}], # We will overwrite text below
        "generationConfig": {
            "responseMimeType": "application/json",
            "responseSchema": JSON_SCHEMA
        }
    }
    
    # ---!!! THIS IS THE NEW FIX !!!---
    # We now explicitly tell the LLM the *correct* function name.
    detailed_json_instruction = (
        f"{prompt_text}\n\n"
        f"IMPORTANT: The function you are generating test cases for is named: {func_name}\n"
        "Please provide your response ONLY as a valid JSON object matching the schema.\n\n"
        "1. The 'preconditions' array must contain N+1 'setup_statement's for each test case.\n"
        "   - The first N statements set up input parameters (e.g., 'list_a = [1, 2]').\n"
        f"  - The *last* (N+1) statement MUST be the function call *using the name {func_name}*, assigning its output to a variable (e.g., 'result = {func_name}(list_a)').\n"
        "2. The 'postconditions' array must contain the 'assert_statement' that *uses* the 'result' variable (e.g., 'assert result == 3').\n\n"
        f"Example format for a function 'add_numbers(a, b)' (if func_name was 'add_numbers'):\n"
        '{"preconditions": ['
        '  {"setup_statement": "a = 10"},'
        '  {"setup_statement": "b = 20"},'
        '  {"setup_statement": "sum_result = add_numbers(a, b)"}'
        '],'
        '"postconditions": ['
        '  {"description": "The sum should be 30", "assert_statement": "assert sum_result == 30"}'
        ']}'
    )
    
    # Set the modified prompt text
    payload["contents"][0]["parts"][0]["text"] = detailed_json_instruction
    # --- END OF MODIFICATION ---


    backoff_time = 1.0
    max_retries = 5

    async with httpx.AsyncClient(timeout=60.0) as client:
        for attempt in range(max_retries):
            try:
                response = await client.post(API_URL, headers=headers, json=payload)
                response.raise_for_status() 
                result_json = response.json()
                
                if "candidates" in result_json and len(result_json["candidates"]) > 0:
                    text_content = result_json["candidates"][0]["content"]["parts"][0]["text"]
                    return text_content
                else:
                    print(f"API call successful but no candidates found for prompt: {prompt_text[:50]}...")
                    return None

            except httpx.HTTPStatusError as e:
                print(f"HTTP Error {e.response.status_code} for prompt: {prompt_text[:50]}... Response: {e.response.text}")
                if 400 <= e.response.status_code < 500:
                    print("Client error. Aborting retries.")
                    return None 
            except httpx.RequestError as e:
                print(f"RequestError during API call: {e}. Retrying in {backoff_time}s...")
            except Exception as e:
                print(f"Unexpected exception during API call: {e}. Retrying in {backoff_time}s...")

            await asyncio.sleep(backoff_time)
            backoff_time *= 2

    print(f"Failed to call API for prompt: {prompt_text[:50]}... after {max_retries} retries.")
    return None

def parse_and_clean_json(api_response: str) -> dict | None:
    """
    Parses the raw string response from the LLM, cleans it,
    and returns a dictionary containing both lists:
    {"preconditions": [...], "postconditions": [...]}
    """
    if not api_response:
        return None

    try:
        json_match = re.search(r"\{.*\}", api_response, re.DOTALL)
        
        if not json_match:
            print(f"No JSON object ({{...}}) found in API response: {api_response[:200]}...")
            return None
            
        cleaned_response = json_match.group(0)
        cleaned_response = cleaned_response.replace(u'\u00A0', ' ')
        data = json.loads(cleaned_response)

        if ("postconditions" in data and isinstance(data["postconditions"], list) and
            "preconditions" in data and isinstance(data["preconditions"], list)):

            valid_postconditions = []
            for item in data["postconditions"]:
                if (isinstance(item, dict) and 
                    "description" in item and 
                    "assert_statement" in item):
                    valid_postconditions.append(item)
                else:
                    print(f"Skipping malformed postcondition item: {item}")
            
            valid_preconditions = []
            for item in data["preconditions"]:
                if (isinstance(item, dict) and "setup_statement" in item):
                    valid_preconditions.append(item)
                else:
                    print(f"Skipping malformed precondition item: {item}")

            if not valid_postconditions or not valid_preconditions:
                 print(f"Parsed JSON, but 'preconditions' or 'postconditions' list was empty or malformed.")
                 return None

            return {
                "preconditions": valid_preconditions,
                "postconditions": valid_postconditions
            }
        else:
            print(f"Failed to find 'preconditions' AND 'postconditions' lists in parsed JSON: {data}")
            return None

    except json.JSONDecodeError as e:
        print(f"JSONDecodeError: Failed to parse API response: {e}")
        print(f"Raw response was: {api_response[:200]}...")
        return None
    except Exception as e:
        print(f"Unexpected error in parse_and_clean_json: {e}")
        return None


def get_pending_prompts():
    """
    Fetches all prompts that do not have post-conditions generated yet
    or were processed with old logic (empty pre-conditions).
    """
    client, db = get_db_client()
    prompts_collection = db["FunctionPrompts"]
    
    pending_prompts = list(prompts_collection.find({
        "$or": [
            {"Post_Conditions": []},
            {"Pre_Conditions": []}
        ]
    }))
    
    print(f"Found {len(pending_prompts)} pending prompts to process.")
    client.close()
    return pending_prompts

# ---!!! THIS FUNCTION IS UPDATED !!!---
async def process_prompts():
    """
    Main function to orchestrate fetching, calling API, and storing results.
    """
    pending_prompts = get_pending_prompts()
    
    client, db = get_db_client()
    prompts_collection = db["FunctionPrompts"]
    functions_collection = db["Functions"] # <-- ADDED
    
    for prompt in pending_prompts:
        prompt_id = prompt["Prompt_ID"]
        prompt_text = prompt["Prompt_Text"]
        prompt_strategy = prompt["Prompt_Strategy"]
        function_id = prompt.get("Function_ID")

        print(f"Processing Prompt ID: {prompt_id} (Strategy: {prompt_strategy})")

        # ---!!! ADDED LOGIC TO GET FUNC_NAME !!!---
        if not function_id:
            print(f"  - ERROR: Prompt ID {prompt_id} has no Function_ID. Skipping.")
            continue
            
        function_doc = functions_collection.find_one({"Function_ID": function_id})
        if not function_doc:
            print(f"  - ERROR: Could not find Function_ID {function_id} in Functions collection. Skipping.")
            continue
            
        function_code = function_doc.get("Function_Code")
        if not function_code:
            print(f"  - ERROR: Function {function_id} has no Function_Code. Skipping.")
            continue
            
        func_name = get_function_name(function_code)
        if not func_name:
            print(f"  - ERROR: Could not parse function name from Function_Code for {function_id}. Skipping.")
            continue
            
        print(f"  - Found real function name: {func_name}")
        # ---!!! END OF ADDED LOGIC !!!---

        # Pass the correct func_name to the API
        response_text = await call_gemini_api(prompt_text, prompt_strategy, func_name)

        if not response_text:
            print(f"Skipping Prompt ID {prompt_id} due to API failure.")
            continue

        try:
            parsed_data = parse_and_clean_json(response_text)

            if parsed_data:
                pre_conditions_list = parsed_data["preconditions"]
                post_conditions_list = parsed_data["postconditions"]
                
                print(f"Successfully parsed {len(pre_conditions_list)} pre-conditions and "
                      f"{len(post_conditions_list)} post-conditions for Prompt ID: {prompt_id}.")
                
                prompts_collection.update_one(
                    {"Prompt_ID": prompt_id},
                    {
                        "$set": {
                            "Pre_Conditions": pre_conditions_list,
                            "Post_Conditions": post_conditions_list
                        }
                    }
                )
                print(f"Successfully updated DB for Prompt ID {prompt_id}.")
            else:
                print(f"Error: Failed to parse valid JSON for Prompt ID {prompt_id}.")
                print(f"Raw response was: {response_text[:300]}...")

        except Exception as e:
            print(f"An error occurred during post-processing for Prompt ID {prompt_id}: {e}")
            
    client.close()
    print("Database connection closed.")


async def main():
    """Main entry point for async execution."""
    print("Starting LLM Interaction Module...")
    await process_prompts()
    print("LLM Interaction Module finished.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except RuntimeError:
        # Handle already-running asyncio loop (e.g., in Jupyter)
        print("Asyncio already running. Awaiting main().")
        loop = asyncio.get_event_loop()
        loop.create_task(main())