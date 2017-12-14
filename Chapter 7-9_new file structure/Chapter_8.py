'''
Creating a Parts Factory
'''

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

# source credit: https://github.com/foobacca/poodr-py/blob/70cb2c92dce917251cebb9e8364e3eb6c57f2ea0/bike.py
def parts_factory(config, part_class = Part, parts_class = Parts):
    return parts_class([
        part_class(
            name = part_config[0],
            description = part_config[1],
            needs_spare = part_config[2] if len(part_config) > 2 else True # checking for False as answer to 'needs spare?'
        ) for part_config in config
    ])

# 2d array to describe bike composition of parts
road_config = [
    ['chain', '10-speed'],
    ['tyre_size', '23'],
    ['tape_colour', 'red'],
]
mountain_config = [
    ['chain', '10-speed'],
    ['tyre_size', '2.1'],
    ['front_shock', 'Manitou', False],
    ['rear_shock', 'Fox'],
]

if __name__ == '__main__':

    road_parts = parts_factory(road_config)
    print(road_parts)
    # -> [#<Part:0x00000101825b70
    #       @name="chain",
    #       @description="10-speed",
    #       @needs_spare=true>,
    #     #<Part:0x00000101825b20
    #       @name="tire_size",
    #          etc ...

    mountain_parts = parts_factory(mountain_config)
    print(mountain_parts)
    # -> [#<Part:0x0000010181ea28
    #        @name="chain",
    #        @description="10-speed",
    #        @needs_spare=true>,
    #     #<Part:0x0000010181e9d8
    #        @name="tire_size",
    #        etc ...
