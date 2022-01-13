"""
6. Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


with open('task6_subjects_and_hours.txt', 'r') as file:
    content = file.readlines()
    # print(content)
    subj_dict = {}
    for line in content:
        line = line.rstrip('\n')
        # print(line)
        subject, hours = line.split(': ')  # ну почему ошибка-то?
        # print(subject)
        # print(hours)
        hours_str_list = hours.split()
        # print(hours_str_list)
        hours_int_list = []
        for el in hours_str_list:
            # print(type(el))
            if el.endswith("(л)"):
                hours_int_list.append(int(el[:-3]))
                # print(hours_int_list)
            elif el.endswith("(пр)"):
                hours_int_list.append(int(el[:-4]))
                # print(hours_int_list)
            elif el.endswith("(лаб)"):
                hours_int_list.append(int(el[:-5]))
                # print(hours_int_list)
            sum_hours = sum(hours_int_list)
            subj_dict[subject] = sum_hours
    print(subj_dict)





