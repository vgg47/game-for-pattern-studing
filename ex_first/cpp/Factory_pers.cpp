#pragma once
#include "../h/Factory_pers.h"

std::unique_ptr<Unit> Soldier_factory::create_unit() {
	unique_ptr<Soldier> new_soldier(new Soldier);
	return new_soldier;
}

std::unique_ptr<Unit> Archer_factory::create_unit() {
	unique_ptr<Archer> new_archer(new Archer);
	return new_archer;
}

std::unique_ptr<Unit> Knight_factory::create_unit() {
	unique_ptr<Knight> new_knight(new Knight);
	return new_knight;
}

std::unique_ptr<Unit> Guardian_citadeles_factory::create_unit() {
	unique_ptr<Guardian_citadeles> new_guardian_citadeles(new Guardian_citadeles);
	return new_guardian_citadeles;
}

std::unique_ptr<Unit> Pathfinder_factory::create_unit() {
	unique_ptr<Pathfinder> new_pathfinder(new Pathfinder);
	return new_pathfinder;
}

std::unique_ptr<Unit> Siege_gun_factory::create_unit() {
	unique_ptr<Siege_gun> new_siege_gun(new Siege_gun);
	return new_siege_gun;
}	

std::unique_ptr<Unit> Orc_worker_factory::create_unit() {
	unique_ptr<Orc_worker> new_orc_worker(new Orc_worker);
	return new_orc_worker;
}

std::unique_ptr<Unit> Uruk_hai_factory::create_unit() {
	unique_ptr<Uruk_hai> new_uruk_hai(new Uruk_hai);
	return new_uruk_hai;
}

std::unique_ptr<Unit> Uruk_shooter_factory::create_unit() {
	unique_ptr<Uruk_shooter> new_uruk_shooter(new Uruk_shooter);
	return new_uruk_shooter;
}

std::unique_ptr<Unit> Shaman_factory::create_unit() {
	unique_ptr<Shaman> new_shaman(new Shaman);
	return new_shaman;
}

std::unique_ptr<Unit> Berserk_factory::create_unit() {
	unique_ptr<Berserk> new_berserk(new Berserk);
	return new_berserk;
}

std::unique_ptr<Unit> Horseman_factory::create_unit() {
	unique_ptr<Horseman> new_horseman(new Horseman);
	return new_horseman;
}

std::unique_ptr<Unit> Ram_factory::create_unit() {
	unique_ptr<Ram> new_ram(new Berserk);
	return new_ram;
}

