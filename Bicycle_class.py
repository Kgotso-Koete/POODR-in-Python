'''
Promoting chain and tire_size behavior to Bicycle superclass
'''

class Bicycle(object):
	def __init__(self,**kwargs):
		self.__size = kwargs['size']
		self.__chain = kwargs.get('chain','10-speed')
		self.__tire_size = kwargs.get('tire_size', 23)

	@property
	def size(self):
		return self.__size

	@property
	def chain(self):
		return self.__chain

	@property
	def tire_size(self):
		return self.__tire_size

class RoadBike(Bicycle):
	def __init__(self,**kwargs):
		Bicycle.__init__(self,**kwargs) # <- RoadBike now MUST send
		self.__tape_color = kwargs.get('tape_color', None)

	@property
	def tape_color(self):
		return self.__tape_color

	def spares(self):
		return {'chain': self.chain , 'tire_size': self.tire_size , 'tape_color': self.tape_color}

class MountainBike(Bicycle):
	def __init__(self,**kwargs):
		Bicycle.__init__(self,**kwargs)
		self.__front_shock = kwargs['front_shock']
		self.__rear_shock = kwargs['rear_shock']

	@property
	def front_shock(self):
		return self.__front_shock

	@property
	def rear_shock(self):
		return self.__rear_shock

	def spares(self):
		add_spare = {'front_shock':self.front_shock, 'rear_shock': self.rear_shock}
		return {**super().spares(), **add_spare}


if __name__ == '__main__':
	# initialize a new bike
	road_bike = RoadBike(
	size = 'M',
	tape_color = 'red' )

	print(road_bike.spares())
	# => "M"

	mountain_bike = MountainBike(
	size = 'S',
	front_shock = 'Manitou',
	rear_shock = 'Fox')

	print(mountain_bike.size)
	# NoMethodError: undefined method `size
