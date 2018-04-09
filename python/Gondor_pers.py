from Unit_hierarchy import Gondor, Damage_dealer, Support 

class Gondor_soldier(Gondor, Damage_dealer):
	"""docstring for Soldier"""
	def __init__(self, **characteristics):
		super().__init__(**characteristics)
	
	@staticmethod
	def message():
		print("New Gondor Soldier is created")

class Gondor_archer(Gondor, Damage_dealer):
	def __init__(self, **characteristics):
		super().__init__(**characteristics)

	@staticmethod
	def message():
		print("New Gondor Archer is created")