""" Created by Vladimir Gonchrov, 11.04.2018 
	This file declares specific classes of units of the race Gondor
	message() is method which prints message when unit is created
	check_attack() is method which prints units attack """


from unithierarchy import Gondor, DamageDealer, Support 

class Soldier(Gondor, DamageDealer):
	"""docstring for Soldier"""
	def __init__(self, magic_spell = 20, attack = 15, attack_range = 5, attack_speed = 40,\
				attack_type = "phys", cost = 45, health = 70, speed = 5, defence = 30,\
				magic_resistance = 15, phys_resistance = 10):
		super().__init__(magic_spell = 20, attack = 15, attack_range = 5, attack_speed = 40,\
				attack_type = "phys", cost = 45, health = 70, speed = 5, defence = 30,\
				magic_resistance = 15, phys_resistance = 10)
	
	@staticmethod
	def message():
		print("New Soldier is created")


class Archer(Gondor, DamageDealer):
	def __init__(self, **characteristics):
		super().__init__(**characteristics)

	@staticmethod
	def message():
		print("New Archer is created")

class Knight(Gondor, DamageDealer):
	def __init__(self, **characteristics):
		super().__init__(**characteristics)

	@staticmethod
	def message():
		print("New Knight is created")

class GuardianOfCitadeles(Gondor, DamageDealer):
	def __init__(self, **characteristics):
		super().__init__(**characteristics)

	@staticmethod
	def message():
		print("New Guardian of Citadeles is created")

class Pathfinder(Gondor, Support):
	"""docstring for Pathfinder"""
	def __init__(self, **characteristics):
		super().__init__(**characteristics)
	
	@staticmethod
	def message():
		print("New Pathfinder is created")

"""--------------------в проекте осадные орудия и тд и тп-----------------"""

# class SiegeGun(Gondor, Support):
# 	"""docstring for SiegeGun"""
# 	def __init__(self, **characteristics):
# 		super().__init__(**characteristics)21
	
# 	@staticmethod
# 	def message():
# 		print("New SiegeGun is created")

