import sys

sys.path.append('./army')
sys.path.append('./unitfactory')


from izengardarmy import IzengardArmy
from gondorarmy import GondorArmy
from gondorunitfactory import GondorUnitFactory
from izengardunitfactory import IzengardUnitFactory
from army import Army
import price


class Player():
    def __init__(self, name, race, level=1, expireince=0, gold=3000,
                 inventary=[], army=[]):
        self.name = name
        self.race = race
        self.level = level
        self.expireince = expireince
        self.gold = gold
        self.inventary = inventary
        self.army = army

    def create_army(self, name_army):
        if self.race == "гондор" or self.race == "1":
            self.army.append(GondorArmy(
                GondorUnitFactory(), name_army, self.name))
        elif self.race == "изенгард" or self.race == "2":
            self.army.append(IzengardArmy(
                IzengardUnitFactory(), name_army, self.name))
        else:
            print("incorrect input")

    def count_attack(self, real_army=None):
        summ = 0
        if (real_army == None):
            for concrete_army in self.army:
                summ += concrete_army.count_attack()
        else:
            print(type(real_army))
            summ += real_army.count_attack()
        return summ

    def count_defence(self, real_army=None):
        summ = 0
        if (real_army == None):
            for concrete_army in self.army:
                summ += concrete_army.count_defence()
        else:
            print(type(real_army))
            summ += real_army.count_defence()
        return summ

    def set_number_of_steps(self, concrete_army):
        value = self.army[concrete_army].number_of_steps + 5
        if self.gold >= price.number_of_steps[value]:
            self.army[concrete_army].set_number_of_steps(value)
            self.gold -= price.number_of_steps[value]
            return True
        else:
            return False

    def set_morale(self, concrete_army):
        value = self.army[concrete_army].morale + 0.25
        if self.gold >= price.morale[value]:
            self.army[concrete_army].set_morale(value)
            self.gold -= price.morale[value]
            return True
        else:
            return False
