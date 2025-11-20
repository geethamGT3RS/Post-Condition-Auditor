"""This file has all the functions to make calls to the LLM API (gemini-Flash model)
to generate preconditions and postconditions for given Python functions."""
import os
import json
import re
import time
from dotenv import load_dotenv
from config import get_db_client
import ast  # <-- ADDED for parsing function name
from Prompts import updateTestcases
from Prompts import updateReasoning
import google.generativeai as genai
from typing import Tuple, Optional
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from google.api_core.exceptions import ResourceExhausted

#env file as .env in root directory
env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env')
print(f"Loading environment variables from: {env_path}")
if os.path.exists(env_path):
    load_dotenv(env_path)

#Set API Key
API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    API_KEY = "AIzaSyBgSkpBxN9snTdvVHLU0hjjpsXwZBoKf74" 
    if not API_KEY:
        raise ValueError("GEMINI_API_KEY environment variable not set. Please set it before running the script.")
    

# Define the class for the Two-Stage LLM Pipeline
class PostconditionPipeline:
    """A Two-Stage LLM Pipeline using Gemini API:
        1. The Reasoner: Generates reasoning about the function's pre and post conditions.
        2. The Translator: Converts reasoning into structured JSON output.
        """
    
    def __init__(self, api_key):
        """Initializes the Gemini API client and configurations."""
        # Initialize the Gemini API client
        genai.configure(api_key=api_key)
        
        # Configuration for "Thinking" (allows creativity)
        self.reasoning_config = genai.GenerationConfig(
            temperature=0.7
        )
        
        # Configuration for "Formatting" (strict structure)
        self.formatting_config = genai.GenerationConfig(
            temperature=0.1, 
            response_mime_type="application/json"
        )
        
        self.model = genai.GenerativeModel("gemini-2.0-flash")
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

    def process(self, func_name: str,initial_prompt: str, schema_instruction: str) -> Tuple[Optional[dict], Optional[str]]:
        """
        Executes the Two-Stage pipeline.
        Arguments:
        - func_name: The name of the function being analyzed.
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
                print(f"Thinking about the function...{func_name}")
                reasoning_response = self._send_request( chat_session, initial_prompt, self.reasoning_config)
                if reasoning_response is None:
                    raise Exception("Reasoning stage failed.")
                raw_reasoning = reasoning_response
                # print("Reasoning complete.")
                # print(f"Raw reasoning output:\n{raw_reasoning}\n")
                break
            except Exception as e:
                print(f"Error during reasoning stage on attempt {attempt + 1}/{self.max_retries}: {e}")
                time.sleep(self.backoff_time * (2 ** attempt))  # Exponential backoff
        else:
            print("Max retries reached. Reasoning stage failed.")
            return None, None

        # --- STAGE 2: The Translator ---
        print("2. Formatting output...")

        for attempt in range(self.max_retries):
            try:

                format_prompt = f"""
        Based on your previous explanation, output the data using this exact JSON object structure:
        {schema_instruction}
        The function being analyzed is named: {func_name} and do not include the import statement for this function in the setup statements.
        Do not add any new information, just structure the existing response. 
        """
                formatting_response = self._send_request(chat_session, format_prompt, self.formatting_config)
                if formatting_response is None:
                    raise Exception("Formatting stage failed.")
                structured_response = formatting_response
                # print("Formatting complete.")   
                # print(f"Structured output:\n{structured_response}\n")
                break
            except Exception as e:
                print(f"Error during formatting stage on attempt {attempt + 1}/{self.max_retries}: {e}")
                time.sleep(self.backoff_time * (2 ** attempt))  # Exponential backoff
        else:
            print("Max retries reached. Formatting stage failed.")
            return None, raw_reasoning

        # --- STAGE 3: The Auditor (Parsing) ---
        try:
            return json.loads(structured_response.text), raw_reasoning
        except json.JSONDecodeError:
            print("Error: Failed to parse JSON.")
            return None, raw_reasoning
        
    
    def process_missin_structureddata(self, raw_reasoning, func_name: str, schema_instruction: str) -> Optional[list]:
        """
        It takes in the reasoning text output from the LLM and function name and then calls the LLM again to extract the structured JSON data.
        Arguments:
        - raw_reasoning: The raw text output from the reasoning stage.
        - func_name: The name of the function being analyzed.
        - schema_instruction: The JSON schema instruction for formatting.
        Returns:
        - structured_response: The final structured JSON output from the LLM.
        """
        # We do not need a chat session here as we are only formatting the existing reasoning
        # --- STAGE 2: The Translator ---
        print("2. Formatting output...")

        # try:
        #     chat_session = self.model.start_chat(history=[])
        # except Exception as e:
        #     print(f"Error starting chat session with Gemini API: {e}")
        #     return None

        print("Re-formatting missing structured data...")

        for attempt in range(self.max_retries):
            try:

                format_prompt = f"""
        Here is the previous analysis for post-conditions of a Python function {func_name}:
        {raw_reasoning}
        Based strictly on the text above, output the data using this exact JSON object structure:
        {schema_instruction}
        The function being analyzed is named: {func_name} and do not include the import statement for this function in the setup statements.
        Do not add any new information, just structure the above shared analysis. 
        """
                formatting_response = self._send_formatting_request(format_prompt, self.formatting_config)
                if formatting_response is None:
                    raise Exception("Formatting stage failed.")
                structured_response = formatting_response
                # print("Formatting complete.")   
                # print(f"Structured output:\n{structured_response}\n")
                break
            except Exception as e:
                print(f"Error during formatting stage on attempt {attempt + 1}/{self.max_retries}: {e}")
                time.sleep(self.backoff_time * (2 ** attempt))  # Exponential backoff
        else:
            print("Max retries reached. Formatting stage failed.")
            return None

        # --- STAGE 3: The Auditor (Parsing) ---
        try:
            return json.loads(structured_response.text)
        except json.JSONDecodeError:
            print("Error: Failed to parse JSON.")
            return None

# --- USAGE EXAMPLE ---

# Define your schema constraint
target_schema = """
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Function Test Case Schema",
  "type": "object",
  "properties": {
    "test_cases": {
      "type": "array",
      "description": "A list of individual test scenarios for the function.",
      "items": {
        "type": "object",
        "required": [
          "test_case_name",
          "preconditions",
          "postconditions"
        ],
        "properties": {
          "test_case_name": {
            "type": "string",
            "description": "A descriptive name for the test case."
          },
          "preconditions": {
            "type": "object",
            "description": "The setup and function call required before testing postconditions.",
            "required": ["setup_statement"],
            "properties": {
              "setup_statement": {
                "type": "string",
                "description": "An ordered list of Python statements to set up inputs and call the function.",
                "minItems": 1
              }
            }
          },
          "postconditions": {
            "type": "array",
            "description": "A list of conditions and assertions that must be true after the function executes.",
            "items": {
              "type": "object",
              "required": [
                "description",
                "assert_statement"
              ],
              "properties": {
                "description": {
                  "type": "string",
                  "description": "A human-readable description of the expected result."
                },
                "assert_statement": {
                  "type": "string",
                  "description": "The verifiable Python assertion statement (e.g., 'assert result == 20')."
                }
              }
            },
            "minItems": 1
          }
        }
      }
    }
  },
  "required": ["test_cases"]
}
"""
# Helper function to extract function name from code string
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
    pipeline = PostconditionPipeline(API_KEY)
    structured_data, raw_reasoning = pipeline.process(function_name, initial_prompt, target_schema)

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
        print(f"Failed to generate postconditions for Prompt ID {prompt_id}.")
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
    pipeline = PostconditionPipeline(API_KEY)
    structured_data = pipeline.process_missin_structureddata(raw_reasoning, func_name, target_schema)
    if structured_data is None:
        print(f"Failed to generate structured data for Prompt ID {prompt_id}.")
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
                print(f"Failed to generate postconditions for Prompt ID {prompt_id}.")
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
if __name__ == "__main__":
    prompt_id=1
    # print(f"Generating and updating postconditions for Prompt ID {prompt_id}...")
    # success = generate_and_update_postconditions_byPrompt(prompt_id)
    # if not success:
    #     print(f"Failed to generate postconditions for Prompt ID {prompt_id}.")
    # time.sleep(4)
    # prompt_id=2
    # print(f"Generating and updating postconditions for Prompt ID {prompt_id}...")
    # success = generate_and_update_postconditions_byPrompt(prompt_id)
    # if not success:
    #     print(f"Failed to generate postconditions for Prompt ID {prompt_id}.")
    print(f"Updating test cases for Prompt ID {prompt_id}...")
    success = update_testcases_for_prompt(prompt_id)
    if not success:
        print(f"Failed to update test cases for Prompt ID {prompt_id}.")
    prompt_id=2
    print(f"Updating test cases for Prompt ID {prompt_id}...")
    success = update_testcases_for_prompt(prompt_id)
    if not success:
        print(f"Failed to update test cases for Prompt ID {prompt_id}.")
    prompt_id=3
    print(f"Updating test cases for Prompt ID {prompt_id}...")
    success = update_testcases_for_prompt(prompt_id)
    if not success:
        print(f"Failed to update test cases for Prompt ID {prompt_id}.")