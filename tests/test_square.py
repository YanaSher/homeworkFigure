import pytest
from src.Square import Sguare


def test_non_square():
    with pytest.raises(ValueError):  # проверяем, что выдаст ошибку при 0 значении
        Sguare(side=0)


def test_non_square2():
    with pytest.raises(ValueError):  # проверяем, что выдаст ошибку при отрицательном значении
        Sguare(side=-5)


def test_name(square):
    assert Sguare.get_name(square) == 'Square'


def test_area(square):
    assert Sguare.get_area(square) == 25


def test_perimetr(square):
    assert Sguare.get_perimetr(square) == 20


def test_area_square_and_area_circle(square, circle):
    assert square.add_area(circle) == 103.54


def test_eror_sum_area(square, string):
    with pytest.raises(ValueError):  # проверяем, что если фигура не определяется, то ошибка
        assert square.add_area(string) == 103.54
