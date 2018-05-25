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
        self.type = characteristics['type']
        self.used_skill = characteristics['used_skill']

    def get_defence(self):
        return self.defence


    def get_attack(self):
        pass
