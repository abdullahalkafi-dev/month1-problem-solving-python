from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from factorial import factorial_loop, factorial_recursion
from palindrome_checker import palindrome_checker, palindrome_checker_slice

app = FastAPI()


class NumberData(BaseModel):
	number: int


class TextData(BaseModel):
	text: str


@app.get("/")
def home():
	return {"message": "Welcome to Day 3!"}


@app.post("/factorial-loop")
def get_factorial_loop(body: NumberData):
	print(body)
	number = body.number
	try:
		return {"number": number, "factorial": factorial_loop(number)}
	except (TypeError, ValueError) as error:
		raise HTTPException(status_code=400, detail=str(error))


@app.post("/factorial-recursion")
def get_factorial_recursion(body: NumberData):
	print(body)
	number = body.number
	try:
		return {"number": number, "factorial": factorial_recursion(number)}
	except (TypeError, ValueError) as error:
		raise HTTPException(status_code=400, detail=str(error))


@app.post("/palindrome-loop")
def check_palindrome_loop(body: TextData):
	print(body)
	text = body.text
	if not text:
		raise HTTPException(status_code=400, detail="Text field cannot be empty")
	return {"text": text, "is_palindrome": palindrome_checker(text)}


@app.post("/palindrome-slice")
def check_palindrome_slice(body: TextData):
	print(body)
	text = body.text
	if not text:
		raise HTTPException(status_code=400, detail="Text field cannot be empty")
	return {"text": text, "is_palindrome": palindrome_checker_slice(text)}
