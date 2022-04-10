from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Такой фигуры несуществует")
        elif (side_a + side_b) < side_c or (side_a + side_c) < side_b or (side_c + side_b) < side_a:
            raise ValueError("Такого треугольника не существует")
        self._side_a = side_a
        self._side_b = side_b
        self._side_c = side_c
        #   self._polyperimetr = round((self._side_a + self._side_b + self._side_c) / 2, 2)
        self._name = 'Triangle'
        self._area = round((self.polp * ((self.polp - self._side_a) * (self.polp - self._side_b) * (self.polp - self._side_c))) ** 0.5, 2)
        self._perimetr = round(self._side_a + self._side_b + self._side_c, 2)

    @property
    def polp(self):
        return (self._side_a + self._side_b + self._side_c) / 2  # вычисляем полупериметр
