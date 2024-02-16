import math
import source.shapes as shapes


class TestCircle:

    def setup_method(self, method):
        print(f"Setting up {method}")
        self.my_circle = shapes.Circle(10)

    def teardown_method(self, method):
        print(f"Tearing up {method}")
        del self.my_circle

    def test_area(self):
        result = self.my_circle.area()
        expected = math.pi * 10 ** 2
        assert result == expected

    def test_perimeter(self):
        result = self.my_circle.perimeter()
        expected = 2 * math.pi * 10
        assert result == expected

    def test_not_same_area_rectangle(self, my_rectangle):
        assert self.my_circle.area() != my_rectangle.area()

