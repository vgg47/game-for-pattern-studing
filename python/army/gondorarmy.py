""" Created by Vladimir Goncharov, 13.04.2018
    File declares class which responsible for Gordon army"""

from army import Army


class GondorArmy(Army):
    """docstring for GondorArmy"""

    def __init__(self, uf):
        super().__init__(uf)
        self.available_unit = ['soldier', 'archer', 'knight', 'guardianofcitadeles', 'pathfinder']
