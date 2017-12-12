'''
Creating a Schedule class
'''
from datetime import date, timedelta
import inspect

class Schedule(object):
    def is_scheduled(self, schedulable, start_date, end_date):
        stack = inspect.stack()
        the_class = stack[1][0].f_locals["self"].__class__.__name__
        if True:
            return print("This", the_class , "is not scheduled between ", start_date, " and ", end_date)
        else:
            return False

############## Page 149 ##############
class Bicycle(object):
    # Inject the Schedule and provide a default
    def __init__(self,**kwargs):
        self.__schedule = kwargs.get('schedule', Schedule())

    # data hiding
    @property
    def schedule(self):
        return self.__schedule

    # Return true if this bicycle is available during this (now Bicycle specific) interval.
    def can_be_scheduled(self,start_date, end_date):
        return not self.is_scheduled(
            start_date - timedelta(days=self.lead_days()), end_date)

    # Return the schedule's answer
    def is_scheduled(self, start_date, end_date):
        return self.schedule.is_scheduled(self, start_date, end_date)

    # Return the number of lead_days before a bicycle  can be scheduled.
    def lead_days(self):
        return 1

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
