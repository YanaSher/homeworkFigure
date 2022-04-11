import pytest
from src.Circle import Circle


def test_non_square():
    with pytest.raises(ValueError):  # проверяем, что выдаст ошибку при 0 значении
        Circle(radius=0)


def test_non_square2():
    with pytest.raises(ValueError):  # проверяем, что выдаст ошибку при отрицательном значении
        Circle(radius=-5)


def test_name(circle):
    assert Circle.get_name(circle) == 'Circle'


def test_area(circle):
    assert Circle.get_area(circle) == 78.54


def test_perimetr(circle):
    assert Circle.get_perimetr(circle) == 31.42


def test_area_circle_and_area_rectangle(circle, rectangle):
    assert circle.add_area(rectangle) == 108.54


def test_eror_sum_area(circle, string):
    with pytest.raises(ValueError):  # проверяем, что если фигура не определяется, то ошибка
        assert circle.add_area(string) == 103.54
