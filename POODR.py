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

#initialize
test_gear_1 = Gear( 52 , 11 , 26 , 1.5)
test_gear_2 = Gear( 52 , 11 , 24 , 1.25)

print(test_gear_1.gear_inches())
# -> 137.090909090909
print(test_gear_2.gear_inches())
# -> 125.272727272727
