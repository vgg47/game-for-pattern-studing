""" Created by Vladimir Goncharov, 13.04.2018
	File declares class which responsible for Izengard army"""

from army import Army


class IzengardArmy(Army):
    """docstring for IzengardArmy"""

    def __init__(self, uf):
        super(IzengardArmy, self).__init__(uf)
        self.army['orc_worker'] = []
        self.army['uruk_hai'] = []
        self.army['uruk_shooter'] = []
        self.army['berserk'] = []
        self.army['shaman'] = []
        self.army['horseman'] = []
