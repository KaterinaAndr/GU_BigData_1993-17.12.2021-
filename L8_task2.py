"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой.
"""


class ZeroDivErr(Exception):
    def __init__(self):
        self.msg = "Попытка деления на ноль!"

a = input("Разделим число a на b. Введите а: ")
b = input("теперь b: ")

try:
    a = int(a)
    b = int(b)
    if b == 0:
        raise ZeroDivErr
except ValueError:
    print('Вы ввели не число')
except ZeroDivErr as err:
    print(err.msg)
else:
    print(f"Результат деления {a} на {b} = {a/b}")



