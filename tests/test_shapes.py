import pytest

from source.shapes import Shape


def test_perimeter_not_implemented():
    with pytest.raises(NotImplementedError):
        Shape().perimeter()


def test_area_not_implemented():
    with pytest.raises(NotImplementedError):
        Shape().area()
