'''
Moving methods from Gear to Wheel
'''

class Gear:
	# initialize
	def __init__(self, chainring, cog):
		self.__chainring = chainring
		self.__cog = cog

	# getter methods to keep initialized variables private
	@property
	def chainring(self):
		return self.__chainring

	@property
	def cog(self):
		return self.__cog

	def ratio(self):
		return self.chainring / float(self.cog)

	def gear_inches(self, diameter):
		return self.ratio() * diameter

# Wheel now has the diameter method and initializes Gear
class Wheel:
	# initialize
	def __init__(self, rim, tire, chainring, cog):
		self.__rim = rim
		self.__tire = tire
		self.__gear = Gear(chainring, cog)

	@property
	def rim(self):
		return self.__rim

	@property
	def tire(self):
		return self.__tire

	@property
	def gear(self):
		return self.__gear

	def diameter(self):
		return self.rim + (self.tire * 2)

	def gear_inches(self):
		return self.gear.gear_inches(self.diameter())


if __name__ == '__main__':
	## create new instance of Wheel
	new_wheel = Wheel( 26 , 1.5, 52 , 11 )
	#expect -----> 137.0909090909091
	print(new_wheel.gear_inches())
