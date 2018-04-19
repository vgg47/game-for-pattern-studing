""" Created by Vladimir Gonchrov, 11.04.2018
    Army is dictionary where key is type of unit and value is
    list units this type.
    Method choice_side() return Factory which create units selected race
    Method create_army() creates army race which player chose
    Method hire(<type_unit>) allows hire units definitely type"""
import sys

sys.path.append('./army')
sys.path.append('./unitfactory')


from izengardarmy import IzengardArmy
from gondorarmy import GondorArmy
from gondorunitfactory import GondorUnitFactory
import fight as ft
from izengardunitfactory import IzengardUnitFactory
from player import Player

""" Механика такова: 1) игрок выбирает сторону, ему автоматически создается
первая армия
2)далее в процессе игры он может создавать дополнительные армии, но только
той расы, которую он выбрал в начале игры."""


def choice_side(_race):
    if _race == "gondor" or _race == 1:
        return GondorUnitFactory()
    elif _race == "izengard" or _race == "2":
        return IzengardUnitFactory()
    else:
        print("incorrect input")
        raise Exception


def main():
        #choosen_race = input("Choose your side: Gondor or Izengard? ").lower()
    choosen_race = "gondor"
    dima = Player()
    uf = choice_side(choosen_race)
    dima.create_army(choosen_race, uf, "nagibateli228")

    # нужно допилить чтобы персонажа определнного типа
    # нельщя было запихнуть в чужой лист
    for i in range(2):
        dima.army["nagibateli228"].hire("soldier_squad", "soldier")
        print("attack ftorce your army:", ft.count_attack(dima.army["nagibateli228"]))


if __name__ == '__main__':
    main()
