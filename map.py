import sys

sys.path.append('./castle')
sys.path.append('./army')
sys.path.append('./unitfactory')


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
                  name=_name, defenses=_defenses, gold=_gold)


def generate_map(size):
    game_map = []
    castle_coordinate = []
    for i in range(size):
        game_map.append([])
        for j in range(size):
            game_map[i].append([None, None])

    for q in range(size):
        i = randint(0, size - 1)
        j = randint(0, size - 1)
        current_castle_name = sample(castle_name, size)
        if game_map[i][j][0] is None:
            castle_coordinate.append((i, j))
            game_map[i][j][0] = generate_castle(game_map[i][j][0], q,
                                                current_castle_name[q])
    return game_map, castle_coordinate
