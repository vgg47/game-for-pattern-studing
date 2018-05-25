""" Created by Vladimir Gonchrov, 12.04.2018
This class is responsible for creating units of Izengard race
In id units first digit is responsible for race: 1 - Gondor, 2 - Izengard
second digit is responsible for type: 1 - Damage Dealer, 2 - Support"""

from izengardpers import OrcWorker, UrukHai, UrukShooter, \
    Shaman, Berserk, Horseman
from unitfactory import UnitFactory


class IzengardUnitFactory(UnitFactory):
    """-----methods that create units of the race izengard-------------"""

    def create_orc_worker(self):
        return OrcWorker(fury=20, attack=20, attack_range=5,
                         attack_type="phys", cost=50, health=60, speed=5,
                         defence=20,
                         magic_resistance=10, phys_resistance=20,
                         type='оркрабочий', used_skill=False)

    def create_uruk_hai(self):
        return UrukHai(fury=40, attack=35, attack_range=5,
                       attack_type="phys", cost=80, health=90, speed=7,
                       defence=30,
                       magic_resistance=15, phys_resistance=30,
                       type='урукхай', used_skill=False)

    def create_uruk_shooter(self):
        return UrukShooter(fury=15, attack=15, attack_range=20,
                           attack_type="phys", cost=70, health=70, speed=5,
                           defence=15,
                           magic_resistance=15, phys_resistance=10,
                           type='урукстрелок', used_skill=False)

    def create_berserk(self):
        return Berserk(fury=100, attack=40, attack_range=7,
                       attack_type="phys", cost=100, health=100, speed=9,
                       defence=30,
                       magic_resistance=30, phys_resistance=30,
                       type='берсерк', used_skill=False)

    def create_shaman(self):
        return Shaman(fury=30, heal=20, increase_attack=20,
                      increase_defence=20,
                      cost=60, health=40, speed=5, defence=20,
                      magic_resistance=30, phys_resistance=30,
                      type='шаман', used_skill=False)

    def create_horseman(self):
        return Horseman(fury=30, attack=30, attack_range=7,
                        attack_type="phys", cost=90, health=80, speed=15,
                        defence=35,
                        magic_resistance=15, phys_resistance=15,
                        type='всадник', used_skill=False)

    def create_unit(self, _type):
        _type = _type.lower()
        if _type == "oркрабочий" or _type == "211":
            return self.create_orc_worker()
        elif _type == "урукхай" or _type == "212":
            return self.create_uruk_hai()
        elif _type == "урукстрелок" or _type == "213":
            return self.create_uruk_shooter
        elif _type == "берсерк" or _type == "214":
            return self.create_berserk()
        elif _type == "шаман" or _type == "221":
            return self.create_shaman()
        elif _type == "всадник" or _type == "215":
            return self.create_horseman()
        else:
            print("Incorrect input on _type = {}".format(_type))
