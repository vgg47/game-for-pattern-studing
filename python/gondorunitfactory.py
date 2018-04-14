""" Created by Vladimir Gonchrov, 12.04.2018
This class is responsible for creating units of Gondor race
In id units first digit is responsible for race: 1 - Gondor, 2 - Izengard
second digit is responsible for type: 1 - Damage Dealer, 2 - Support"""

from unitfactory import UnitFactory
from gondorpers import Soldier, Archer, Knight, Pathfinder, GuardianOfCitadeles

class GondorUnitFactory(UnitFactory):

    """---------------methods that create units of the race gondor---------------------------------------------"""
    def create_soldier(self):
        return Soldier(magic_spell = 20, attack = 15, attack_range = 5, attack_speed = 40,\
                attack_type = "phys", cost = 45, health = 70, speed = 5, defence = 30,\
                magic_resistance = 15, phys_resistance = 10)

    def create_archer(self):
        return Archer(magic_spell = 20, attack = 12, attack_range = 20, attack_speed = 40,\
                attack_type = "phys", cost = 60, health = 50, speed = 5, defence = 20,\
                magic_resistance = 20, phys_resistance = 7)

    def create_knight(self):
        return Knight(magic_spell = 15, attack = 25, attack_range = 7, attack_speed = 40,\
                attack_type = "phys", cost = 100, health = 90, speed = 15, defence = 40,\
                magic_resistance = 20, phys_resistance = 15)

    def create_guardian_of_citadeles(self):
        return GuardianOfCitadeles(magic_spell = 30, attack = 30, attack_range = 7, attack_speed = 45,\
                attack_type = "phys", cost = 100, health = 110, speed = 7, defence = 45,\
                magic_resistance = 20, phys_resistance = 25)

    def create_pathfinder(self):
        return Pathfinder(magic_spell = 30, heal = 20, heal_range = 15,\
            heal_speed = 30, increase_attack = 20, increase_defence = 20,\
            cost = 80, health = 80, speed = 7, defence = 30,\
            magic_resistance = 15, phys_resistance = 10)

    def create_unit(self, _type):
        _type = _type.lower()
        if _type == "soldier" or _type == "111":
            return self.create_soldier()
        elif _type == "archer" or _type == "112":
            return self.create_archer()
        elif _type == "khight" or _type == "113":
            return self.create_knight()
        elif _type == "guardian of citadeles" or _type == "114":
            return self.create_guardian_of_citadeles()
        elif _type == "pathfinder" or _type == "121":
            return self.create_pathfinder()
        else:
            print("Incorrect input")

