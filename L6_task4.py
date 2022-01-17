"""
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
 о превышении скорости.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.color} {self.name} поехала со скоростью {self.speed}')

    def stop(self):
        print(f'Машина {self.color} {self.name} остановилась со скорости {self.speed}')

    def turn(self, direction):
        self.direction = direction
        print(f'Машина {self.color} {self.name} повернула {self.direction} на скорости {self.speed}')

    def show_speed(self, current_speed):
        self.current_speed = current_speed
        print(f'Текущая скорость автомобиля = {current_speed}')


class TownCar(Car):

    def show_speed(self, current_speed):
        self.current_speed = current_speed
        if self.current_speed > 60:
        # if int(self.current_speed) > 60:
            print(f'Превышение скорости!')
        else:
            print(f'Текущая скорость автомобиля = {current_speed}')


class SportCar(Car):
    # def __init__(self, speed, color, name, is_police, n_horses):
    #     super().__init__(self, speed, color, name, is_police)
    #     self.n_horses = n_horses

    def power(self, n_horses):
        self.n_horses = n_horses
        if self.is_police == True:
            print(f'Не может быть!')
        elif n_horses > 500:
            print(f'У Вас очень мощная мащина, водите очень аккуратно!')
        else:
            print(f'У Вас мощная мащина, водите аккуратно)')


class WorkCar(Car):
    def show_speed(self, current_speed):
        self.current_speed = current_speed
        if self.current_speed > 40:
            print(f'Превышение скорости!')
        else:
            print(f'Текущая скорость автомобиля = {current_speed}')


class PoliceCar(Car):

    def power(self, n_horses):
        self.n_horses = n_horses
        if self.n_horses > 500:
            print(f'У Вас очень мощная мащина, в погоне Вам нет равных')
        else:
            print(f'Главное правильная тактика')




a = Car(50, 'red', 'ford', False)
a.go()
a.stop()
a.turn('налево')
a.show_speed(78)
print()

b = TownCar(40, "blue", "Kia", False)
b.go()
b.stop()
b.turn('направо')
b.show_speed(78)
b.show_speed(50)
print()

c = SportCar(80, "yellow", "Camaro", False)
c.go()
c.stop()
c.turn('налево')
c.show_speed(150)
c.power(400)
c.power(550)
print()
d = SportCar(80, "yellow", "Camaro", True)
d.power(400)
print()

e = WorkCar(50, 'gray', 'toyota', False)
e.go()
e.stop()
e.turn('направо')
e.show_speed(30)
e.show_speed(50)
print()

f = PoliceCar(50, 'white', 'ford', True)
f.go()
f.stop()
f.turn('направо')
f.show_speed(50)
f.power(300)
f.power(550)
print()
