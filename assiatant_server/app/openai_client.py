# app/openai_client.py
import os
import openai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPEN_API_KEY")
client = openai.OpenAI(api_key=api_key)

assistant_id = os.getenv("ASSISTANT_ID")