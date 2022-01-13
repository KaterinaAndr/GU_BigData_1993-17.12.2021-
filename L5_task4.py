"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

with open('task4_one-1.txt', 'r') as file_eng, open('task4_raz-1.txt', "w+") as file_rus:
    content = file_eng.readlines()
    # print(content)
    eng_rus = {'One': "Один", "Two": 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    for index, el in enumerate(content, 1):
        a = el.split(' — ')
        # print(a)
        # print(a[0])
        if a[0] in eng_rus.keys():
            # print(1)
            a[0] = eng_rus.get(a[0])
            # print(a)
            new_a = ' — '.join(a)
            print(new_a)  # не пойму как убрать лишние переносы у принта
            file_rus.writelines(new_a)
            # print(new_a, file=file_rus)  # даст дополнительные пустые строки, как убрать не понимаю

