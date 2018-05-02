from player import Player


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
        break;

def try_to_int(x):
    try:
        return int(x)
    except:
        return x


def develop_economy_of_army():
    print("in development")


def hire_troops(player, current_army):
    try:
        _squad_index = int(input(
            "Введи номер отряда, в который ты хочешь нанимать войска. Если хочешь создать новый отряд - введи 0.\n")) - 1
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
