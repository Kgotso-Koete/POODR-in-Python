'''
Bicycle sends spares to Parts , Parts sends needs_spare to each Part.
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
    def __init__(self, parts=None):
        self.__parts = parts

    @property
    def parts(self):
        return self.__parts

    def spares(self):
        return [part for part in self.parts if part.needs_spare]


class Part(object):
    def __init__(self,**kwargs):
        self.__name = kwargs['name']
        self.__description = kwargs['description']
        self.__needs_spare = kwargs.get('needs_spare', True)

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @property
    def needs_spare(self):
        return self.__needs_spare


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

    #The following code creates a number of different parts and saves each in an instance variable.
    chain = Part(name ='chain', description ='10-speed')

    road_tire = Part(name = 'tire_size',  description = '23')

    tape = Part(name ='tape_color', description = 'red')

    mountain_tire = Part(name = 'tire_size',  description = '2.1')

    rear_shock = Part(name = 'rear_shock', description = 'Fox')

    front_shock = Part(name = 'front_shock', description = 'Manitou', needs_spare = False)

    # testing instance of road_bike
    road_bike = Bicycle(size = 'L', parts = Parts([chain, road_tire, tape]))
    print(road_bike.size)    # -> 'L'
    print(road_bike.spares())
    # -> [#<Part:0x00000101036770
    #         @name="chain",
    #         @description="10-speed",
    #         @needs_spare=true>,
    #     #<Part:0x0000010102dc60
    #         @name="tire_size",
    #         etc ...

    # testing instance of mountain_bike
    mountain_bike = Bicycle(size = 'L', parts = Parts([chain, mountain_tire, front_shock, rear_shock]))
    print(mountain_bike.size)    # -> 'L'
    print(mountain_bike.spares())
    # -> [#<Part:0x00000101036770
    #         @name="chain",
    #         @description="10-speed",
    #         @needs_spare=true>,
    #     #<Part:0x0000010101b678
    #         @name="tire_size",
    #         etc ...
