#pragma once
#include <iostream>
#include "../h/Izengard_pers.h"

Orc_worker::Orc_worker(): Unit(50, 60, 5, 20, 10, 20), Izengard(20), Izengard_damage_dealer(20, 5, 30, "phys") {};  
void Orc_worker::Message() const {
    std::cout << "New orc worker is created" << endl;
}

Uruk_hai::Uruk_hai(): Unit(80, 90, 7, 30, 15, 30), Izengard(40), Izengard_damage_dealer(35, 5, 40, "phys") {};  
void Uruk_hai::Message() const {
    std::cout << "New uruk hai is created" << endl;
}

Uruk_shooter::Uruk_shooter(): Unit(70, 70, 5, 15, 15, 10), Izengard(15), Izengard_damage_dealer(15, 20, 40, "phys") {};  
void Uruk_shooter::Message() const {
    std::cout << "New uruk shooter is created" << endl;
}

Shaman::Shaman(): Unit(60, 40, 5, 20, 30, 30), Izengard(30), Izengard_support(20, 15, 30, 25) {};  
void Shaman::Message() const {
    std::cout << "New shaman is created" << endl;
}

Berserk::Berserk(): Unit(100, 100, 9, 30, 30, 30), Izengard(100), Izengard_damage_dealer(40, 7, 40, "phys") {};  
void Berserk::Message() const {
    std::cout << "New berserk is created" << endl;
}

Horseman::Horseman(): Unit(90, 80, 15, 35, 15, 15), Izengard(30), Izengard_damage_dealer(30, 7, 35, "phys") {};  
void Horseman::Message() const {
    std::cout << "New horseman is created" << endl;
}