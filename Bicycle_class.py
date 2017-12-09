'''
Making Bike responsible for initializing variables
**PLEASE NOTE, CONTAINS ERRORS
'''

class Bicycle(object):
	def __init__(self,**kwargs):
		self.__size = kwargs.get('size', None)
		self.__chain = kwargs.get('chain', self.default_chain(self))
		self.__tire_size = kwargs.get('tire_size', self.default_tire_size(self))

	@classmethod
	def post_initialize(self,**kwargs): # Bicycle both sends
		return self.post_initialize(**kwargs)

	@staticmethod
	def post_initialize(self,**kwargs): # And implements this
		return None

	@staticmethod
	def default_chain(self):
		return '10-speed'

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
	def post_initialize(self,**kwargs): # RoadBike can optionally overide this
		self.__tape_color = kwargs.get('tape_color', None)
		# RoadBike can optionally overide this

	@staticmethod
	def default_tire_size(self):
		return '23'

	@property
	def tape_color(self):
		return self.__tape_color

	def spares(self):
		add_spare = {'tape_color': self.tape_color}
		return {**super().spares(), **add_spare}

if __name__ == '__main__':
	# initialize
	road_bike = RoadBike(
              size = 'M',
              tape_color = 'red')

	print(road_bike.spares())
	# -> {:tire_size   => "23",
	#     :chain       => "10-speed",
	#     :tape_color  => "red"}
