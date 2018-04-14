""" Created by Vladimir Gonchrov, 11.04.2018
    Army is dictionary where key is type of unit and value is
    list units this type.
    Method choice_side() return Factory which create units selected race
    Method create_army() creates army race which player chose
    Method hire(<type_unit>) allows hire units definitely type"""

import fight as ft
from gondorarmy import GondorArmy
from gondorunitfactory import GondorUnitFactory
from izengardarmy import IzengardArmy
from izengardunitfactory import IzengardUnitFactory

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
        print("Incorrect input!")
        return choice_side()


def create_army(_race, _factory):
    if _race == "gondor" or _race == "1":
        return GondorArmy(_factory)
    elif _race == "izengard" or _race == "2":
        return IzengardArmy(_factory)
    else:
        print("Incorrect input!")
        return create_army(_race, _factory)


choosen_race = input("Choose your side: Gondor or Izengard? ").lower()
uf = choice_side(choosen_race)
myArmy = create_army(choosen_race, uf)
a = uf.create_unit("soldier")

# нужно допилить чтобы персонажа определнного типа
# нельщя было запихнуть в чужой лист
for i in range(2):
    myArmy.hire("soldier")
    print("attack force your army:", ft.count_attack(myArmy))
    myArmy.hire("archer")
    print("attack force your army:", ft.count_attack(myArmy))
