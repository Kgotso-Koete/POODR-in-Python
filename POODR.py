import collections

class Gear:
	# initialize
	def __init__(self, chainring, cog, rim, tire):
		self.__chainring = chainring
		self.__cog = cog
		self.__rim = rim
		self.__tire = tire

	# getter methods to keep initialized variables private
	@property
	def chainring(self):
		return self.__chainring

	@property
	def cog(self):
		return self.__cog

	@property
	def rim(self):
		return self.__rim

	@property
	def tire(self):
		return self.__tire

	# calculate the ratio
	def ratio(self):
		return self.chainring / float(self.cog)

	# calculate gear inches
	def gear_inches(self):
		return self.ratio() * (self.rim + (self.tire * 2))

# creating a new data structure to align internal and external data structures
class RevealingReferences(object):
#initialize
	def __init__(self, data):
		self.wheels = data

	#getter methed
	@property
	def wheels(self):
		return self.__wheels

	#creating custom struct (named tuple)
	Wheel = collections.namedtuple('Wheel',['rim','tire'])

	#set variables by iterating over 2D array
	@wheels.setter
	def wheels(self, ext_data_struct):
		self.__wheels = [self.Wheel(cell[0], cell[1]) for cell in ext_data_struct]

	#return an array of diameters for each wheel in 2D arry
	def diameters(self):
		return [wheel.rim + (wheel.tire * 2) for wheel in self.wheels]

#initialize
test_gear_1 = Gear( 52 , 11 , 26 , 1.5)
test_gear_2 = Gear( 52 , 11 , 24 , 1.25)

print("Test gear inches methods...")
print(test_gear_1.gear_inches())
# -> 137.090909090909
print(test_gear_2.gear_inches())
# -> 125.272727272727

print()

print("Test revealing preferences method...")
wheel_set = RevealingReferences([[ 622 , 20 ], [ 622 , 23 ], [ 559 , 30 ], [ 559 , 40 ]])
print(wheel_set.diameters())
