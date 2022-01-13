"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
with open('task3_selaries.txt', 'r', encoding='utf-8') as file:
    content = file.readlines()
    print(content)
    min_selarys = []
    for index, el in enumerate(content, 1):
        a = el.split()
        # print(a)
        while file.readline():
            for line in content:
                line = line.rstrip('\n') # no need?
                print(line)
            #     surname, salary = line.split(" ")  # problem!
            #     salary = float(salary)
            #     # print(salary, type(salary))
            #     if salary < 20000:
            #         min_selarys.append(surname)
            # print(min_selarys)
            # print(line)
            # print(type(salary))
            # salary.rstrip('\n')  # no need?

            # salary = float(salary)
            # print(salary, type(salary))
            # if salary < 20000:
            #     min_selarys.append(surname)
                # print(min_selarys)


        #
        # for line in content:
        #     # line = line.rstrip('\n') # no need?
        #     surname, salary = line.split(" ")  # problem!
        #
        #     # print(line)
        #     # print(type(salary))
        #     # salary.rstrip('\n')  # no need?
        #
        #     salary = float(salary)
        #     print(salary, type(salary))
        #     if salary < 20000:
        #         min_selarys.append(surname)
        #         # print(min_selarys)



    # for line in content:
    #     line = line.rstrip('\n')
    #     surname, salary = line.split(", ")
    #     print(salary)
    # for index, el in enumerate(content, 1):
    #     a = el.split()
    #     print(a)
    #     a_int = int(a[1])
    #     print(a)

        # if int(a[1]) < 20000:
        #     print(a[1])

        # print(type(el))



