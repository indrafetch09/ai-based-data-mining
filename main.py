import lmstudio as lms
from fastapi import FastAPI

app = FastAPI()

prompt = """
IMPORTANT: Provide response text only.
Do not include any explanations or additional text,
Do NOT use Markdown, do NOT use asterisks (**),
do NOT use hashtags (#), and do NOT use bullet points.
Explain how data mining works integration with LLM based models"""

model = lms.llm("qwen/qwen3-1.7b")
result = model.respond(prompt)


def clean_text(text):
    return text.replace("**", "").replace("#", "").replace("*", "")


# ERROR when result return a parameter and does not found the attribute
clean_text_result = clean_text(result)


@app.get("/")
def root():
    return {"message": "Welcome to my LLM based data mining AI"}


@app.get("/analyze")
def analyze():
    return {"message": clean_text_result}
