'''
There is now an abstract Parts class.
Bicycle is composed of Parts .
Parts has two subclasses, RoadBikeParts and MountainBikeParts.
'''

# Bicycle is now responsible for three things: knowing its size , holding onto its Parts , and answering its spares
class Bicycle(object):
    def __init__(self, **kwargs):
        self.__size = kwargs['size']
        self.__parts = kwargs['parts']

    @property
    def size(self):
        return self.__size

    @property
    def parts(self):
        return self.__parts

    def spares(self):
        return self.parts.spares()

class Parts(object):
    def __init__(self,**kwargs):
        self.__chain = kwargs.get('chain', self.default_chain(self))
        self.__tire_size = kwargs.get('tire_size', self.default_tire_size(self))
        self.post_initialize(**kwargs)

    # data hiding
    @property
    def chain(self):
        return self.__chain

    @property
    def tire_size(self):
        return self.__tire_size

    @staticmethod
    def post_initialize(self,**kwargs): # And implements this
        return None

    def spares(self):
        parent_spares = {'tire_size': self.tire_size, 'chain':self.chain}
        return {**parent_spares, **self.local_spares()}

    def local_spares(self):
        return {}

    @staticmethod
    def default_tire_size(self):
        raise NotImplementedError("This",self.__class__.__name__,\
         "can not respond to :",\
         self.default_tire_size.__name__ )

    @staticmethod
    def default_chain(self):
        return '10-speed'

class RoadBikeParts(Parts):
    def post_initialize(self,**kwargs):
        self.__tape_color = kwargs.get('tape_color', None)

    @property
    def tape_color(self):
        return self.__tape_color

    def local_spares(self):
        return {'tape_color': self.tape_color}

    @staticmethod
    def default_tire_size(self):
        return '23'

class MountainBikeParts(Parts):
    def post_initialize(self,**kwargs):
        self.__front_shock = kwargs.get('front_shock', None)
        self.__rear_shock = kwargs.get('front_shock', None)

    @property
    def front_shock(self):
        return self.__front_shock

    @property
    def rear_shock(self):
        return self.__rear_shock

    def local_spares(self):
        return {'rear_shock': self.rear_shock}

    @staticmethod
    def default_tire_size(self):
        return '2.1'

if __name__ == '__main__':
    # initialize
    road_bike = Bicycle(
    size = 'L',
    parts = RoadBikeParts(tape_color = 'red'))

    print(road_bike.size) # -> 'L'

    print(road_bike.spares())
    # -> {:tire_size   => "23",
    #     :chain       => "10-speed",
    #     :tape_color  => "red"}

    mountain_bike = Bicycle(
    size = 'L',
    parts = MountainBikeParts(front_shock = 'Manitou',
    rear_shock = 'Fox'))

    print(mountain_bike.size) # -> 'L'

    print(mountain_bike.spares())
    # -> {:tire_size   => "2.1",
    #     :chain       => "10-speed",
    #     :rear_shock  => "Manitou"}
