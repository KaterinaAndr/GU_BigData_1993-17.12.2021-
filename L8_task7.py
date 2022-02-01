"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
 Реализуйте перегрузку методов сложения и умножения комплексных чисел.
 Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
 выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного
 результата.
"""
import math


class ComplexNums:
    def __init__(self, a, b):
        self.a, self.b = a, b
        # self.c, self.d = c, d

    def __add__(self, other):
        return f"Сложение: {ComplexNums(self.a + other.a, self.b + other.b)}"

    def __mul__(self, other):
        return f"Умножение: {ComplexNums(self.a * other.a - self.b * other.b, self.a * other.b - self.b * other.a)}"

    def __str__(self):
        return f"{self.a} + {self.b}j"


num1 = ComplexNums(1, 2)
num2 = ComplexNums(3, 5)
print(num1 + num2)
print(num1 * num2)

