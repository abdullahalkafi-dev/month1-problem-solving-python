from fastapi import FastAPI
from pydantic import BaseModel

from timed_problems import first_non_repeating_char

app = FastAPI()


class TextBody(BaseModel):
    text: str


@app.get("/")
def home():
    return {"message": "Welcome to Day 6!"}


@app.post("/first-non-repeating")
def get_first_non_repeating(body: TextBody):
    result = first_non_repeating_char(body.text)
    return {"result": result}
