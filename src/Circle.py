from src.Figure import Figure
import math


class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Такой фигуры несуществует")
        self._radius = radius
        self._name = 'Circle'
        self._area = round(math.pi * (self._radius ** 2), 2)
        self._perimetr = round(2 * math.pi * self._radius, 2)
