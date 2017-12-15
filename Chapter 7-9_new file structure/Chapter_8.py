'''
Tying up Chapter 8
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

# source credit: https://github.com/foobacca/poodr-py/blob/e972e7f3fa33e6f8631fa86df8837da60f7ffefd/bike.py
class PartsFactory(object):
    class Part(object):
        def __init__(self, **kwargs):
            self.name = kwargs['name']
            self.description = kwargs['description']
            self.needs_spare = kwargs['needs_spare']

        def __str__(self):
            uni = "%s: %s" % (self.name, self.description)
            if self.needs_spare:
                uni += " (needs spare)"
            return uni

    @staticmethod
    def build(config, parts_class = Parts):
        return parts_class([PartsFactory._create_part(part_config) for part_config in config])

    @staticmethod
    def _create_part(part_config):
        return PartsFactory.Part(
            name = part_config[0],
            description = part_config[1],
            needs_spare = part_config[2] if len(part_config) > 2 else True)


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

# source credit: https://github.com/foobacca/poodr-py/blob/e972e7f3fa33e6f8631fa86df8837da60f7ffefd/bike.py
def spares_to_string(spares):
    return '[' + ', '.join([str(s) for s in spares]) + ']'

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

    road_parts = PartsFactory.build(road_config)
    road_bike = Bicycle(
        size ='M',
        parts = road_parts)
    print (road_bike.size)
    print (spares_to_string(road_bike.spares()))

    mountain_parts = PartsFactory.build(mountain_config)
    mountain_bike = Bicycle(
        size ='L',
        parts = mountain_parts)
    print (mountain_bike.size)
    print (spares_to_string(mountain_bike.spares()))
