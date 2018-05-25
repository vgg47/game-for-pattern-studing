""" Created by Vladimir Gonchrov, 11.04.2018
    Army is dictionary where key is type of unit and value is
    list units this type.
    Method choice_side() return Factory which create units selected race
    Method create_army() creates army race which player chose
    Method hire(<type_unit>) allows hire units definitely type"""
import sys
import argparse


sys.path.append('./army')
sys.path.append('./unitfactory')
parser = argparse.ArgumentParser()
parser.add_argument('--size', default=10, required=False, help='Размер игровой карты')


from izengardarmy import IzengardArmy
from gondorarmy import GondorArmy
from gondorunitfactory import GondorUnitFactory
from izengardunitfactory import IzengardUnitFactory
import fight as ft
from player import Player
import dialogues as dia
import map

""" Механика такова: 1) игрок выбирает сторону, ему автоматически создается
первая армия
2)далее в процессе игры он может создавать дополнительные армии, но только
той расы, которую он выбрал в начале игры."""


def main():
    args = parser.parse_args()
    player = dia.read_base_info()
    game_map, castle_coordinate = map.generate_map(int(args.size), player)
    dia.choice_of_action(player, game_map, castle_coordinate)
    # print(player.count_attack())

if __name__ == '__main__':
    main()
