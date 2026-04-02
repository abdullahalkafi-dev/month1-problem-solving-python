from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from bank_account import BankAccount
from inventory_item import InventoryItem

app = FastAPI()

accounts_store: dict[str, BankAccount] = {}
items_store: dict[str, InventoryItem] = {}


class AccountCreateBody(BaseModel):
	account_number: str
	owner_name: str
	balance: float


class AmountBody(BaseModel):
	amount: float


class ItemCreateBody(BaseModel):
	sku: str
	name: str
	price: float
	quantity: int


class QtyBody(BaseModel):
	qty: int


class PriceBody(BaseModel):
	new_price: float


@app.get("/")
def home():
	return {"message": "Welcome to Day 5!"}


@app.post("/accounts")
def create_account(body: AccountCreateBody):
	if body.account_number in accounts_store:
		raise HTTPException(status_code=400, detail="account already exists")

	try:
		account = BankAccount(body.account_number, body.owner_name, body.balance)
	except (TypeError, ValueError) as error:
		raise HTTPException(status_code=400, detail=str(error))

	accounts_store[body.account_number] = account
	return {
		"account_number": account.account_number,
		"owner_name": account.owner_name,
		"balance": account.get_balance(),
	}


@app.post("/accounts/{account_number}/deposit")
def deposit(account_number: str, body: AmountBody):
	account = accounts_store.get(account_number)
	if account is None:
		raise HTTPException(status_code=404, detail="account not found")

	try:
		balance = account.deposit(body.amount)
	except (TypeError, ValueError) as error:
		raise HTTPException(status_code=400, detail=str(error))

	return {"account_number": account_number, "balance": balance}


@app.post("/accounts/{account_number}/withdraw")
def withdraw(account_number: str, body: AmountBody):
	account = accounts_store.get(account_number)
	if account is None:
		raise HTTPException(status_code=404, detail="account not found")

	try:
		balance = account.withdraw(body.amount)
	except TypeError as error:
		raise HTTPException(status_code=400, detail=str(error))
	except ValueError as error:
		if str(error) == "Not enough balance":
			raise HTTPException(status_code=400, detail="insufficient funds")
		raise HTTPException(status_code=400, detail=str(error))

	return {"account_number": account_number, "balance": balance}


@app.get("/accounts/{account_number}")
def get_account(account_number: str):
	account = accounts_store.get(account_number)
	if account is None:
		raise HTTPException(status_code=404, detail="account not found")

	return {
		"account_number": account.account_number,
		"owner_name": account.owner_name,
		"balance": account.get_balance(),
	}


@app.post("/items")
def create_item(body: ItemCreateBody):
	if body.sku in items_store:
		raise HTTPException(status_code=400, detail="item already exists")

	try:
		item = InventoryItem(body.sku, body.name, body.price, body.quantity)
	except (TypeError, ValueError) as error:
		raise HTTPException(status_code=400, detail=str(error))

	items_store[body.sku] = item
	return {
		"sku": item.sku,
		"name": item.name,
		"price": item._price,
		"quantity": item._quantity,
		"inventory_value": item.inventory_value(),
	}


@app.post("/items/{sku}/add-stock")
def add_stock(sku: str, body: QtyBody):
	item = items_store.get(sku)
	if item is None:
		raise HTTPException(status_code=404, detail="item not found")

	try:
		quantity = item.add_stock(body.qty)
	except (TypeError, ValueError) as error:
		raise HTTPException(status_code=400, detail=str(error))

	return {"sku": sku, "quantity": quantity}


@app.post("/items/{sku}/remove-stock")
def remove_stock(sku: str, body: QtyBody):
	item = items_store.get(sku)
	if item is None:
		raise HTTPException(status_code=404, detail="item not found")

	try:
		quantity = item.remove_stock(body.qty)
	except (TypeError, ValueError) as error:
		raise HTTPException(status_code=400, detail=str(error))

	return {"sku": sku, "quantity": quantity}


@app.patch("/items/{sku}/price")
def set_price(sku: str, body: PriceBody):
	item = items_store.get(sku)
	if item is None:
		raise HTTPException(status_code=404, detail="item not found")

	try:
		price = item.set_price(body.new_price)
	except (TypeError, ValueError) as error:
		raise HTTPException(status_code=400, detail=str(error))

	return {
		"sku": sku,
		"price": price,
		"inventory_value": item.inventory_value(),
	}


@app.get("/items/{sku}")
def get_item(sku: str):
	item = items_store.get(sku)
	if item is None:
		raise HTTPException(status_code=404, detail="item not found")

	return {
		"sku": item.sku,
		"name": item.name,
		"price": item._price,
		"quantity": item._quantity,
		"inventory_value": item.inventory_value(),
	}
