from Unit_hierarchy import Gondor, Damage_dealer, Support 

class Soldier(Gondor, Damage_dealer):
	"""docstring for Soldier"""
	def __init__(self, **characteristics):
		super(Soldier, self).__init__(**characteristics)
	
	@staticmethod
	def message():
		print("New soldier is created")
