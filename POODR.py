from collections import namedtuple
import math

#simplifying Gear so it does not do Wheel's job
class Gear:
	# initialize
	def __init__(self, chainring, cog, wheel):
		self.__chainring = chainring
		self.__cog = cog
		self.__wheel = wheel

	# getter methods to keep initialized variables private
	@property
	def chainring(self):
		return self.__chainring

	@property
	def cog(self):
		return self.__cog

	@property
	def wheel(self):
		return self.__wheel

	def ratio(self):
		return self.chainring / float(self.cog)

	# gear_inches gave the 'diameter' method to Wheel to execute
	def gear_inches(self):
		return self.ratio() * self.wheel.diameter()

# Wheel now a seperate class with its own job
class Wheel:
	# initialize
	def __init__(self, rim, tire):
		self.__rim = rim
		self.__tire = tire

	@property
	def rim(self):
		return self.__rim

	@property
	def tire(self):
		return self.__tire

	def diameter(self):
		return self.rim + (self.tire * 2)

	def circumference(self):
		return math.pi * diameter

if __name__ == '__main__':
	## Gear expects a 'Duck' that knows 'diameter'
	new_gear = Gear(52, 11 , Wheel(26, 1.5))
	print(new_gear.gear_inches())
