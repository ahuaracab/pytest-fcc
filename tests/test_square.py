import pytest
import source.shapes as shapes

array1 = [(5, 25), (4, 16), (9, 81)]
array2 = [(5, 20), (4, 16), (9, 36)]


@pytest.mark.parametrize("side_length, expected_area", array1)
def test_multiple_square_areas(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area


@pytest.mark.parametrize("side_length, expected_perimeter", array2)
def test_multiple_square_perimeters(side_length, expected_perimeter):
    assert shapes.Square(side_length).perimeter() == expected_perimeter
