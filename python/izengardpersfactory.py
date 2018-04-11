""" Created by Vladimir Gonchrov, 11.04.2018
	This methods create units of Izengard race"""


from izengardpers import OrcWorker, UrukHai, UrukShooter, Shaman, Berserk, Horseman

def create_orc_worker():
	return OrcWorker(fury = 20, attack = 20, attack_range = 5, attack_speed = 30,\
				attack_type = "phys", cost = 50, health = 60, speed = 5, defence = 20,\
				magic_resistance = 10, phys_resistance = 20)

def create_uruk_hai():
	return UrukHai(fury = 40, attack = 35, attack_range = 5, attack_speed = 40,\
			attack_type = "phys", cost = 80, health = 90, speed = 7, defence = 30,\
			magic_resistance = 15, phys_resistance = 30)

def create_uruk_shooter():
	return UrukShooter(fury = 15, attack = 15, attack_range = 20, attack_speed = 40,\
			attack_type = "phys", cost = 70, health = 70, speed = 5, defence = 15,\
			magic_resistance = 15, phys_resistance = 10)


def create_berserk():
	return Berserk(fury = 100, attack = 40, attack_range = 7, attack_speed = 40,\
			attack_type = "phys", cost = 100, health = 100, speed = 9, defence = 30,\
			magic_resistance = 30, phys_resistance = 30)

def create_shaman():
	return Shaman(fury = 30, heal = 20, heal_range = 15,\
		heal_speed = 30, increase_attack = 20, increase_defence = 20,\
		cost = 60, health = 40, speed = 5, defence = 20,\
		magic_resistance = 30, phys_resistance = 30)

def create_horseman():
	return Horseman(fury = 30, attack = 30, attack_range = 7, attack_speed = 35,\
			attack_type = "phys", cost = 90, health = 80, speed = 15, defence = 35,\
			magic_resistance = 15, phys_resistance = 15)