from fizzbuzz_variant import fizzbuzz_variant
from grade_classifier import grade_classifier

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


def test_grade_classifier():
    assert grade_classifier(100)=="A"
    assert grade_classifier(89.4)=="B"
    assert grade_classifier(89.5)=="A"
    assert grade_classifier(79)=="C"
    assert grade_classifier(70)=="C"
    assert grade_classifier(69)=="D"
    assert grade_classifier(10)=="F"
    print("✅ All grade_classifier tests Passed!")

test_grade_classifier()