import pytest
from fastapi.testclient import TestClient

from api import app, accounts_store, items_store


@pytest.fixture(autouse=True)
def clear_stores():
	accounts_store.clear()
	items_store.clear()


def test_bank_flow():
	client = TestClient(app)

	create_res = client.post(
		"/accounts",
		json={"account_number": "AC-100", "owner_name": "John", "balance": 1000},
	)
	assert create_res.status_code == 200
	assert create_res.json()["balance"] == 1000.0

	deposit_res = client.post("/accounts/AC-100/deposit", json={"amount": 300})
	assert deposit_res.status_code == 200
	assert deposit_res.json() == {"account_number": "AC-100", "balance": 1300.0}

	withdraw_res = client.post("/accounts/AC-100/withdraw", json={"amount": 200})
	assert withdraw_res.status_code == 200
	assert withdraw_res.json() == {"account_number": "AC-100", "balance": 1100.0}


def test_bank_insufficient_funds():
	client = TestClient(app)

	client.post(
		"/accounts",
		json={"account_number": "AC-101", "owner_name": "Jane", "balance": 1000},
	)
	res = client.post("/accounts/AC-101/withdraw", json={"amount": 5000})

	assert res.status_code == 400
	assert res.json() == {"detail": "insufficient funds"}


def test_create_account_invalid_balance():
	client = TestClient(app)

	res = client.post(
		"/accounts",
		json={"account_number": "AC-102", "owner_name": "Bob", "balance": -1},
	)

	assert res.status_code == 400


def test_inventory_flow():
	client = TestClient(app)

	create_res = client.post(
		"/items",
		json={"sku": "KB-01", "name": "Keyboard", "price": 120, "quantity": 3},
	)
	assert create_res.status_code == 200
	assert create_res.json()["inventory_value"] == 360.0

	add_res = client.post("/items/KB-01/add-stock", json={"qty": 2})
	assert add_res.status_code == 200
	assert add_res.json() == {"sku": "KB-01", "quantity": 5}

	remove_res = client.post("/items/KB-01/remove-stock", json={"qty": 1})
	assert remove_res.status_code == 200
	assert remove_res.json() == {"sku": "KB-01", "quantity": 4}

	price_res = client.patch("/items/KB-01/price", json={"new_price": 150})
	assert price_res.status_code == 200
	assert price_res.json()["inventory_value"] == 600.0

	get_res = client.get("/items/KB-01")
	assert get_res.status_code == 200
	assert get_res.json()["inventory_value"] == 600.0


def test_inventory_remove_stock_invalid():
	client = TestClient(app)

	client.post(
		"/items",
		json={"sku": "KB-02", "name": "Keyboard", "price": 50, "quantity": 2},
	)
	res = client.post("/items/KB-02/remove-stock", json={"qty": 5})

	assert res.status_code == 400
	assert res.json() == {"detail": "not enough stock"}


def test_inventory_set_price_invalid():
	client = TestClient(app)

	client.post(
		"/items",
		json={"sku": "KB-03", "name": "Keyboard", "price": 50, "quantity": 10},
	)
	res = client.patch("/items/KB-03/price", json={"new_price": 0})

	assert res.status_code == 400
