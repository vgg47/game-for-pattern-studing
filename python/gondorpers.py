from unithierarchy import Gondor, DamageDealer, Support 

class Soldier(Gondor, DamageDealer):
	"""docstring for Soldier"""
	def __init__(self, **characteristics):
		super().__init__(**characteristics)
	
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