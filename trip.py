'''
Create new TripCoordinator and Driver classes and\
give them the behavior for which they are responsible.
'''
#Trip preparation becomes more complicated
class Trip(object):
	def __init__(self, bicycles, customers, vehicles):
		self.bicycles = bicycles
		self.customers = customers
		self.vehicles = vehicles

	# prepare trandport mode depending on instance
	def prepare(self, preparers):
		for preparer in preparers:
			if isinstance(preparer, Mechanic):
				preparer.prepare_bicycles(self.bicycles)
			elif isinstance(preparer, TripCoordinator):
				preparer.buy_food(self.customers)
			elif isinstance(preparer, Driver):
				preparer.gas_up(self.vehicle)
				preparer.fill_water_tank(self.vehicle)

# when you introduce TripCoordinator and Driver
class TripCoordinator(object):
	def buy_food(self, customers):
		pass

class Driver(object):
	def gas_up(self, vehicle):
		pass
	def fill_water_tank(self, vehicle):
		pass

if __name__ == '__main__':
	#create an instance
