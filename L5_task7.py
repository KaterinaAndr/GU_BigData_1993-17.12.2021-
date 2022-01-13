"""
 7. Создать (не программно) текстовый файл, 
 в котором каждая строка должна содержать данные о фирме: название, форма собственности,
  выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, 
а также словарь со средней прибылью. 
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json

with open('task7_firms.txt', 'r', encoding="utf-8") as file, open('task7_new_json_from_py.json', 'w') as file_json:
    content = file.readlines()
    n_firms = len(content)
    firms_dict = {}
    average_profit_dict = {}
    result = []
    # print(content)
    for line in content:
        line.rstrip('\n')
        # print(line)
        firm, ooo, got, payed = line.split()
        one_firm_profit = int(int(got) - int(payed))
        all_profit = 0
        if one_firm_profit > 0:
            all_profit += one_firm_profit
        firms_dict[firm] = one_firm_profit
    result.append(firms_dict)
    all_profit_per_number = int(all_profit / n_firms)
    average_profit_dict['average_profit'] = all_profit_per_number
    result.append(average_profit_dict)
    print(result)
    json.dump(result, file_json)






