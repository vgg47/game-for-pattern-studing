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
	def __init__(self, uf):
		self.squads = defaultdict(list)
		self.uf = uf

# чет сложно, нужно сначала чекать на принадлежность типа расе выбранной армии
# и если тип находится то нанимать юнита, иначе искать в кортеже хранящем 
# названия всех типов и id. если найдет такое, то вывести сообщение "Данный персонаж
# вам недоступен", если нет, то вывести сообщение "Неккоректный ввод"
	def hire(self, squad_name, _type):
		if _type in self.available_unit:
			self.squads[squad_name].append(self.uf.create_unit(_type))
		else:
			print("incorrect input")
			raise Exception