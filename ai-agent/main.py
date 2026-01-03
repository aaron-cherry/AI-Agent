import os
import argparse
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key == None:
    raise RuntimeError("api key not found")

parser = argparse.ArgumentParser(description="Prompts Google Gemini with arguement and displays response")
parser.add_argument("prompt", type=str, help="User prompt")
args = parser.parse_args()

client = genai.Client(api_key=api_key)

content = client.models.generate_content(model="gemini-2.5-flash", contents=args.prompt)

print(f"""
Prompt tokens: {content.usage_metadata.prompt_token_count}
Response tokens: {content.usage_metadata.candidates_token_count}
      """)

print(content.text)