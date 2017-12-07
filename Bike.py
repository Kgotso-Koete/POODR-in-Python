#create a GearWrapper class to interface with Gear created in external module
class GearWrapper(object):
    @classmethod
    def gear(self, **kwargs):
        from POODR import Gear
        # return an instance of Gear
        return Gear(kwargs.get('chainring'), kwargs.get('cog'), kwargs.get('wheel'))

if __name__ == '__main__':
    from POODR import Wheel
    ## Gear expects variable number of key word arguments
    new_gear = GearWrapper.gear(chainring=52, cog=11, wheel=Wheel(26, 1.5))
    #expect -----> 137.0909090909091
    print(new_gear.gear_inches())
