import sys


sys.path.append('./castle')
sys.path.append('./army')
sys.path.append('./unitfactory')

from player import Player
from random import randint, random, choice, sample
from castle import Castle
from data import castle_name, type_unit
from gondorarmy import GondorArmy
from izengardarmy import IzengardArmy
from gondorunitfactory import GondorUnitFactory
from izengardunitfactory import IzengardUnitFactory
castles = []


def generate_army(counter, _name):
    race = 'гондор' if random() > 0.5 else 'изенгард'
    if race == 'гондор':
        army = GondorArmy(GondorUnitFactory(), 'Гарнизон {}'.format(_name))
    else:
        army = IzengardArmy(IzengardUnitFactory(), 'Гарнизон {}'.format(_name))
    army.squads.append([])
    for i in range(randint(counter * 10, counter * 25)):
        _type = choice(type_unit[race])
        army.squads[0].append(army.uf.create_unit(_type))
    return army


def generate_defenses(counter):
    return None


def generate_castle(vertex, counter, _name):
    _defence = randint(max(0, (counter - 3) * 300), counter * 300)
    _local_army = generate_army(counter, _name)
    _defenses = generate_defenses(counter)
    _gold = randint(max(0, (counter - 3) * 500), counter * 500)
    return Castle(defence=_defence, local_army=_local_army, owner=None,
                  name=_name, defenses=_defenses, gold=_gold, level=counter)


def generate_map(size, player):
    game_map = []
    object_coordinate = {}
    for i in range(size):
        game_map.append([])
        for j in range(size):
            game_map[i].append([None, None])

    for q in range(size):
        i = randint(0, size - 1)
        j = randint(0, size - 1)
        current_castle_name = sample(castle_name, size)
        if game_map[i][j][0] is None:
            object_coordinate[(i, j)] = q
            game_map[i][j][0] = generate_castle(game_map[i][j][0], q,
                                                current_castle_name[q])
    object_coordinate['player'] = [0, 0]
    object_coordinate['size'] = size
    game_map[0][0][1] = player
    return game_map, object_coordinate


def show_map(game_map, object_coordinate):
    for i in range(len(game_map)):
        for j in range(len(game_map[i])):
            if isinstance(game_map[i][j][1], Player) and isinstance(game_map[i][j][0], Castle):
                print("P", end=" ")
            elif isinstance(game_map[i][j][1], Player):
                print("p", end=" ")
            elif not isinstance(game_map[i][j][0], Castle):
                print("x", end=' ')
            else:
                print(object_coordinate[(i, j)], end=' ')
        print()


def move(player, game_map, object_coordinate):
    print('Выбери направление: 1) Вверх\n2) Вправо\n3) Вниз\n4) Влево\n')
    direction = input()
    x = object_coordinate['player'][0]
    y = object_coordinate['player'][1]
    size = object_coordinate['size']
    if direction == '1' and y > 0:
        game_map[x][y - 1][1] = game_map[x][y][1]
        game_map[x][y][1] = None
        y -= 1
    elif direction == '2' and x + 1 < size:
        game_map[x + 1][y][1] = game_map[x][y][1]
        game_map[x][y][1] = None
        x += 1
    elif direction == '3' and y + 1 < size:
        game_map[x][y + 1][1] = game_map[x][y][1]
        game_map[x][y][1] = None
        y += 1
    elif direction == '4' and x > 0:
        game_map[x - 1][y][1] = game_map[x][y][1]
        game_map[x][y][1] = None
        x -= 1
    else:
        print("Incorrect input")
    object_coordinate['player'][0] = x
    object_coordinate['player'][1] = y


def do_there(player, game_map, object_coordinate):
    x = object_coordinate['player'][0]
    y = object_coordinate['player'][1]
    obj = game_map[x][y][0]
    if obj == None:
        print("Здесь нет ничего интересного...")
    elif isinstance(obj, Castle):
        while True:
            print("Здесь стоит {}.\n Аттака местного гарнизона - {},\
             его суммарная защита - {}.\nАттаковать?\n1) Да\n2) Нет\n"
                  .format(obj.name, obj.local_army.count_army_attack(),
                          obj.local_army.count_army_defence()))
            action = input()
# тут должен быть выбор армии для атаки
            if action == "1":
                result = start_fight(player.army[0], obj.local_army)
                if result:
                    print("Поздравляю! {} теперь принадлежит тебе."
                          .format(ogj.name))
                    obl.owner = player
                else:
                    print("Черт! Ты проиграл.")
                    del player.army[0]
            elif action == '2':
                pass
            else:
                do_there(player, game_map, object_coordinate)
