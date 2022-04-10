from src.Figure import Figure


class Sguare(Figure):
    def __init__(self, side):
        if side <= 0:
            raise ValueError("Такой фигуры несуществует")
        self._side = side
        self._name = 'Square'
        self._area = round(self._side ** 2, 2)
        self._perimetr = round(4 * self._side, 2)
