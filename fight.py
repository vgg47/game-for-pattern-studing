""" Created by Vladimir Gonchrov, 11.04.2018
    count_attack() considers the total damage to the army / unit"""
import sys

sys.path.append('./army')


from army import Army


def start_fight(my_army, enemy_army):
    print("Удачи, Герой!\n"
          "Сразиться автоматически?\n 1) Да\n2) Нет\n")
    auto = input()
    if auto.lower() in 'даyes1':
        return auto_fight(my_army, enemy_army)
    elif auto.lower() in 'нетno2':
        return fight_ones_own(my_army, enemy_army)
    else:
        print("Incorrect input")
        return start_fight(my_army, enemy_army)


def choose_squad_for_fight(army):
    army.show_squads()
    try:
        squad_index = int(input()) - 1
        return squad_index
    except Exception:
        print("Incorrect input")
        choose_squad_for_fight(army)


def squad_is_alive(squad):
    for unit in squad:
        if unit.health > 0:
            return True
    return False


def squad_fight(my_squad, enemy_squad):
    while(squad_is_alive(my_squad) and squad_is_alive(enemy_squad)):
        for i in range(len(my_squad)):
            if isistance(my_squad[i], DamageDealer):
                enemy_unit_index = randint(0, len(enemy_squad))
                my_squad[i].action(enemy_squad[enemy_unit_index])
            elif isistance(my_squad[i], Support):
                own_unit_index = randint(0, len(my_squad))
                my_squad[i].action(my_squad[own_unit_index])
            if my_squad[i].health == 0:
                del my_squad[i]
            if enemy_squad[enemy_unit_index].health == 0:
                del enemy_squad[enemy_unit_index]


def auto_attack(my_army, enemy_army):
    index_strongest_squad = 0
    max_potential = -1
    for i in range(len(my_army.squads)):
        potential = my_army.count_potential(my_army.squads[i])
        if max_potential < potential:
            max_potential = potential
            index_strongest_squad = i
    victim_max_potential = -1
    min_victim_potential = -1
    index_suitable_enemy_squad = 0
    index_weakest_enemy_squad = 0
    for i in range(len(enemy_army.squads)):
        potential = enemy_army.count_potential(enemy_army.squads[i])
        if victim_max_potential < potential and potential < max_potential:
            victim_max_potential = potential
            index_suitable_enemy_squad = i
        if min_victim_potential > potential:
            min_victim_potential = potential
            index_weakest_enemy_squad = i
    if victim_max_potential == -1:
        index_suitable_enemy_squad = index_weakest_enemy_squad
    squad_fight(my_army[index_strongest_squad],
                enemy_army[index_suitable_enemy_squad])
    if not squad_is_alive(my_army.squads[index_strongest_squad]):
        del my_army.squads[index_strongest_squad]
    if not squad_is_alive(enemy_army[index_suitable_enemy_squad]):
        del enemy_army.squads[index_suitable_enemy_squad]


def fight_ones_own(my_army, enemy_army):
    while(my_army.is_alive() and enemy_army.is_alive()):
        print("Выбери свой отряд для нападения:\n")
        own_squad_index = choose_squad_for_fight(my_army)
        print("Выбери отряд, на который хочешь напасть:\n")
        enemy_squad_index = choose_squad_for_fight(enemy_army)
        squad_fight(my_army.squads[own_squad_index],
                    enemy_army.squads[enemy_squad_index])
        if not squad_is_alive(my_army.squads[own_squad_index]):
            del my_army.squads[own_squad_index]
        if not squad_is_alive(enemy_army[enemy_squad_index]):
            del enemy_army.squads[enemy_squad_index]
        auto_attack(enemy_army, my_army)
    return end_battle(my_army, enemy_army)


def auto_fight(my_army, enemy_army):
    while(my_army.is_alive() and enemy_army.is_alive()):
        auto_attack(my_army, enemy_army)
        auto_attack(enemy_army, my_army)
    return end_battle(my_army, enemy_army)


def end_battle(my_army, enemy_army):
    if my_army.is_alive():
        return True
    return False
