import gondorpers as gd
from factorypers import FactoryPers

class SoldierFactory(object):
	@staticmethod
	def create_unit():
		return gd.Soldier(magic_spell = 20, attack = 15, attack_range = 5, attack_speed = 40,\
 				attack_type = "phys", cost = 45, health = 70, speed = 5, defence = 30,\
 				magic_resistance = 15, phys_resistance = 10)

class ArcherFactory(FactoryPers):
	@staticmethod
	def create_unit():
		return gd.Archer(magic_spell = 20, attack = 12, attack_range = 20, attack_speed = 40,\
 				attack_type = "phys", cost = 60, health = 50, speed = 5, defence = 20,\
 				magic_resistance = 20, phys_resistance = 7)

class KnightFactory(FactoryPers):
	@staticmethod
	def create_unit():
		return gd.Knight(magic_spell = 15, attack = 25, attack_range = 7, attack_speed = 40,\
 				attack_type = "phys", cost = 100, health = 90, speed = 15, defence = 40,\
 				magic_resistance = 20, phys_resistance = 15)


class GuardianOfCitadelesFactory(FactoryPers):
	@staticmethod
	def create_unit():
		return gd.GuardianOfCitadeles(magic_spell = 30, attack = 30, attack_range = 7, attack_speed = 45,\
 				attack_type = "phys", cost = 100, health = 110, speed = 7, defence = 45,\
 				magic_resistance = 20, phys_resistance = 25)

class PathfinderFactory(FactoryPers):
	@staticmethod
	def create_unit():
		return gd.Pathfinder(magic_spell = 30, heal = 20, heal_range = 15,\
				heal_speed = 30, increase_attack = 20, increase_defence = 20,\
				cost = 80, health = 80, speed = 7, defence = 30,\
				magic_resistance = 15, phys_resistance = 10)