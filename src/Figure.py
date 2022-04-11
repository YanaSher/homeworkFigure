# basic class
class Figure:

    def __init__(self, name, area, perimetr):
        self._name = name  # название фигуры
        self._area = area  # площадь
        self._perimetr = perimetr  # периметр(сумма длин сторон или длинна окружности)

    def get_name(self):
        return self._name

    def get_area(self):
        return self._area

    def get_perimetr(self):
        return self._perimetr

    def add_area(self, other_figure):
        if isinstance(other_figure, Figure):
            sum_areas = self._area + other_figure._area
            return sum_areas
        else:
            raise ValueError("Неправильная фигура")
