import sys

sys.path.append('./army')
sys.path.append('./unitfactory')


from izengardarmy import IzengardArmy
from gondorarmy import GondorArmy
from gondorunitfactory import GondorUnitFactory
from izengardunitfactory import IzengardUnitFactory
from army import Army



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
            self.army.append(GondorArmy(GondorUnitFactory(), name_army))
        elif self.race == "изенгард" or self.race == "2":
            self.army.append(IzengardArmy(IzengardUnitFactory(), name_army))
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