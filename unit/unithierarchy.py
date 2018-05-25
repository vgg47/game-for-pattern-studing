""" Created by Vladimir Gonchrov, 11.04.2018
    This file declares races and types classes """

from unit import Unit


class Gondor(Unit):
    """docstring for Gondor"""

    def __init__(self, **characteristics):
        self.magic_spell = characteristics['magic_spell']
        super().__init__(**characteristics)


class Izengard(Unit):
    """docstring for Izengard"""

    def __init__(self, **characteristics):
        self.fury = characteristics['fury']
        super().__init__(**characteristics)


class DamageDealer(Unit):
    """docstring for Damage_dealer"""

    def __init__(self, **characteristics):
        self.attack = characteristics['attack']
        self.attack_range = characteristics['attack_range']
        self.attack_type = characteristics['attack_type']
        super().__init__(**characteristics)

    def action(self, enemy, reply=True):
        if self.attack_type == 'phys':
            protection_factor = enemy.phys_resistance
        else:
            protection_factor = enemy.magic_resistance
        difference = self.attack - protection_factor - enemy.defence
        if difference > 0:
            enemy.health = max(enemy.health - difference, 0)
            if enemy.health > 0:
                if isinstance(enemy, DamageDealer) and enemy.attack_range >= \
                        self.attack_range and reply == True:
                    enemy.action(self, reply=False)

    def get_attack(self):
        return self.attack


class Support(Unit):
    """docstring for Support"""

    def __init__(self, **characteristics):
        self.heal = characteristics['heal']
        self.increase_attack = characteristics['increase_attack']
        self.increase_defence = characteristics['increase_defence']
        super().__init__(**characteristics)

    def action(self, ally):
        ally.defence += self.increase_defence
        ally.attack += self.increase_attack
        ally.heal += self.heal

    def get_attack(self):
        return 0
      