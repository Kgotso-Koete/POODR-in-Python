'''
Tying up chapter 5 with all classes so far
'''

class Bicycle(object):
	def __init__(self,**kwargs):
		self.__size = kwargs.get('size', None)
		self.__chain = kwargs.get('chain', self.default_chain(self))
		self.__tire_size = kwargs.get('tire_size', self.default_tire_size(self))
		self.post_initialize(**kwargs)

	# data hiding
	@property
	def size(self):
		return self.__size

	@property
	def chain(self):
		return self.__chain

	@property
	def tire_size(self):
		return self.__tire_size

	@staticmethod
	def post_initialize(self,**kwargs): # And implements this
		return None

	def spares(self):
		parent_spares = {'tire_size': self.tire_size, 'chain':self.chain}
		return {**parent_spares, **self.local_spares()}

	def local_spares(self):
		return {}

	@staticmethod
	def default_tire_size(self):
		raise NotImplementedError("This",self.__class__.__name__,\
	                             "can not respond to :",\
								 self.default_tire_size.__name__ )

	@staticmethod
	def default_chain(self):
		return '10-speed'


class RoadBike(Bicycle):
	def post_initialize(self,**kwargs):
		self.__tape_color = kwargs.get('tape_color', None)

	@property
	def tape_color(self):
		return self.__tape_color

	def local_spares(self):
		return {'tape_color': self.tape_color}

	@staticmethod
	def default_tire_size(self):
		return '23'


class MountainBike(Bicycle):
	def post_initialize(self,**kwargs):
		self.__front_shock = kwargs.get('front_shock', None)
		self.__rear_shock = kwargs.get('front_shock', None)

	@property
	def front_shock(self):
		return self.__front_shock

	@property
	def rear_shock(self):
		return self.__rear_shock

	def local_spares(self):
		return {'rear_shock': self.rear_shock}

	@staticmethod
	def default_tire_size(self):
		return '2.1'

class RecumbantBike(Bicycle):
	def post_initialize(self,**kwargs):
		self.__flag = kwargs.get('flag', None)

	@property
	def flag(self):
		return self.__flag

	def local_spares(self):
		return {'flag': self.flag}

	@staticmethod
	def default_tire_size(self):
		return '9-speed'

	@staticmethod
	def default_chain(self):
		return '28'

if __name__ == '__main__':
	# initialize
	road_bike = RoadBike(
	size = 'M',
	tape_color = 'red')

	print(road_bike.spares())
	# -> {:tire_size   => "23",
	#     :chain       => "10-speed",
	#     :tape_color  => "red"}

	mountain_bike = MountainBike(
	size = 'S',
	front_shock = 'Manitou',
	rear_shock = 'Fox')

	print(mountain_bike.spares())
	# -> {:tire_size   => "2.1",
	#     :chain       => "10-speed",
	#     :rear_shock  => "Manitou"}

	bent = RecumbantBike(flag = 'tall and orange')
	print(bent.spares())
	# -> {:tire_size   => "28",
	#     :chain       => "9-speed",
	#     :flag  => "tall and orange"}
