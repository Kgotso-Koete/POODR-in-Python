'''
Creating a Bicycle class with attributes/methods to be inherited
'''

class Bicycle(object):
	def __init__(self,**kwargs):
		self.size = kwargs['size']
		self.tape_color = kwargs['tape_color']

	def spares(self):
		return {'chain': '10-speed' , 'tire_size': '23' , 'tape_color': self.tape_color}

if __name__ == '__main__':
	# initialize a new bike
	bike = Bicycle( size = 'M' ,tape_color = 'red' )
	print(bike.size)
	# -> 'M'
	print(bike.spares())
	# -> {:tire_size => "23", 27 # :chain => "10-speed", 28 # :tape_color => "red"}
