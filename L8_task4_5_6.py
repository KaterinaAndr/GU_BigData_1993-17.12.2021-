"""
   4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
    5. Продолжить работу над первым заданием.
Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое
подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру (например, словарь).
    6. Продолжить работу над вторым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать
строковый тип данных.
"""
# equipment_dict =           {printer: {'HP': {"model": "Lazer_Jet-17", "count": 15}},
#                          notebook: {'Lenovo': {'model': 'Lv-18', "count": 10}}}
# equipment_dict = {"equipment_type": {'name': {'model': model, "count": count}}}


class Storage:
    equipment_dict = {}

    @classmethod
    def storage_to(cls, eq_type, name, model, count):
        equipment_type = cls.equipment_dict.get(eq_type) # проверить наличие notebook
        if equipment_type:  # если да, то  (это значение {'Lenovo': {'model': 'Lv-18', "count": 10}} по ключу 'notebook'
            if equipment_type.get(name):   # проверить наличие 'Lenovo' если да, то
                name_dict = equipment_type.get(name)  # это значение {'model': 'Lv-18', "count": 10} по ключу 'Lenovo'
                if name_dict.get(model):  # проверить наличие в 'Lenovo' model 'Lv-18' если да, то
                    current_count = name_dict.setdefault("count") + count   # кол-во: было + добавлено
                    name_dict.update({"count": current_count})  # кол-во: перезаписано
                else:  # если нет то
                    name_dict.update({'model': model, "count": count})  # добавить модель и кол-во к 'Lenovo'
            else:  # если нет то
                equipment_type.update({name: {'model': model, "count": count}}) # добавить {'Lenovo': модель и кол-во} к notebook ЭТО ДУБЛИРУЕТ СТРОКУ НИЖЕ?
        # else:
        #     cls.equipment_dict[eq_type] = {'name': {'model': model, "count": count}}
        # return cls.equipment_dict
        cls.equipment_dict[eq_type] = {'name': {'model': model, "count": count}}

    @classmethod
    def storage_from(cls, eq_type, name, model, count):
        pass


class OfficeEquip:
    def __init__(self, eq_type, name, model, count):
        self.eq_type = eq_type
        self.name = name
        self.model = model
        self.count = count
# в этом месте я сообразила как принять экземпляр коасса н-р Принтер
# и "отправить на склад" в equipment_dict = {}

class Printer(OfficeEquip):
    def __init__(self, eq_type, name, model, count, colour):
        super().__init__(eq_type, name, model, count)
        self.colour = colour



class PC(OfficeEquip):
    def __init__(self, eq_type, name, model, count, n_proc_core, n_gb_ram):
        super().__init__(eq_type, name, model, count)
        self.n_proc_core = n_proc_core
        self.n_gb_ram = n_gb_ram


class Cooler(OfficeEquip):
    def __init__(self, eq_type, name, model, count, type_water):
        super().__init__(eq_type, name, model, count)
        self.type_water = type_water


printer1 = Printer('printer', 'HP', "Lazer_Jet-17", 10, "black")

# print()


