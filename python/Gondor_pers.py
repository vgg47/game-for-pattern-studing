from Unit_hierarchy import Gondor, Damage_dealer, Support 

class Soldier(Gondor, Damage_dealer):
	"""docstring for Soldier"""
	def __init__(self, gondor_characteristics, damage_dealer_characteristics, characteristics):
		Gondor.__init__(self, gondor_characteristics, characteristics)
		Damage_dealer.__init__(self, damage_dealer_characteristics, characteristics)
	
	@staticmethod
	def message():
		print("New soldier is created")
