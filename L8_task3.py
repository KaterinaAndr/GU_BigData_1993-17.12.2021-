"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка
на наличие только чисел. Проверить работу исключения на реальном примере.
Запрашивать у пользователя данные и заполнять список необходимо только числами.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь
сам не остановит работу скрипта, введя, например, команду «stop». При этом скрипт завершается,
сформированный список с числами выводится на экран.
Подсказка: для этого задания примем, что пользователь может вводить только числа и строки.
Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента.
Вносить его в список, только если введено число. Класс-исключение должен не позволить пользователю
ввести текст (не число) и отобразить соответствующее сообщение. При этом работа скрипта
не должна завершаться.
"""
# a = input("Введите число (для остановки ввода введите «stop»): ")


class MyErr(Exception):

    def __init__(self):
        self.msg = "Вы ввели не число"


a = 0
nums_list = []
while a != 'stop':
    try:
        a = int(a)
        if a == int(a):
            nums_list.append(a)
        else:
            raise MyErr
    except Exception:
        print("Эта ошибка проходит")  # почему просто не переходит на "except MyErr as err:"
        # почему нужно это дополнительное исключение?
    except MyErr as err:
        print(err.msg, 1)  # 1 это метка для отслеживания

    a = input("Введите число (для остановки ввода введите «stop»): ")


print(nums_list)
