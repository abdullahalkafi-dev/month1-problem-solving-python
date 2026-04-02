def normalize_amount(amount: float) -> float:
    if not isinstance(amount, (float, int)):
        raise TypeError("amount data type not allowed")
    if amount < 0:
        raise ValueError("amount must be grater than 0")
    return amount


if __name__ == "__main__":
    print(normalize_amount(50))
    print(normalize_amount(0))
    print(normalize_amount("20"))
    print(normalize_amount(-10))
