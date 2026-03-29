def is_even(n: int):
    """Takes in integer. Return True if integer is even, False if odd"""
    if not isinstance(n, int):
        raise TypeError("Only Integer is allow")
    return n % 2 == 0


if __name__ == "__main__":
    print(is_even(0))
    print(is_even(2))
    print(is_even(3))
