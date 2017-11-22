class Gear:
	# initialize
	def __init__(self, chainring, cog):
		self.chainring = chainring
		self.cog = cog

	# calculate the ratio
	def ratio(self):
		return self.chainring / float(self.cog)

print(Gear(52, 11).ratio())
