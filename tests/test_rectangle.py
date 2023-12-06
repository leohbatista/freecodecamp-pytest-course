import source.shapes as shapes


def test_eq(rectangle):
    assert rectangle == shapes.Rectangle(5, 10)


def test_not_eq_rectangle(rectangle, rectangle2):
    assert rectangle != rectangle2


def test_not_eq_other_shape(rectangle):
    assert rectangle != shapes.Circle(10)


def test_area(rectangle):
    assert rectangle.area() == 50


def test_perimeter(rectangle):
    assert rectangle.perimeter() == 30
