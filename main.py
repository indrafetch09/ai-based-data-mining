import os

from dotenv import load_dotenv
from fastapi import FastAPI
from google import genai

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

app = FastAPI()
client = genai.Client(api_key=GEMINI_API_KEY)

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Hi from fastapi, please introduce yourself",
)


@app.get("/")
def read_root():
    return response.text
