'''
Creating a Bicycle class trying to be both road and mountain bike
'''

class Bicycle(object):
	def __init__(self,**kwargs):
		self.style = kwargs['style']
		self.size = kwargs['size']
		self.tape_color = kwargs.get('tape_color', 'red')
		self.front_shock = kwargs['front_shock']
		self.rear_shock = kwargs['rear_shock']

	def spares(self):
		if (self.style == 'road'):
			return {'chain':'10-speed', 'tire_size':'23', 'tape_color':self.tape_color}
		else:
			return {'chain':'10-speed', 'tire_size':'2.1', 'rear_shock':self.rear_shock}

if __name__ == '__main__':
	# initialize a new bike
	bike = Bicycle(
		style = 'mountain',
		size = 'S',
		front_shock = 'Manitou',
		rear_shock = 'Fox')

	print(bike.spares())
	# -> {:tire_size   => "2.1",
	#     :chain       => "10-speed",
	#     :rear_shock  => 'Fox'}
