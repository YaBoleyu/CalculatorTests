import pytest
from calculator import divide,add,subtract,multiply


def test_add():
    assert add(2,3) == 5


def test_add_negative():
    assert add(2, -5) == -3


def test_add_invalid():
    with pytest.raises(TypeError):
        assert add(2, "a")  # should be TypeError error


def test_add_none():
    with pytest.raises(TypeError):
        assert add(2, None)  # should be TypeError error


def test_add_array():
    with pytest.raises(TypeError):
        assert add(2, [1, 2, 3])  # should be TypeError error


def test_add_reversed():
    assert add(2,3) == add(3,2)


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(2, 3) == 6


def test_multiply_zero():
    assert multiply(2, 0) == 0


def test_multiply_negative():
    assert multiply(2, -3) == -6


def test_multiply_float():
    assert multiply(2, 1.5) == 3.0


def test_divide():
    assert divide(6, 3) == 2


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(6, 0)