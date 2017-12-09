'''
First attempt at a Bicycle sub-class
'''

class Bicycle(object):
	def __init__(self,**kwargs):
		self.size = kwargs['size']
		self.tape_color = kwargs.get('tape_color', None)

	def spares(self):
		return {'chain': '10-speed' , 'tire_size': '23' , 'tape_color': self.tape_color}

class MountainBike(Bicycle):
	def __init__(self,**kwargs):
		Bicycle.__init__(self,**kwargs)
		self.front_shock = kwargs['front_shock']
		self.rear_shock = kwargs['rear_shock']

	def spares(self):
		add_spare = {'front_shock':self.front_shock, 'rear_shock': self.rear_shock}
		return {**super().spares(), **add_spare}


if __name__ == '__main__':
	# initialize a new bike
	mountain_bike = MountainBike(
                  size = 'S',
                  front_shock = 'Manitou',
                  rear_shock = 'Fox')

	print(mountain_bike.size)
	 # -> 'S')
	print(mountain_bike.spares())
	# -> {:tire_size   => "23",       <- wrong!
	#     :chain       => "10-speed",
	#     :tape_color  => nil,        <- not applicable
	#     :front_shock => 'Manitou',
	#     :rear_shock  => "Fox"}
