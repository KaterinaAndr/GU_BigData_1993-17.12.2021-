"""
1. Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
 третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке
 (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов.
При его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
from itertools import cycle
from time import sleep

class TrafficLight:
    colors = ('красный', 'жёлтый', 'зелёный')
    time = (7, 2, 4)
    color_time = {'красный': 7, 'жёлтый': 2, 'зелёный': 4}

    def __init__(self, color):
        self.__color = color

    def running(self):
        lights_change = cycle(self.colors)
        for color in lights_change:
            if self.__color == color:
                print(color)
                sleep(self.color_time.get(color))
                self.__color = next(lights_change)

a = TrafficLight('красный')
a.running()





# colors = ('красный', 'жёлтый', 'зелёный')
# time = (7, 2, 4)
# color_time = {}
# for col, t in zip(colors, time):
#     color_time[col] = t
#     color_time.update(color_time)
# print(color_time)


