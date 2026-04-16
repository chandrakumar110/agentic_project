import os
import sys
from dotenv import load_dotenv
import google.generativeai as genai
from prompts.system_prompts import user_intent_classification_prompt

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("Error: GEMINI_API_KEY not found.")
    print("Make sure you have set GEMINI_API_KEY in your .env file.")
    sys.exit(1)

genai.configure(api_key=api_key)
model = genai.GenerativeModel(
    "gemini-2.0-flash",
    system_instruction=user_intent_classification_prompt
)

def classify_user_intent(user_input):
    response = model.generate_content(user_input)
    return response.text