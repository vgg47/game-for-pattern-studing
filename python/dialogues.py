from player import Player
from price import price
import army


def choose_race(name):
    race = input(
        "{}, пришло время выбрать сторону: Гондор или Изенгард? ".format(name)).lower()
    if not (race in ("1", '2', 'изенгард', 'гондор')):
        print("incorrect input")
        return choose_race(name)
    else:
        return race


def read_base_info():
    name = input("Доброго времени суток!\nВведи своё имя: ")
    choosen_race = choose_race(name)
    # choosen_race = choose_race(name)
    player = Player(name=name, race=choosen_race)
    player.create_army(input(
        "Введи название своей первой армии: "))
    # player.create_castle(name=input("Введи название своей первой крепости: "), owner=Player.name)
    print("Отлично, {}, хорошей игры и пусть удача всегда будет на твоей стороне!".format(name))
    return player


def choice_of_action(player):
    while True:
        action = input(
            'Выбери действие: \n1) Отправиться в поход\n2) Развивать войска\n3) Развивать замки\n')
        if action == '1':
            crusade(player)
        elif action == '2':
            develop_troops(player)
        elif action == '3':
            print("in development")
            # develop_castles()
        break


def try_to_int(x):
    try:
        return int(x)
    except:
        return x


def develop_economy_of_army(player, current_army)
    while True:
        action = input(
            "Выбери, что ты хочешь улучшить:\n1) Увеличить запас хода армии\n2) Поднять боевой дух армии\n3) Вернуться назад\n")
        while True:
            if action == '1':
                if  player.army[current_army].number_of_steps < army.max_number_of_steps:
                    choice = input("Текущий запас хода {}. Улучшение будет стоить {} золота.\nВ данный момента у игрока {} золота. Произвести улучшение?\n".format(player.army[current_army], price.number_of_steps[player.army[current_army].number_of_steps], player.gold))
                    if choice in "yes" or choise == '1':
                        player.army[current_army].set_number_of_steps()
                    else:
                        break
                else:
                    print("Запас хода твоей армии максимален, так держать!")
                    break
            elif action == '2':
                if  player.army[current_army] .morale < army.max_morale:
                    choice = input("Текущий боевой дух {}. Улучшение будет стоить {} золота.\nВ данный момента у игрока {} золота. Произвести улучшение?\n".format(player.army[current_army].morale, price.morale[player.army[current_army].morale], player.gold))
                    if choice in "yes" or choise == '1':
                        player.army[current_army].set_morale()
                    else:
                        break
                else:
                    print("Боевой дух твоей армии максимален, так держать!")
                    break
            elif action == '3':
                break
            else:
                print("Некорректный ввод")

def hire_troops(player, current_army):
    try:
        _squad_index = int(input(
            "Введи номер отряда до {}, в который ты хочешь нанимать войска. Если хочешь создать новый отряд - введи 0.\n".format(len(player.army[current_army].squads)))) - 1
        print("Введи тип юнита для найма и количество: ")
        _type, _quantity = map(try_to_int, input().split())
        player.army[current_army].hire(
            _squad_index, _type, _quantity)
    except ValueError:
        print("Введите два корректных аргумента")
        hire_troops(player, current_army)


def crusade(player):
    print("in development")


def develop_troops(player):
    while True:
        action = input(
            'Выбери действие: \n1) Развивать существующие армии\n2) Создавать новые\n3) Вернуться назад\n')
        if action == '1':
            print('Выбери номер армии: ')
            for i in range(len(player.army)):
                print('{}) {}'.format(i + 1, player.army[i].name_army))
            current_army = int(input()) - 1
            while True:
                sub_action = input(
                    "1) Развивать экономику\n2) Нанимать войска\n3) Вернуться назад\n")
                if sub_action == '1':
                    develop_economy_of_army(player, current_army)
                elif sub_action == '2':
                    hire_troops(player, current_army)
                elif sub_action == '3':
                    break  # нужно сделать переход к след части кода
        elif action == '2':
            name_army = input("Введи название армии: ")
            player.create_army(name_army)
        elif action == '3':
            break
