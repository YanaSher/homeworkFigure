from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Такой фигуры несуществует")
        self._side_a = side_a
        self._side_b = side_b
        self._name = 'Rectangle'
        self._area = round(self._side_a * self._side_b, 2)
        self._perimetr = round(2 * (self._side_a + self._side_b), 2)
