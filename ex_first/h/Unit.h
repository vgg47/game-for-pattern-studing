#pragma once

class Unit {
public:
    Unit() = default;
    
    Unit(int cost, int _health, int _speed, int _defence, int _magic_resistance, int _phys_resistance);    
	
    virtual void Message() const;

    int cost;
    int health;
    int speed;
    int defence;
    int magic_resistance;
    int phys_resistance;

};