""" Created by Vladimir Gonchrov, 11.04.2018
    This file declares specific classes of units of the race Gondor
    message() is method which prints message when unit is created
    check_attack() is method which prints units attack """

from unithierarchy import Gondor, DamageDealer, Support


class Soldier(Gondor, DamageDealer):
    """id class - 111"""

    def __init__(self, **characteristics):
        super().__init__(**characteristics)

    @staticmethod
    def message():
        print("New Soldier is created")


class Archer(Gondor, DamageDealer):
    """ id class - 112 """

    def __init__(self, **characteristics):
        super().__init__(**characteristics)

    @staticmethod
    def message():
        print("New Archer is created")


class Knight(Gondor, DamageDealer):
    """ id class - 113 """

    def __init__(self, **characteristics):
        super().__init__(**characteristics)

    @staticmethod
    def message():
        print("New Knight is created")


class GuardianOfCitadeles(Gondor, DamageDealer):
    """ id class - 114 """

    def __init__(self, **characteristics):
        super().__init__(**characteristics)

    @staticmethod
    def message():
        print("New Guardian of Citadeles is created")


class Pathfinder(Gondor, Support):
    """id class - 121"""

    def __init__(self, **characteristics):
        super().__init__(**characteristics)

    @staticmethod
    def message():
        print("New Pathfinder is created")


"""--------------------в проекте осадные орудия и тд и тп-----------------"""

# class SiegeGun(Gondor, Support):
#   """docstring for SiegeGun"""
#   def __init__(self, **characteristics):
#       super().__init__(**characteristics)21

#   @staticmethod
#   def message():
#       print("New SiegeGun is created")
