import os
import sys
from dotenv import load_dotenv
from langchain.agents import create_agent
# Load environment variables from .env file
load_dotenv()

# Initialize the Gemini client
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("Error: GEMINI_API_KEY not found.")
    print("Make sure you have set GEMINI_API_KEY in your .env file.")
    sys.exit(1)

client = genai.Client(api_key=api_key)


