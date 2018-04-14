""" Created by Vladimir Gonchrov, 11.04.2018
    count_attack() considers the total damage to the army / unit"""

from army import Army


def count_attack(real_army):
    sum_attack = 0
    for type_unit in real_army.army:
        for concrete_unit in real_army.army[type_unit]:
            sum_attack += concrete_unit.get_attack()
    return sum_attack
