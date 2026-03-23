def fizzbuzz_variant(n: int) -> str:
    """Returns a combination of Fizz, Buzz based on divisibility."""
    if not isinstance(n, int):
        raise TypeError("Only integer is allowed as valid input")
    result = ""
    if n % 3 == 0:
        result += "Fizz"
    if n % 5 == 0:
        result += "Buzz"
    if n%7 ==0: 
        result += "Pop"
    return result if result else str(n)

if __name__ == "__main__":
    print(fizzbuzz_variant(3))
    print(fizzbuzz_variant(5))
    print(fizzbuzz_variant(14))
    print(fizzbuzz_variant(15))
    print(fizzbuzz_variant(105))
    print(fizzbuzz_variant(17))
