import pytest
from factorial import factorial


def test_factorial_of_zero():
    assert factorial(0) == 1


def test_factorial_of_five():
    assert factorial(5) == 120


def test_factorial_of_ten():
    assert factorial(10) == 3628800


def test_negative_number():
    with pytest.raises(ValueError):
        factorial(-1)
