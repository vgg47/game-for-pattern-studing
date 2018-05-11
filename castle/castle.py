""" Created by Vladimir Goncharov 03.05.2018
	This file declares base class Castle """


class Castle(object):
	def __init__(self, **characteristics):
		self.defence = characteristics['defence']
		self.local_army = characteristics['local_army']
		self.owner = characteristics['owner']
		self.name = characteristics['name']
		self.defenses = characteristics['defenses']
		self.gold = characteristics['gold']

# здесь должен быть билдер :\
