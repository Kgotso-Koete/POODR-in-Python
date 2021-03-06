'''
Testing that Wheel object reponds to diameter() method
'''
import unittest


class Wheel:
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


class Gear:
	def __init__(self, **kwargs):
		self.__chainring = kwargs['chainring']
		self.__cog = kwargs['cog']
		self.__wheel = kwargs['wheel']

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

	# The object in the'wheel' variable plays the 'Diameterizable' role.
	def gear_inches(self):
		return self.ratio() * self.wheel.diameter()


# create a player of the Diameterizable role
class DiameterDoube(object):
	def diameter(self):
		return 10


class WheelTest(unittest.TestCase):
	def setUp(self):
		self.wheel = Wheel(26, 1.5)

	def test_implements_the_diameterizable_interface(self):
		callable(self.wheel.diameter)

	def test_calculates_diameter(self):
		self.assertAlmostEqual(self.wheel.diameter(), 29, delta = 1.5)

	print('All wheel tests pass!!!')
	print()


class GearTest(unittest.TestCase):

	def test_calculates_gear_inches(self):
		gear =  Gear(chainring = 52, cog = 11, wheel = DiameterDoube())
		self.assertAlmostEqual(gear.gear_inches(), 47.27, delta = 0.01)

	print('All Gear tests pass!!!')
	print()


if __name__ == '__main__':
	unittest.main() # execute init tests
