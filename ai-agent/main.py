import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

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

response_content = client.models.generate_content(model="gemini-2.5-flash", contents=messages)

verbose_debug = f"""
User prompt: {args.prompt}
Prompt tokens: {response_content.usage_metadata.prompt_token_count}
Response tokens: {response_content.usage_metadata.candidates_token_count}
      """

if args.verbose:
    print(verbose_debug)

print(response_content.text)