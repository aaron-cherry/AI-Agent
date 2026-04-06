import os
import argparse
import prompts
from dotenv import load_dotenv
from google import genai
from google.genai import types
from call_function import available_functions, call_function

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key == None:
    raise RuntimeError("api key not found")

parser = argparse.ArgumentParser(description="Prompts Google Gemini with arguement and displays response")
parser.add_argument("prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages = [types.Content(role="user", parts=[types.Part(text=args.prompt)])]

client = genai.Client(api_key=api_key)

response_content = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=messages,
    config=types.GenerateContentConfig(tools=[available_functions], system_instruction=prompts.system_prompt)
    )

verbose_debug = f"""
User prompt: {args.prompt}
Prompt tokens: {response_content.usage_metadata.prompt_token_count}
Response tokens: {response_content.usage_metadata.candidates_token_count}
      """

if args.verbose: print(verbose_debug)

if response_content.function_calls:
    function_responses = []
    for function_call in response_content.function_calls:
        result = call_function(function_call, args.verbose)
        if result.parts is None: raise Exception("result.parts is empty/None")
        if result.parts[0].function_response is None: raise Exception("first part of function response is None")
        if result.parts[0].function_response.response is None: raise Exception("function response is None")
        function_responses.append(result.parts[0])
        if args.verbose:
            print(f"-> {result.parts[0].function_response.response}")
    #exit()

if not response_content.function_calls:
    print(response_content.text)