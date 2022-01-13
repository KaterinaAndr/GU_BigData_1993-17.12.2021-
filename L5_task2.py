"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open('task2_text.txt', 'r') as file:
    content = file.readlines()
    print(content)
    for index, el in enumerate(content, 1):
        a = el.split()
        print(f'В строке №{index} слов: {len(a)} ')


