import sys

sys.path.append('./army')
sys.path.append('./unitfactory')


from izengardarmy import IzengardArmy
from gondorarmy import GondorArmy


class Player():
    def __init__(self, level=1, expireince=0, gold=3000,
                 inventary=[], army={}):
        self.level = level
        self.expireince = expireince
        self.gold = gold
        self.inventary = inventary
        self.army = army

    def create_army(self, _race, _factory, name_army):
        if _race == "gondor" or _race == "1":
            self.army[name_army] = GondorArmy(_factory)
        elif _race == "izengard" or _race == "2":
            return IzengardArmy(_factory)
        else:
            print("incorrect input")
            raise Exception

