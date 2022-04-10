# в этом файле распологаются фикстуры, чтобы не дублировать их по тестам
import pytest
from src.Square import Sguare
from src.Rectangle import Rectangle
from src.Triangle import Triangle
from src.Circle import Circle


@pytest.fixture()
def square():
    return Sguare(5)


@pytest.fixture()
def rectangle():
    return Rectangle(5, 6)


@pytest.fixture()
def triangle():
    return Triangle(4, 6, 8)


@pytest.fixture()
def circle():
    return Circle(5)
