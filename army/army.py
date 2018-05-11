""" Created by Vladimir Goncharov, 13.04.2018"""

# import sys
# from gondorunitfactory import GondorUnitFactory
# from izengardunitfactory import IzengardUnitFactory
from collections import defaultdict
# sys.path.append('.home/elevely/tp/python/unitfactory')

max_morale = 2.25
max_number_of_steps = 70  


class Army(object):
    """docstring for Army"""

    def __init__(self, uf, name_army, owner=None, morale=1, number_of_steps=1, mobilized=False):
        self.squads = []
        self.uf = uf
        self.name_army = name_army
        self.mobilized = mobilized
        self.owner = owner
        self.morale = morale
        self.number_of_steps = number_of_steps

    def hire(self, squad_index, _type, _quantity=1):
        # if squad_index == 0:
        #     self.squads.append([])
        #     squad_index = len(self.squads) - 1
        if _type in self.available_unit:
            for i in range(_quantity):
                self.squads[squad_index].append(self.uf.create_unit(_type))
            if _quantity == 1:
                print("New {} is created".format(_type))
            else:
                print("{} new units with type {} are created".format(
                    _quantity, _type))
        else:
            print("incorrect input on data: _type = {}".format(_type))

    def count_attack(self):
        sum_attack = 0
        for squad in self.squads:
            for concrete_unit in squad:
                sum_attack += concrete_unit.get_attack()
        return sum_attack

    def count_defence(self):
        sum_defence = 0
        for squad in self.squads:
            for concrete_unit in squad:
                sum_defence += concrete_unit.get_defence()
        return sum_defence

    def set_morale(self, value):
        self.morale = value

    def set_number_of_steps(self, value):
        self.number_of_steps = value

    def show_squad(self, index_squad):
        try:
            squad = self.squads[index_squad]
        except:
            self.squads.append([])
            squad = self.squads[len(self.squads) - 1]
        print("Сейчас в отряде находятся: ")
        unit_dict = defaultdict(int)
        for unit in squad:
            print(unit)
            unit_dict[unit.type] += 1
        for unit_types in unit_dict:
            print("--> Количество: {}. Тип: {}".format(unit_dict[unit_types], unit_types))

# отладить вывод типа в показа отряда 