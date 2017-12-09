'''
Creating RecumbentBike Class without __init__ overide
'''

class Bicycle(object):
	def __init__(self,**kwargs):
		self.__size = kwargs.get('size', None)
		self.__chain = kwargs.get('chain', self.default_chain(self))
		self.__tire_size = kwargs.get('tire_size', self.default_tire_size(self))

	@staticmethod
	def default_chain(self):
		return '10-speed'

	@staticmethod
	def default_tire_size(self):
		raise NotImplementedError("This",self.__class__.__name__,"can not respond to :",self.default_tire_size.__name__ )

	@property
	def size(self):
		return self.__size

	@property
	def chain(self):
		return self.__chain

	@property
	def tire_size(self):
		return self.__tire_size

	def spares(self):
		return {'tire_size': self.tire_size, 'chain':self.chain}

class RoadBike(Bicycle):
	def __init__(self,**kwargs):
		Bicycle.__init__(self,**kwargs) # <- RoadBike now MUST send
		self.__tape_color = kwargs.get('tape_color', None)

	@staticmethod
	def default_tire_size(self):
		return '23'

	@property
	def tape_color(self):
		return self.__tape_color

	def spares(self):
		add_spare = {'tape_color': self.tape_color}
		return {**super().spares(), **add_spare}

class MountainBike(Bicycle):
	def __init__(self,**kwargs):
		Bicycle.__init__(self,**kwargs)
		self.__front_shock = kwargs['front_shock']
		self.__rear_shock = kwargs['rear_shock']

	@staticmethod
	def default_tire_size(self):
		return '2.1'

	@property
	def front_shock(self):
		return self.__front_shock

	@property
	def rear_shock(self):
		return self.__rear_shock

	def spares(self):
		add_spare = {'front_shock':self.front_shock, 'rear_shock': self.rear_shock}
		return {**super().spares(), **add_spare}

class RecumbentBike(Bicycle):
	def __init__(self,**kwargs):
		self.__flag = kwargs['flag']

	@property
	def flag(self):
		return self.__flag

	@staticmethod
	def default_chain(self):
		return '9-speed'

	@staticmethod
	def default_tire_size(self):
		return '28'

	def spares(self):
		add_spare = {'flag':self.flag}
		return {**super().spares(), **add_spare}


if __name__ == '__main__':
	# initialize a new bike
	bent = RecumbentBike(flag = 'tall and orange')
	print(bent.size)
	# -> {:tire_size => nil, <- didn't get initialized
	#     :chain     => nil,
	#     :flag      => "tall and orange"}
