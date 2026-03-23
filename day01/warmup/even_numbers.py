def print_even(limit: int) -> None:
    """It takes an int as limit And print the evens from 0  to that limit."""
    if not isinstance(limit, int):
        raise TypeError("Only integer is allowed as valid limit")
    for n in range(0, limit + 1, 2):
        print(n)


if __name__ == "__main__":
    print_even(10)
