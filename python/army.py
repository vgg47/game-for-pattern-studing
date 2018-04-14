""" Created by Vladimir Goncharov, 13.04.2018"""

from gondorunitfactory import GondorUnitFactory
from izengardunitfactory import IzengardUnitFactory


class Army(object):
	"""docstring for Army"""
	def __init__(self, uf):
		self.army = {}
		self.uf = uf
	
	@staticmethod
	def employ(_type):
		self.army[_type].append(uf.create_unit(_type))