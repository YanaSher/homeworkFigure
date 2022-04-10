import pytest
from src.Circle import Circle



def test_non_square():
    with pytest.raises(ValueError):  # проверяем, что выдаст ошибку при 0 значении
        Circle(radius=0)


def test_non_square2():
    with pytest.raises(ValueError):  # проверяем, что выдаст ошибку при отрицательном значении
        Circle(radius=-5)


def test_name(circle):
    assert Circle.get_name(circle) == 'Square'

def test_area(circle):
    assert Circle.get_area(circle) == 78.54

def test_perimetr(circle):
    assert Circle.get_perimetr(circle) == 31.42
