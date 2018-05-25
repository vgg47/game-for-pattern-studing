""" Created by Vladimir Gonchrov, 12.04.2018
This class is responsible for creating units of Gondor race
In id units first digit is responsible for race: 1 - Gondor, 2 - Izengard
second digit is responsible for type: 1 - Damage Dealer, 2 - Support"""

import sys

sys.path.append('./unit')

from gondorpers import Soldier, Archer, Knight, Pathfinder, GuardianOfCitadeles
from unitfactory import UnitFactory


class GondorUnitFactory(UnitFactory):
    """---------methods that create units of the race gondor--------"""

    def create_soldier(self):
        return Soldier(magic_spell=20, attack=15, attack_range=5,
                       attack_type='phys', cost=45, health=70,
                       speed=5, defence=30, magic_resistance=15,
                       phys_resistance=10, type='солдат',
                       wall_of_shield=False, used_skill=False)

    def create_archer(self):
        return Archer(magic_spell=20, attack=12, attack_range=20,
                      attack_type="phys", cost=60, health=50,
                      speed=5, defence=20, magic_resistance=20,
                      phys_resistance=7, type='лучник', used_skill=False)

    def create_knight(self):
        return Knight(magic_spell=15, attack=25, attack_range=7,
                      attack_type="phys", cost=100, health=90,
                      speed=15, defence=40, magic_resistance=20,
                      phys_resistance=15, type='рыцарь', used_skill=False)

    def create_guardian_of_citadeles(self):
        return GuardianOfCitadeles(magic_spell=30, attack=30,
                                   attack_range=7,
                                   attack_type="phys",
                                   cost=100, health=110, speed=7, defence=45,
                                   magic_resistance=20, phys_resistance=25,
                                   type='стражцитадели', used_skill=False)

    def create_pathfinder(self):
        return Pathfinder(magic_spell=30, heal=20, increase_attack=20,
                          increase_defence=20,
                          cost=80, health=80, speed=7, defence=30,
                          magic_resistance=15, phys_resistance=10,
                          type='следопыт', used_skill=False)

    def create_unit(self, _type):
        _type = _type.lower()
        if _type == "солдат" or _type == "111":
            return self.create_soldier()
        elif _type == "лучник" or _type == "112":
            return self.create_archer()
        elif _type == "рыцарь" or _type == "113":
            return self.create_knight()
        elif _type == "стражцитадели" or _type == "114":
            return self.create_guardian_of_citadeles()
        elif _type == "следопыт" or _type == "121":
            return self.create_pathfinder()
        else:
            print("Incorrect input")
