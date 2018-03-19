#pragma once

#include "Unit_division.h"


Gondor::Gondor(int _magic_spell): magic_spell(_magic_spell) {};
Gondor_damage_dealer::Gondor_damage_dealer(int _attack, int _range, int _attack_speed, string _type_attack): attack(_attack), range(_range), type_attack(_type_attack) {}
Gondor_support::Gondor_support(int _heal, int _increase_attack, int _increase_defence, int _heal_speed): heal(_heal), increase_attack(_increase_attack), increase_defence(_increase_defence), heal_speed(_heal_speed) {}

Izengard::Izengard(int _fury): fury(_fury) {}
Izengard_damage_dealer::Izengard_damage_dealer(int _attack, int _range, int _attack_speed, string _type_attack): attack(_attack), range(_range), type_attack(_type_attack) {}
Izengard_support::Izengard_support(int _heal, int _increase_attack, int _increase_defence, int _heal_speed): heal(_heal), increase_attack(_increase_attack), increase_defence(_increase_defence), heal_speed(_heal_speed) {}

