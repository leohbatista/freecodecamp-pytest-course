import pytest

from source.my_functions import add, divide


def test_add():
    result = add(2, 3)
    assert result == 5


def test_add_strings():
    result = add("hello", "world")
    assert result == "helloworld"


def test_divide():
    result = divide(10, 2)
    assert result == 5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
