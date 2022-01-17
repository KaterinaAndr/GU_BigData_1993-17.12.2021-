"""
3. Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}



class Position(Worker):
    def get_full_name(self):
        print(f'Фамилия и имя сотрудника: {self.surname} {self.name}, должность: {self.position}')

    def get_total_income(self):
        print(f'Доход сотрудника: {int(self._income.get("wage")) + int(self._income.get("bonus"))}')


ivanov = Position("Иванов", 'Сергей', 'менеджер', '123', '32')
ivanov.get_full_name()
ivanov.get_total_income()
