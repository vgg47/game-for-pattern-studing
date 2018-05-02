""" Created by Vladimir Goncharov, 13.04.2018
	File declares class which responsible for Izengard army"""

from army import Army


class IzengardArmy(Army):
    """docstring for IzengardArmy"""

    def __init__(self, uf, name_army, mobilized=None):
        super().__init__(uf, name_army, mobilized)
        self.available_unit = ('orcworker', 'urukhai', 'urukshooter', 'berserk', 'shaman', 'horseman')
