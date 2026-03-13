import lmstudio as lms
from fastapi import FastAPI

app = FastAPI()

model = lms.llm("qwen/qwen3.5-9b")
result = model.respond("Hai")


@app.get("/")
async def root():
    return {"message": "Welcome to my sassy AI"}


@app.get("/analyze")
async def analyze():
    return {"message": result}
