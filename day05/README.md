# Day 5: Bank Account & Inventory Management

## Today I built two classes and exposed them as a REST API

1. BankAccount class with deposit/withdraw logic and validation
2. InventoryItem class with stock and price management
3. FastAPI endpoints to interact with both using in-memory stores

This is the first day where business logic lives inside classes, and HTTP routes just call those methods. A big step up from utility functions.

## Problems Solved

### 1) BankAccount Class

**What it does:** Manages a bank account with balance tracking.

**Constructor validation:**
- `account_number` must be a string
- `owner_name` must be a string
- `balance` must be a number (int or float)
- `balance` cannot be negative

**Methods:**
- `deposit(amount)`: Adds to balance, validates amount > 0, returns new balance
- `withdraw(amount)`: Subtracts from balance, validates amount > 0, checks sufficient funds, returns new balance
- `get_balance()`: Returns current balance

**Class invariant:** `_balance` is always >= 0 (maintained by constructor and withdraw validation).

### 2) InventoryItem Class

**What it does:** Manages stock and pricing for a product.

**Constructor validation:**
- `sku` is a string
- `name` is a string
- `price` must be a number and > 0
- `quantity` must be an integer and >= 0

**Methods:**
- `add_stock(qty)`: Adds qty to quantity, validates qty > 0, returns new quantity
- `remove_stock(qty)`: Subtracts qty, validates qty > 0, checks quantity available, returns new quantity
- `set_price(new_price)`: Updates price, validates new_price > 0, returns new price
- `inventory_value()`: Returns price * quantity

**Class invariant:** `_price` > 0 and `_quantity` >= 0 (maintained by validation in constructor and methods).

## Input Rejection Strategy

**Type errors (TypeError):**
- Wrong data type passed (e.g., string for balance, float for qty)
- Always rejected at method entry

**Value errors (ValueError):**
- Invalid semantic value (e.g., negative balance, zero price, qty > stock)
- Always rejected at method entry
- State does not change if validation fails

**Duplicate creation:**
- Duplicate account_number or SKU in store returns HTTP 400 "already exists"

## API Error Strategy

**400 (Bad Request):**
- Type validation failed
- Value validation failed
- Business rule violation (insufficient funds, not enough stock)
- Duplicate resource attempted

**404 (Not Found):**
- Account or SKU does not exist in store
- GET on non-existent resource
- POST action on non-existent resource (e.g., deposit to non-existent account)

**200 (Success):**
- All validation passed
- State was successfully updated
- Response includes the current state after operation

## API Endpoints

### Bank
- `POST /accounts` - Create account
- `POST /accounts/{account_number}/deposit` - Add money
- `POST /accounts/{account_number}/withdraw` - Remove money
- `GET /accounts/{account_number}` - View account

### Inventory
- `POST /items` - Create item
- `POST /items/{sku}/add-stock` - Increase stock
- `POST /items/{sku}/remove-stock` - Decrease stock
- `PATCH /items/{sku}/price` - Update price
- `GET /items/{sku}` - View item

## Key Design Decision: Business Logic in Classes

The class methods handle all validation and state changes. The API routes are thin shells that:
1. Extract request data
2. Call the class method
3. Catch any exceptions and map them to HTTP codes
4. Return the result

This keeps business rules in one place and makes them testable independently of HTTP.

## Day 6 Refactor Plan

Add a `get_price()` and `get_quantity()` accessor methods to InventoryItem instead of exposing `_price` and `_quantity` directly in API responses. This follows proper encapsulation and makes future changes to internal storage easier.

## Complexity

### BankAccount Methods
- All methods: O(1) - Direct arithmetic and field access

### InventoryItem Methods
- All methods: O(1) - Direct arithmetic, comparison, field access

### API In-Memory Store
- Create: O(1) - Dictionary insertion
- Get: O(1) - Dictionary lookup
- Update: O(1) - Dictionary update and method call

Total for all endpoints in current setup: O(1) per request.

## Test Run Status

All 6 Day 5 tests passed via pytest with FastAPI TestClient:
- Bank flow with deposit and withdraw
- Bank insufficient funds error
- Inventory flow with stock and price changes
- Inventory validation errors

## Mistakes Log & Learnings

1. Initially exposed `_price` and `_quantity` directly in API responses. Realized this breaks encapsulation and makes it easy to have inconsistent state later.
2. Started with `balance < 0` validation but realized `balance <= 0` is stricter and follows the invariant better for edge cases.
3. First version forgot to check for duplicate SKU on create. Added validation after realizing the test expected 400 on duplicate attempts.
4. Learned that catching exceptions at the API layer and converting them to HTTP codes is the right pattern, not duplicating validation logic in routes.

## Reflection

Today felt like proper software engineering. Classes contain domain logic, exceptions encode business rules, and the API is just a translation layer. This pattern scales well and makes tests simple because you test class behavior and endpoint behavior separately.

The key insight: validation failures should never leave the object in a partially-modified state. All checks happen first, then state changes happen. This makes the system reliable.
