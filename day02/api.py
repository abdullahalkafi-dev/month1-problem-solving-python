from fastapi import FastAPI, HTTPException
from char_frequency import char_frequency, char_frequency_only_alpha
from pydantic import BaseModel

app = FastAPI()


class TextData(BaseModel):
    text: str


@app.get("/")
def home():
    return {"message": "Welcome to Day 2!"}


@app.post("/char-frequency-all")
def get_char_frequency(body: TextData):
    print(body)
    text = body.text
    if not text:
        raise HTTPException(status_code=400, detail="Text field cannot be empty")
    return char_frequency(text)


@app.post("/char-frequency-alpha")
def get_char_frequency_alpha(body: TextData):
    print(body)
    text = body.text
    if not text:
        raise HTTPException(status_code=400, detail="Text field cannot be empty")
    return char_frequency_only_alpha(text)
