from fizzbuzz_variant import fizzbuzz_variant


def test_fizzbuzz():
    assert fizzbuzz_variant(3) == "Fizz"
    assert fizzbuzz_variant(5) == "Buzz"
    assert fizzbuzz_variant(14) == "Pop"
    assert fizzbuzz_variant(15) == "FizzBuzz"
    assert fizzbuzz_variant(105) == "FizzBuzzPop"
    # Edge Cases
    assert fizzbuzz_variant(1) == "1"
    assert fizzbuzz_variant(0) == "FizzBuzzPop"
    print("✅ All FizzBuzz tests passed!")


test_fizzbuzz()
