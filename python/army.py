""" Created by Vladimir Goncharov, 13.04.2018"""

from gondorunitfactory import GondorUnitFactory
from izengardunitfactory import IzengardUnitFactory

gondor_type_units = ('soldier', 'archer', 'pathfinder', 'knight', \
		'guardian of citadeles', '111', '112', '113', '114', '121')
izengard_type_units = ('orc worker', 'uruk hai', 'uruk shooter', \
		'berserk', 'shaman', 'horseman', '211', '212', '213', \
		'214', '215', '221')
all_type_units = [gondor_type_units, izengard_type_units]

class Army(object):
	"""docstring for Army"""
	def __init__(self, uf):
		self.army = {}
		self.uf = uf

# чет сложно, нужно сначала чекать на принадлежность типа расе выбранной армии
# и если тип находится то нанимать юнита, иначе искать в кортеже хранящем 
# названия всех типов и id. если найдет такое, то вывести сообщение "Данный персонаж
# вам недоступен", если нет, то вывести сообщение "Неккоректный ввод"
	def hire(self, _type):
		# for concrete_race in all_type_units:
		# 	for concrete_type in concrete_race:
		# 		if
		self.army[_type].append(self.uf.create_unit(_type))