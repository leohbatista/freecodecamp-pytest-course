import time

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


@pytest.mark.slow
def test_very_slow():
    time.sleep(3)
    result = divide(10, 2)
    assert result == 5


@pytest.mark.skip(reason="Not implemented yet")
def test_not_implemented():
    assert False


@pytest.mark.xfail(reason="We know that this fails")
def test_divide_by_zero_xfail():
    divide(10, 0)
