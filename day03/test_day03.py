import pytest
from factorial import factorial_loop, factorial_recursion
from palindrome_checker import palindrome_checker, palindrome_checker_slice


def test_factorial_values():
    assert factorial_recursion(5) == 120
    assert factorial_loop(5) == 120
    assert factorial_loop(0) == 1
    assert factorial_recursion(1) == 1


def test_factorial_type_error():
    with pytest.raises(TypeError):
        factorial_loop("5")
    with pytest.raises(TypeError):
        factorial_recursion(5.5)


def test_factorial_value_error():
    with pytest.raises(ValueError):
        factorial_loop(-1)
    with pytest.raises(ValueError):
        factorial_recursion(-5)


def test_palindrome_values():
    assert palindrome_checker("madam") is True
    assert palindrome_checker_slice("radar") is True
    assert palindrome_checker("") is True
    assert palindrome_checker_slice("Step on no pets") is True 


def test_palindrome_negative():
    assert palindrome_checker("python") is False
    assert palindrome_checker_slice("hello") is False


def test_palindrome_case_sensitivity():
    assert palindrome_checker("MaDaM") is True
    assert palindrome_checker_slice("nOOn") is True


def test_palindrome_errors():
    with pytest.raises(TypeError):
        palindrome_checker(121)
    with pytest.raises(TypeError):
        palindrome_checker_slice(None)
