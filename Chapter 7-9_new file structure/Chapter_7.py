'''
Bicycle, Vehicle and Mechanic now inherit from Mixin and any specified class
'''
from datetime import date, timedelta
import inspect

class Schedule(object):
    def is_scheduled(self, schedulable, start_date, end_date):
        stack = inspect.stack()
        the_class = stack[1][0].f_locals["self"].__class__.__name__
        if True:
            return print("This", the_class , "is not scheduled\n between", start_date, " and ", end_date)
        else:
            return False

class ScheduleChecker_Mixin(object):
    @property
    def schedule(self):
        if not hasattr(self, '_schedule'):
            self._schedule = Schedule()
        return self._schedule

    # Return true if this bicycle is available during this (now Bicycle specific) interval.
    def can_be_scheduled(self,start_date, end_date):
        return not self.is_scheduled(
            start_date - timedelta(days=self.lead_days()), end_date)

    # Return the schedule's answer
    def is_scheduled(self, start_date, end_date):
        return self.schedule.is_scheduled(self, start_date, end_date)

    # Return the number of lead_days before a bicycle  can be scheduled.
    def lead_days(self):
        return 0

############## Page 151 ##############
# Bicycle now inherits from ScheduleChecker_Mixin and any other specified Class
class Bicycle(ScheduleChecker_Mixin, object):
    def lead_days(self):
        return 1

class Vehicle(ScheduleChecker_Mixin, object):
    def lead_days(self):
        return 3

class Mechanic(ScheduleChecker_Mixin, object):
    def lead_days(self):
        return 4


if __name__ == '__main__':
    # convert number inputs into dates
    starting = date(2015, 9, 4)
    ending = date(2015, 9, 10)

    # initialize
    b = Bicycle()
    print(b.can_be_scheduled(starting, ending))
    # This Bicycle is not scheduled
    #   between 2015-09-03 and 2015-09-10
    #  => true

    v = Vehicle()
    print(v.can_be_scheduled(starting, ending))
    # This Vehicle is not scheduled
    #   between 2015-09-03 and 2015-09-10
    #  => true

    m = Mechanic()
    print(m.can_be_scheduled(starting, ending))
    # This Mechanic is not scheduled
    #   between 2015-09-03 and 2015-09-10
    #  => true
