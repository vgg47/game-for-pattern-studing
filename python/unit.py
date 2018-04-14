""" Created by Vladimir Gonchrov, 11.04.2018
    This file declares base class Unit """


class Unit(object):
    def __init__(self, **characteristics):
        self.cost = characteristics['cost']
        self.health = characteristics['health']
        self.speed = characteristics['speed']
        self.defence = characteristics['defence']
        self.magic_resistance = characteristics['magic_resistance']
        self.phys_resistance = characteristics['phys_resistance']
        self.message()

    @staticmethod
    def message():
        pass

    def get_attack(self):
        if self.attack is None:
            return 0
        else:
            return self.attack
