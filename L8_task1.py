"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их
тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, input_date):
        self.input_date = input_date

    def to_int(self):
    # @classmethod
    # def to_int(cls):

        try:
            data_list = self.input_date.split('-')
            day = data_list[0]
            month = data_list[1]
            year = data_list[2]
            day_int = int(day)
            month_int = int(month)
            year_int = int(year)
            print(f'Введенная дата: {day_int} число {month_int} месяца {year_int} года.')
            return day_int, month_int, year_int
        except Exception:
            print('Неверные входящие данные')


    @staticmethod
    def valid_date(date_to_validate):
        try:
            day, month, year = date_to_validate
            if day not in range(1, 32):
                print('Неверно введена дата')
            elif month not in range(1, 13):
                print('Неверно введен месяц')
            elif year not in range(0, 2200):
                print('Неверно введен год')
        except Exception:
            print('Дата не прошла валидацию')


a = Date('10-10-2020')
# a = Date('90-10-2021')
# a = Date('9010-2021')
# a = Date('90-мм-2021')
date_to_validate = a.to_int()
a.valid_date(date_to_validate)
# print()

