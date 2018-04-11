from unithierarchy import Izengard, DamageDealer, Support 

class OrcWorker(Izengard, DamageDealer):
	"""docstring for OrcWorker"""
	def __init__(self, **characteristics):
		super().__init__(**characteristics)
	
	@staticmethod
	def message():
		print("New Orc worker is created")

class UrukHai(Izengard, DamageDealer):
	"""docstring for UrukHai"""
	def __init__(self, **characteristics):
		super().__init__(**characteristics)
	
	@staticmethod
	def message():
		print("New Uruk-hai is created")

class UrukShooter(Izengard, DamageDealer):
	"""docstring for UrukShooter"""
	def __init__(self, **characteristics):
		super().__init__(**characteristics)
	
	@staticmethod
	def message():
		print("New Uruk-shooter is created")

class Shaman(Izengard, Support):
	"""docstring for Shaman"""
	def __init__(self, **characteristics):
		super().__init__(**characteristics)
	
	@staticmethod
	def message():
		print("New Shaman is created")

class Berserk(Izengard, DamageDealer):
	"""docstring for Berserk"""
	def __init__(self, **characteristics):
		super().__init__(**characteristics)
	
	@staticmethod
	def message():
		print("New Berserk is created")

class Horseman(Izengard, DamageDealer):
	"""docstring for Horseman"""
	def __init__(self, **characteristics):
		super().__init__(**characteristics)
	
	@staticmethod
	def message():
		print("New Horseman is created")

