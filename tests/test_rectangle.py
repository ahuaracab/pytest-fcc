def test_area(my_rectangle):
    result = my_rectangle.area()
    expected = 10 * 20
    assert result == expected


def test_perimeter(my_rectangle):
    result = my_rectangle.perimeter()
    expected = 2 * (10 + 20)
    assert result == expected


def test_not_equal(my_rectangle, weird_rectangle):
    assert my_rectangle != weird_rectangle

