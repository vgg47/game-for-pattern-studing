class El(list):
	def __init__(self, x):
		self.x = x

	def append(self, a):
		self.x.append(a)


a = El([1, 2, 3, 4])
a.append(2)
print(a.x)