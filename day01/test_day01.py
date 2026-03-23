from fizzbuzz_variant import fizzbuzz_variant


def test_fizzbuzz():
    assert fizzbuzz_variant(3)=="Fizz"
    assert fizzbuzz_variant(5)=="Buzz"
    assert fizzbuzz_variant(15)=="FizzBuzz"
    assert fizzbuzz_variant(3)=="Fizz"
    assert fizzbuzz_variant(3)=="Fizz"
    assert fizzbuzz_variant(3)=="Fizz"
   # Edge Cases
    assert fizzbuzz_variant(1) == "1"
    assert fizzbuzz_variant(0) == "FizzBuzz" 
    print("✅ All FizzBuzz tests passed!")

test_fizzbuzz()