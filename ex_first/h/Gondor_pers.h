#pragma once

#include "Unit_division.h"

class Soldier: public Gondor_damage_dealer {
public:
    Soldier();

    void Message() const override;
};

class Archer: public Gondor_damage_dealer {
public:
    Archer();

    void Message() const override;
};

class Knight: public Gondor_damage_dealer {
public:
    Knight();

    void Message() const override;
};

class Guardian_citadeles: public Gondor_damage_dealer {
public:
    Guardian_citadeles();

    void Message() const override;
};

class Pathfinder: public Gondor_support {
public:
    Pathfinder();

    void Message() const override;
};

class Siege_gun: public Gondor_damage_dealer {
public:
    Siege_gun();

    void Message() const override;
};
