import os
import sys
from dotenv import load_dotenv
import google.generativeai as genai
from agent_prompts import weather_prompt,news_prompt,general_prompt


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("Error: GEMINI_API_KEY not found.")
    print("Make sure you have set GEMINI_API_KEY in your .env file.")
    sys.exit(1)


genai.configure(api_key=api_key)

def answer_user_query(user_intent,user_query):
    if user_intent == "weather_report":
        system_prompt = weather_prompt
    elif user_intent == "news_report":
        system_prompt = news_prompt
    else:
        system_prompt = general_prompt
        
    model = genai.GenerativeModel(
        "gemini-2.0-flash",
        system_instruction=system_prompt
    )
    response = model.generate_content(user_query)

    return response.text

