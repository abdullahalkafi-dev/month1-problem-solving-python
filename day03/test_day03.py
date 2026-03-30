import pytest
from factorial import factorial_loop, factorial_recursion


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
