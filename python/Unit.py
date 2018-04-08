class Unit(object):
	def __init__(self, characteristics):
		""" characteristics включает в себя cost, health, speed, defence, magic_resistance, phys_resistance"""
		self.characteristics = characteristics	
		self.message()

	@staticmethod
	def message():
		pass
