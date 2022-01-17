"""
2. Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
 толщиной в 1 см*число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        print(f'Длина дороги = {self._length} (метров), ширина дороги = {self._width} (метров)')

    def mass_culc(self, mass_per_sqmetr, thickness):
        self.mass_per_sqmetr = mass_per_sqmetr
        self.thickness = thickness
        self.mass_result = self._length * self._width * self.mass_per_sqmetr * self.thickness
        print(f'Масса асфальта, необходимого для покрытия всей дороги = {int(self.mass_result / 1000)} тонн.')


road1 = Road(5000, 20)
road1.mass_culc(25, 5)

print()
road2 = Road(10000, 25)
road2.mass_culc(200, 10)