""" Created by Vladimir Gonchrov, 11.04.2018
    count_attack() considers the total damage to the army / unit"""
import sys

sys.path.append('./army')


from army import Army


def count_attack(real_army):
    sum_attack = 0
    for squad in real_army.squads:
        for concrete_unit in real_army.squads[squad]:
            sum_attack += concrete_unit.get_attack()
    return sum_attack
