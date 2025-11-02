import json
import time
import asyncio
import httpx
import re
import os
from pymongo import MongoClient

# Import from your existing project structure
import Prompts
from config import get_db_client

# --- Gemini API Configuration ---
# Use gemini-2.5-flash-preview-09-2025 model
API_KEY = ""
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-09-2025:generateContent?key={API_KEY}"

JSON_SCHEMA = {
    "type": "OBJECT",
    "properties": {
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
    "required": ["postconditions"]
}

async def call_gemini_api(prompt_text: str, strategy: str) -> str | None:
    """
    Calls the Gemini API with the given prompt and handles retries.
    Requests a JSON response based on the defined schema.
    """
    headers = {'Content-Type': 'application/json'}
    
    # Construct the payload
    payload = {
        "contents": [{"parts": [{"text": prompt_text}]}],
        "generationConfig": {
            "responseMimeType": "application/json",
            "responseSchema": JSON_SCHEMA
        }
    }
    
    # For Naive/FewShot, we don't request JSON, so remove the generationConfig
    if strategy != "ChainOfThought_strategy":
         # Remove the config asking for JSON
        payload.pop("generationConfig", None)
        # Manually add the prompt instruction for JSON format
        payload["contents"][0]["parts"][0]["text"] = (
            f"{prompt_text}\n\n"
            "IMPORTANT: Please provide your response ONLY as a valid JSON object "
            '{"postconditions": [{"description": "...", "assert_statement": "..."}]}'
        )


    backoff_time = 1.0  # Initial retry delay in seconds
    max_retries = 5

    # Use httpx.AsyncClient for async requests
    async with httpx.AsyncClient(timeout=60.0) as client:
        for attempt in range(max_retries):
            try:
                response = await client.post(API_URL, headers=headers, json=payload)

                # Check for HTTP errors
                response.raise_for_status() 

                # Successful call, return the text content
                # The response from Gemini is a JSON object, and we need the text part.
                result_json = response.json()
                
                # Debug: Print the raw response to see its structure
                # print(f"--- RAW API Response (Prompt {prompt_text[:20]}...) ---")
                # print(json.dumps(result_json, indent=2))
                # print("--------------------------------------------------")

                # Extract the text part which contains our *application* JSON
                if "candidates" in result_json and len(result_json["candidates"]) > 0:
                    text_content = result_json["candidates"][0]["content"]["parts"][0]["text"]
                    return text_content
                else:
                    print(f"API call successful but no candidates found in response for prompt: {prompt_text[:50]}...")
                    return None

            except httpx.HTTPStatusError as e:
                print(f"HTTP Error {e.response.status_code} for prompt: {prompt_text[:50]}... Response: {e.response.text}")
                # Don't retry on client errors (like 400 Bad Request)
                if 400 <= e.response.status_code < 500:
                    print("Client error. Aborting retries.")
                    return None 
            except httpx.RequestError as e:
                print(f"RequestError during API call: {e}. Retrying in {backoff_time}s...")
            except Exception as e:
                print(f"Unexpected exception during API call: {e}. Retrying in {backoff_time}s...")

            # Exponential backoff
            await asyncio.sleep(backoff_time)
            backoff_time *= 2  # Double the wait time for the next retry

    print(f"Failed to call API for prompt: {prompt_text[:50]}... after {max_retries} retries.")
    return None

def parse_and_clean_json(api_response: str) -> list[dict] | None:
    """
    Parses the raw string response from the LLM, cleans it,
    and returns the list of postcondition objects.
    This is the robust version that fixes JSONDecodeError.
    """
    if not api_response:
        return None

    try:
        # Use regex to find the JSON block. This is more reliable than splitting.
        # This looks for the first '{' and the last '}'
        # re.DOTALL makes '.' match newlines
        json_match = re.search(r"\{.*\}", api_response, re.DOTALL)
        
        if not json_match:
            print(f"No JSON object ({{...}}) found in API response: {api_response[:200]}...")
            return None
            
        cleaned_response = json_match.group(0)

        # Fix for JSONDecodeError: Replace non-breaking spaces (U+00A0) and other weird whitespace
        cleaned_response = cleaned_response.replace(u'\u00A0', ' ')

        # Parse the cleaned string as JSON
        data = json.loads(cleaned_response)

        # Validate the structure
        if "postconditions" in data and isinstance(data["postconditions"], list):
            # Further validation: check if items are dicts with correct keys
            valid_postconditions = []
            for item in data["postconditions"]:
                if (isinstance(item, dict) and 
                    "description" in item and 
                    "assert_statement" in item):
                    valid_postconditions.append(item)
                else:
                    print(f"Skipping malformed postcondition item: {item}")
            
            if not valid_postconditions:
                 print(f"Parsed JSON, but 'postconditions' list was empty or malformed.")
                 return None

            return valid_postconditions
        else:
            print(f"Failed to find 'postconditions' list in parsed JSON: {data}")
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
    Fetches all prompts that do not have post-conditions generated yet.
    """
    client, db = get_db_client()
    prompts_collection = db["FunctionPrompts"]
    
    # Find prompts where Post_Conditions is an empty array
    pending_prompts = list(prompts_collection.find({"Post_Conditions": []}))
    
    print(f"Found {len(pending_prompts)} pending prompts to process.")
    client.close()
    return pending_prompts

async def process_prompts():
    """
    Main function to orchestrate fetching, calling API, and storing results.
    """
    pending_prompts = get_pending_prompts()
    
    for prompt in pending_prompts:
        prompt_id = prompt["Prompt_ID"]
        prompt_text = prompt["Prompt_Text"]
        prompt_strategy = prompt["Prompt_Strategy"]

        print(f"Processing Prompt ID: {prompt_id} (Strategy: {prompt_strategy})")

        response_text = await call_gemini_api(prompt_text, prompt_strategy)

        if not response_text:
            print(f"Skipping Prompt ID {prompt_id} due to API failure.")
            continue

        # Now, parse the response and store it
        try:
            # Use the robust parser
            post_conditions_list = parse_and_clean_json(response_text)

            if post_conditions_list:
                print(f"Successfully parsed {len(post_conditions_list)} postconditions for Prompt ID: {prompt_id}.")
                # We have the list! Let's update the database.
                Prompts.updatePostConditions(prompt_id, post_conditions_list)
                print(f"Successfully updated post-conditions for Prompt ID {prompt_id}.")
            else:
                print(f"Error: Failed to parse valid JSON for Prompt ID {prompt_id}.")
                print(f"Raw response was: {response_text[:300]}...")

        except Exception as e:
            print(f"An error occurred during post-processing for Prompt ID {prompt_id}: {e}")


async def main():
    """Main entry point for async execution."""
    print("Starting LLM Interaction Module...")
    await process_prompts()
    print("LLM Interaction Module finished.")

if __name__ == "__main__":
    # This is the standard way to run an async main function in a script.
    # Note: This environment may support top-level await.
    # If so, you could run `await main()` directly.
    try:
        asyncio.run(main())
    except RuntimeError:
        # If asyncio is already running (e.g., in Jupyter/Canvas)
        # you might just await it.
        print("Asyncio already running. Awaiting main().")
        # In a real notebook/interactive environment, you'd just call:
        # await main()

