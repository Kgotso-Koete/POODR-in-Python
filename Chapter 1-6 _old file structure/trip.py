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

	# prepare each prerarer
	def prepare(preparers):
		for preparer in preparers:
			preparer.prepare_trip()

# when every preparer is a Duck that responds to 'prepare_trip'
class Mechanic(object):
	def prepare_trip(trip):
		return [prepar_bicycle(bicycle) for bicycle in trip.bicycles]

class TripCoordinator(object):
	def prepare_trip(trip):
		return buy_food(trip.customers)

class Driver(object):
	def prepare_trip(trip):
		vehicle = trip.vehicle
		gas_up(vehicle)
		fill_water_tank(vehicle)
		return vehicle

if __name__ == '__main__':
	#create an instance
