import pytest
from src.Rectangle import Rectangle


def test_non_rectangle():
    with pytest.raises(ValueError):  # проверяем, что выдаст ошибку при 0 значении
        Rectangle(0, 5)
    with pytest.raises(ValueError):
        Rectangle(5, 0)


def test_non_rectangle2():
    with pytest.raises(ValueError):  # проверяем, что выдаст ошибку при отрицательном значении
        Rectangle(-5, 6)
    with pytest.raises(ValueError):
        Rectangle(5, -6)


def test_name(rectangle):
    assert Rectangle.get_name(rectangle) == 'Rectangle'


def test_area(rectangle):
    assert Rectangle.get_area(rectangle) == 30


def test_perimetr(rectangle):
    assert Rectangle.get_perimetr(rectangle) == 22
