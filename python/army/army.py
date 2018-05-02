""" Created by Vladimir Goncharov, 13.04.2018"""

# import sys
# from gondorunitfactory import GondorUnitFactory
# from izengardunitfactory import IzengardUnitFactory
from collections import defaultdict
# sys.path.append('.home/elevely/tp/python/unitfactory')

gondor_type_units = ('soldier', 'archer', 'pathfinder', 'knight', \
		'guardian of citadeles', '111', '112', '113', '114', '121')
izengard_type_units = ('orc worker', 'uruk hai', 'uruk shooter', \
		'berserk', 'shaman', 'horseman', '211', '212', '213', \
		'214', '215', '221')
all_type_units = [gondor_type_units, izengard_type_units]

class Army(object):
	"""docstring for Army"""
	def __init__(self, uf, name_army, mobilized=False):
		self.squads = []
		self.uf = uf
		self.name_army = name_army
		self.mobilized = mobilized


	def hire(self, squad_index, _type, _quantity=1):
		if squad_index == -1:
			self.squads.append([])
			squad_index = len(self.squads) - 1
		if _type in self.available_unit:
			for i in range(_quantity):
				self.squads[squad_index].append(self.uf.create_unit(_type))
			if _quantity == 1:
				print("New {} is created".format(_type))
			else:
				print("{} new units with type {} are created".format(_quantity, _type))
		else:
			print("incorrect input on data: _type = {}".format(_type))
	

	def count_attack(self):
	    sum_attack = 0
	    for squad in self.squads:
	        for concrete_unit in squad:
	            sum_attack += concrete_unit.get_attack()
	    return sum_attack
