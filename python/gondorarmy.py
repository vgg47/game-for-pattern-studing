""" Created by Vladimir Goncharov, 13.04.2018
    File declares class which responsible for Gordon army"""

from army import Army


class GondorArmy(Army):
    """docstring for GondorArmy"""

    def __init__(self, uf):
        super(GondorArmy, self).__init__(uf)
        self.army['soldier'] = []
        self.army['archer'] = []
        self.army['knight'] = []
        self.army['guardianofcitadeles'] = []
        self.army['pathfinder'] = []
