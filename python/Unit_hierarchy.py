from Unit import Unit

class Gondor(Unit):
	"""docstring for Gondor"""
	def __init__(self, characteristics, gondor_characteristics):
		Unit.__init__(self, characteristics)
		"""в данный момент gondor_characteristics включает в себя magic_spell"""
		self.gondor_characteristics = gondor_characteristics

class Izengard(Unit):
	"""docstring for Izengard"""
	def __init__(self, characteristics, izengard_characteristics):
		Unit.__init__(self, characteristics)
		"""в данный момент izengard_characteristics включает в себя fury"""
		self.izengard_characteristics = izengard_characteristics

class Damage_dealer(Unit):
	"""docstring for Damage_dealer"""
	def __init__(self, characteristics, damage_dealer_characteristics):
		""" attack_characteristics включает в себя 
		attack, attack_range, attack_speed, attack_type """
		Unit.__init__(self, characteristics)
		self.damage_dealer_characteristics = damage_dealer_characteristics
		
class Support(Unit):
	"""docstring for Support"""
	def __init__(self, characteristics, support_characteristics):
		""" support_characteristics включает в себя 
		heal, heal_range, heal_speed, increase_attack, increase_defence"""
		Unit.__init__(self, characteristics)
		self.support_characteristics = support_characteristics
		
