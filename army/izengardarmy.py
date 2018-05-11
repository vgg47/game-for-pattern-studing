""" Created by Vladimir Goncharov, 13.04.2018
	File declares class which responsible for Izengard army"""

from army import Army


class IzengardArmy(Army):
    """docstring for IzengardArmy"""

    def __init__(self, uf, name_army, owner=None, morale=1, number_of_steps=1,
                 mobilized=False):
        super().__init__(uf, name_army, owner, morale, number_of_steps, mobilized)
        self.available_unit = ('оркрабочий', 'урукхай',
                               'урукстрелок', 'берсерк', 'шаман', 'всадник')
