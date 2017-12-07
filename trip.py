'''
Creating a Trip and Bike class without Duck Types
'''

class Trip:
	def __init__(self, bicycles, customers, vehicle):
		self.bicycles = bicycles
		self.customers = customers
		self.vehicle = vehicle

	# mechanic coulc be from any class
	def prepare(mechanic):
		return mechanic.prepare_bicycles(bicycles)

class Mechanic:
	def prepare_all_bicycles(bicycles):
		return [prepare_each_bicycle(bicycle) for each bicycle in bicycles]

	def prepare_each_bicycle(bicycle):
		# some definition of preperation

if __name__ == '__main__':
	#create an instance
