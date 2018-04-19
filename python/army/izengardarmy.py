""" Created by Vladimir Goncharov, 13.04.2018
	File declares class which responsible for Izengard army"""

from army import Army


class IzengardArmy(Army):
    """docstring for IzengardArmy"""

    def __init__(self, uf):
        super().__init__(uf)
        self.available_unit = ['orc_worker', 'uruk hai', 'uruk shooter', 'berserk', 'shaman', 'horseman']
