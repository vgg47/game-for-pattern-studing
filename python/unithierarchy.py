from unit import Unit

class Gondor(Unit):
	"""docstring for Gondor"""
	def __init__(self, **characteristics):
		self.magic_spell = characteristics['magic_spell']
		super().__init__(**characteristics)

class Izengard(Unit):
	"""docstring for Izengard"""
	def __init__(self, **characteristics):
		self.fury = characteristics['fury']
		super().__init__(**characteristics)

class DamageDealer(Unit):
	"""docstring for Damage_dealer"""
	def __init__(self, **characteristics):
		self.attack = characteristics['attack']
		self.attack_range = characteristics['attack_range']
		self.attack_speed = characteristics['attack_speed']
		self.attack_type = characteristics['attack_type']
		super().__init__(**characteristics)
		
class Support(Unit):
	"""docstring for Support"""
	def __init__(self, **characteristics):
		self.heal = characteristics['heal']
		self.heal_range = characteristics['heal_range']
		self.heal_speed = characteristics['heal_speed']
		self.increase_attack = characteristics['increase_attack']
		self.increase_defence = characteristics['increase_defence']
		super().__init__(**characteristics)
