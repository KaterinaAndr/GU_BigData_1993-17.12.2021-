"""
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы
для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def fabric(self):
        pass


class Costume(Clothes):

    def __init__(self, h, n):
        self.h = h  # рост
        self.n = n  # количество шт

    @property
    def fabric(self):
        fabric_count = (2 * self.h + 0.3) / 100 * self.n
        return f"Для пошива {self.n} шт. брюк на рост {self.h}см необходимо {fabric_count:.3f} м. ткани"


class Coat(Clothes):

    def __init__(self, v, n):
        self.v = v  # размер
        self.n = n  # количество шт

    @property
    def fabric(self):
        fabric_count = (self.v / 6.5 + 0.5) * self.n # формула дает странный результат
        return f"Для пошива {self.n} шт. пальто {self.v} размера необходимо {fabric_count:.3f} м. ткани"


costume = Costume(165, 1)
print(costume.fabric)
print()
coat = Coat(65, 1)
print(coat.fabric)
print()
coat = Coat(46, 1)
print(coat.fabric)
print()
costume = Costume(187, 4)
print(costume.fabric)
print()
coat = Coat(7, 1)
print(coat.fabric)
print()
