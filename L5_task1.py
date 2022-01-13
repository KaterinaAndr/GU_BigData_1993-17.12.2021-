"""
1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""
with open('task1_text_from_you.txt', 'w') as file:
    input_str = None
    while input_str != 'n':
        input_str = input("Напиши мне что-нибудь, пожалуйста! Как надоест - нажми n!\n")
        line_str = f'{input_str}\n'
        file.write(line_str)



