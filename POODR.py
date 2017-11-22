class Gear:
	# initialize
	def __init__(self, chainring, cog, rim, tire):
		self.chainring = chainring
		self.cog = cog
		self.rim = rim
		self.tire = tire

	# calculate the ratio
	def ratio(self):
		return self.chainring / float(self.cog)

	# calculate gear inches
	def gear_inches(self):
		return self.ratio() * (self.rim + (self.tire * 2))

print(Gear( 52 , 11 , 26 , 1.5).gear_inches())
print(Gear( 52 , 11 , 24 , 1.25).gear_inches())
