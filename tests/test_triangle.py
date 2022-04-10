import pytest
from src.Triangle import Triangle


def test_non_rectangle():
    with pytest.raises(ValueError):  # проверяем, что выдаст ошибку при 0 значении
        Triangle(0, 5, 6)
    with pytest.raises(ValueError):
        Triangle(5, 0, 6)
    with pytest.raises(ValueError):
        Triangle(4, 5, 0)


def test_non_rectangle2():
    with pytest.raises(ValueError):  # проверяем, что выдаст ошибку при отрицательном значении
        Triangle(-5, 6, 4)
    with pytest.raises(ValueError):
        Triangle(5, -6, 4)
    with pytest.raises(ValueError):
        Triangle(5, 6, -4)


def test_non_rectangle3():
    with pytest.raises(ValueError):  # проверяем, что выдаст ошибку если сума сторон меньше длинны стороны
        Triangle(1, 1, 4)
    with pytest.raises(ValueError):
        Triangle(1, 4, 1)
    with pytest.raises(ValueError):
        Triangle(4, 1, 1)


def test_name(triangle):
    assert Triangle.get_name(triangle) == 'Triangle'


def test_area(triangle):
    assert Triangle.get_area(triangle) == 11.62


def test_perimetr(triangle):
    assert Triangle.get_perimetr(triangle) == 18
