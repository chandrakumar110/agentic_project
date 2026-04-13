import os
import sys
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("Error: GEMINI_API_KEY not found.")
    print("Make sure you have set GEMINI_API_KEY in your .env file.")
    sys.exit(1)

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-flash")

def get_weather_report(query):
    response = model.generate_content(query)
    return response.text

# if __name__ == "__main__":
#     query = "What is the weather like today?"
#     report = get_weather_report(query)
#     print(report)




