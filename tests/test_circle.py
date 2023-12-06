import math

import source.shapes as shapes


class TestCircle:
    def setup_method(self, method):
        print(f"setup_method for {method.__name__}")
        self.circle = shapes.Circle(10)

    def teardown_method(self, method):
        print(f"teardown_method for {method.__name__}")
        del self.circle

    def test_radius(self):
        assert self.circle.radius == 10

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius**2

    def test_perimeter(self):
        assert self.circle.perimeter() == 2 * math.pi * self.circle.radius
