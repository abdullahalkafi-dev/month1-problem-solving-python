def factorial_loop(n: int) -> int:
    """Its take an integer and returns its factorial.
    Its uses loop to calculate factorial.
    """
    if not isinstance(n, int):
        raise TypeError("Only Int allowed. ")
    if n < 0:
        raise ValueError("Input can not less than 0")
    if n == 0 or n == 1:
        return 1
    temp = 1
    for i in range(2, n + 1):
        temp = temp * i

    return temp


def factorial_recursion(n: int) -> int:
    """Its take an integer and returns its factorial.
    Its uses recursion to calculate factorial.
    """
    if not isinstance(n, int):
        raise TypeError("Only Int allowed. ")
    if n < 0:
        raise ValueError("Input can not less than 0")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursion(n - 1)


if __name__ == "__main__":
    print(factorial_recursion(5))
    print(factorial_loop(6))
