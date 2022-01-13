"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import random

with open('task5_numbers.txt', 'w+') as numbers:
    count_num = random.randint(1, 10)
    while count_num < 20:
        a = f"{str(random.randint(1, 100))} "
        numbers.write(a)
        count_num += 1

with open('task5_numbers.txt', 'r+') as numbers:
    content = numbers.readlines()
    # print(content)
    # print(type(content))
    nums_int = []
    for el in content:
        b = el.split()
        # print(type(b))
        # print(b)

        for num in b:
            nums_int.append(int(num))
            # print(nums_int)
    print(sum(nums_int))

