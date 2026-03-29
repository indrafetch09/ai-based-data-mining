import lmstudio as lms
from fastapi import FastAPI

from app.core import system_prompt

app = FastAPI()

model = lms.llm("qwen/qwen3-1.7b")

result = model.respond(f"""
    ${system_prompt} Explain how data mining works effectively with LLM integration in bahasa

""")


@app.get("/")
def root():
    return {"message": "Welcome to my LLM based data mining AI"}


@app.get("/analyze")
def analyze():

    return {"message": result.content}
