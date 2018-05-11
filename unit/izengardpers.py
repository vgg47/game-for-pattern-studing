""" Created by Vladimir Gonchrov, 11.04.2018
    This file declares specific classes of units of the race Izengard
    message() is method which prints message when unit is created
    check_attack() is method which prints units attack """

from unithierarchy import Izengard, DamageDealer, Support


class OrcWorker(Izengard, DamageDealer):
    def __init__(self, **characteristics):
        super().__init__(**characteristics)


class UrukHai(Izengard, DamageDealer):
    def __init__(self, **characteristics):
        super().__init__(**characteristics)


class UrukShooter(Izengard, DamageDealer):
    def __init__(self, **characteristics):
        super().__init__(**characteristics)


class Shaman(Izengard, Support):
    def __init__(self, **characteristics):
        super().__init__(**characteristics)


class Berserk(Izengard, DamageDealer):
    def __init__(self, **characteristics):
        super().__init__(**characteristics)


class Horseman(Izengard, DamageDealer):
    def __init__(self, **characteristics):
        super().__init__(**characteristics)
