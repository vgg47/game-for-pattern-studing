#pragma once
#include <iostream>
#include "../h/Gondor_pers.h"

Soldier::Soldier(): Unit(45, 70, 5, 30, 15, 10), Gondor(20), Gondor_damage_dealer(15, 5, 40, "phys") {};  
void Soldier::Message() const {
    std::cout << "New soldier is created" << endl;
}

Archer::Archer(): Unit(60, 50, 5, 20, 20, 7), Gondor(20), Gondor_damage_dealer(12, 20, 40, "phys") {};  
void Archer::Message() const {
    std::cout << "New archer is created" << endl;
}

Knight::Knight(): Unit(100, 90, 15, 40, 20, 15), Gondor(15), Gondor_damage_dealer(25, 7, 40, "phys") {};  
void Knight::Message() const {
    std::cout << "New knight is created" << endl;
}

Guardian_citadeles::Guardian_citadeles(): Unit(100, 110, 7, 45, 20, 25), Gondor(30), Gondor_damage_dealer(30, 7, 45, "phys") {};  
void Guardian_citadeles::Message() const {
    std::cout << "New guardian of the citadele is created" << endl;
}

Pathfinder::Pathfinder(): Unit(80, 80, 7, 30, 15, 10), Gondor(35), Gondor_support(20, 40, 30) {};  
void Pathfinder::Message() const {
    std::cout << "New pathfinder is created" << endl;
}

Siege_gun::Siege_gun(): Unit(120, 150, 3, 30, 15, 20), Gondor(30), Gondor_damage_dealer(60, 20, 20, "phys") {};  
void Siege_gun::Message() const {
    std::cout << "New siege gun is created" << endl;
}
