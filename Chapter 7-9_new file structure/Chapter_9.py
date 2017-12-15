'''
Applying unit tests to Gear too
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
		self.__rim = kwargs['rim']
		self.__tire = kwargs['tire']

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

	def ratio(self):
		return self.chainring / float(self.cog)

	def gear_inches(self):
		return self.ratio() * Wheel(self.rim, self.tire).diameter()


class WheelTest(unittest.TestCase):

	def test_calculates_diameter(self):
		wheel = Wheel(26, 1.5)
		self.assertAlmostEqual(wheel.diameter(), 29, delta = 1.5)

class GearTest(unittest.TestCase):

	def test_calculates_gear_inches(self):
		gear =  Gear(chainring = 52, cog = 11, rim = 26, tire = 1.5 )
		self.assertAlmostEqual(gear.gear_inches(), 137.1, delta = 0.01)


if __name__ == '__main__':
	unittest.main()
