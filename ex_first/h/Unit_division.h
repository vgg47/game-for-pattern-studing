#pragma once

#include "Unit.h"
#include <string.h>

class Gondor: public Unit {
	int magic_spell;

	Gondor(int _magic_spell);
};

class Izengard: public Unit {
	int fury; 

	Izengard(int _fury); 
};

class Izengard_damage_dealer: public Izengard  {
public:
	Izengard_damage_dealer(int _attack, int _range, int _attack_speed, string  _type_attack);

	int attack;
	int range;
	int attack_speed;
	string type_attack;

};

class Gondor_damage_dealer: public Gondor  {
public:
	Gondor_damage_dealer(int _attack, int _range, int _attack_speed, string _type_attack);

	int attack;
	int range;
	int attack_speed;
	string type_attack;

};

class Izengard_support: public Izengard {
	int heal;
	int increase_attack;
	int increase_defence;
	int heal_speed;

	Izengard_support(int _heal, int _increase_attack, int _increase_defence, int _heal_speed);
};

class Gondor_support: public Gondor {
	int heal;
	int increase_attack;
	int increase_defence;
	int heal_speed;

	Gondor_support(int _heal, int _increase_attack, int _increase_defence, int _speed);
};