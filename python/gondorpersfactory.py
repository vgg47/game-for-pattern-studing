""" Created by Vladimir Gonchrov, 11.04.2018 """


from gondorpers import Soldier, Archer, Knight, Pathfinder, GuardianOfCitadeles

def create_soldier():
	return Soldier(magic_spell = 20, attack = 15, attack_range = 5, attack_speed = 40,\
				attack_type = "phys", cost = 45, health = 70, speed = 5, defence = 30,\
				magic_resistance = 15, phys_resistance = 10)

def create_archer():
	return Archer(magic_spell = 20, attack = 12, attack_range = 20, attack_speed = 40,\
			attack_type = "phys", cost = 60, health = 50, speed = 5, defence = 20,\
			magic_resistance = 20, phys_resistance = 7)

def create_knight():
	return Knight(magic_spell = 15, attack = 25, attack_range = 7, attack_speed = 40,\
			attack_type = "phys", cost = 100, health = 90, speed = 15, defence = 40,\
			magic_resistance = 20, phys_resistance = 15)


def create_guardianofcitadeles():
	return GuardianOfCitadeles(magic_spell = 30, attack = 30, attack_range = 7, attack_speed = 45,\
			attack_type = "phys", cost = 100, health = 110, speed = 7, defence = 45,\
			magic_resistance = 20, phys_resistance = 25)

def create_pathfinder():
	return Pathfinder(magic_spell = 30, heal = 20, heal_range = 15,\
		heal_speed = 30, increase_attack = 20, increase_defence = 20,\
		cost = 80, health = 80, speed = 7, defence = 30,\
		magic_resistance = 15, phys_resistance = 10)