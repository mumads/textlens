from fastapi import FastAPI 
from pydantic import BaseModel 
from nlp_tools import analyze_text

app = FastAPI(title="TextLens - NLP API")

class TextInput(BaseModel):
    text: str


@app.get("/")
def read_root():
    return {"message": "Welcome to TextLens NLP API!"}

@app.post("/analyze")
def analyize(input: TextInput):
    result = analyze_text(input.text)
    return result
