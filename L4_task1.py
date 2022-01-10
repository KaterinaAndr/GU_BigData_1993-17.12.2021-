"""
1. Реализовать скрипт,
 в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
 В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
 Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
# python L4_task1.py 1 2 3

from sys import argv

name_of_script, hours, money_per_hour, bonus = argv
print('Имя скрипта:', name_of_script)
print('выработка в часах:', hours)
print('ставка в час:', money_per_hour)
print('премия:', bonus)
print('расчет заработной платы сотрудника:', (int(hours) * int(money_per_hour)) + int(bonus))






# def zp_culc_func(hours, money_per_hour, bonus):
#     # hours = int(input(('Введите выработку сотрудника в часах: ')))
#     # money_per_hour = int(input(('Введите ставку сотрудника в час: ')))
#     # bonus = int(input(('Введите премию сотрудника: ')))
#     zp_culc = (hours * money_per_hour) + bonus
#     return zp_culc
#
#
# a = zp_culc_func()
# print(a)