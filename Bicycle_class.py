'''
Moving all Bicycle responsibilities to new sub-class RoadBike
'''

class Bicycle(object):
	pass

class RoadBike(Bicycle):
	def __init__(self,**kwargs):
		self.__size = kwargs['size']
		self.__tape_color = kwargs.get('tape_color', None)

	@property
	def size(self):
		return self.__size

	@property
	def tape_color(self):
		return self.__tape_color

	def spares(self):
		return {'chain': '10-speed' , 'tire_size': '23' , 'tape_color': self.tape_color}

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

	print(road_bike.size)
	# => "M"

	mountain_bike = MountainBike(
	size = 'S',
	front_shock = 'Manitou',
	rear_shock = 'Fox')

	print(mountain_bike.size)
	# NoMethodError: undefined method `size
