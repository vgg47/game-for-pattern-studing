""" Created by Vladimir Goncharov, 13.04.2018"""

import sys
# from gondorunitfactory import GondorUnitFactory
# from izengardunitfactory import IzengardUnitFactory
sys.path.append('./unit')
from collections import defaultdict
from unit import Unit
import data 
# sys.path.append('.home/elevely/tp/python/unitfactory')


class Army(object):
    """docstring for Army"""

    def __init__(self, uf, name_army, owner=None, morale=1,
                 number_of_steps=1, mobilized=False):
        self.squads = []
        self.uf = uf
        self.name_army = name_army
        self.mobilized = mobilized
        self.owner = owner
        self.morale = morale
        self.number_of_steps = number_of_steps

    def hire(self, squad_index, _type, _quantity=1):
        if squad_index == 0:
            self.squads.append([])
            squad_index = len(self.squads) - 1
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

    def count_army_attack(self):
        sum_attack = 0
        for squad in self.squads:
            for concrete_unit in squad:
                sum_attack += concrete_unit.get_attack()
        return sum_attack

    def count_army_defence(self):
        sum_defence = 0
        for squad in self.squads:
            for concrete_unit in squad:
                sum_defence += concrete_unit.get_defence()
        return sum_defence

    def count_squad_attack(squad):
        sum_attack = 0
        for concrete_unit in squad:
            sum_attack += concrete_unit.get_attack()
        return sum_attack

    def count_squad_defence(self):
        sum_defence = 0
        for concrete_unit in squad:
            sum_defence += concrete_unit.get_defence()
        return sum_defence

    def count_squad_health(self):
        sum_health = 0
        for concrete_unit in squad:
            sum_health += concrete_unit.get_health()
        return sum_health

    def count_squad_potential(squad):
        return count_squad_attack(squad) + count_squad_defence(squad)\
            + count_squad_health(squad)

    def is_alive(self):
        for squad in self.squads:
            for unit in squad:
                if unit.health > 0:
                    return True
        return False

    def set_morale(self, value):
        self.morale = value

    def set_number_of_steps(self, value):
        self.number_of_steps = value

    def show_squads(self):
        for i in range(len(self.squads)):
            print("{}:\n   Суммарные атака: {}; защита: {}; здоровье: {}\n."
                  .format(i + 1, count_squad_attack(self.squads[i]),
                          count_squad_defence(self.squads[i]),
                          count_squad_health(self.squads[i])))

    def show_squad(self, index_squad):
        try:
            squad = self.squads[index_squad]
        except:
            self.squads.append([])
            squad = self.squads[len(self.squads) - 1]
        print("Сейчас в отряде находятся: ")
        unit_dict = defaultdict(int)
        for unit in squad:
            unit_dict[unit.type] += 1
        for unit_types in unit_dict:
            print("--> Количество: {}. Тип: {}"
                  .format(unit_dict[unit_types], unit_types))    

    

# отладить вывод типа в показа отряда
