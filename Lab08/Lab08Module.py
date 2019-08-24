##############################
#   Author: Maanus Gulia
#   email:  mgulia@purdue.edu
#   ID:     ee364a15
#   Date:   3/5/19
##############################

import os #List of module import statements
import sys #Each one on a line
import copy

#Module level Variables. (Write this statement verbatim.)
######################################################
DataPath = os.path.expanduser('')

class TimeSpan:

    def __init__(self, weeks, days, hours):
        if (weeks < 0 or days < 0 or hours < 0):
            raise TypeError("The arguments cannot be negative")

        if (hours >= 24):
            temp = hours
            days += temp // 24
            hours = hours % 24

        if days >= 7:
            temp = days
            weeks += temp // 7
            days = days % 7

        self.weeks = weeks
        self.days = days
        self.hours = hours

    def __str__(self):

        hours = self.hours
        days = self.days
        weeks = self.weeks

        if hours < 10:
            hours = '0' + str(self.hours) + 'H'
        else:
            hours = str(self.hours) + 'H'

        days = str(self.days) + 'D'

        if weeks < 10:
            weeks = '0' + str(self.weeks) + 'W'
        else:
            weeks = str(self.weeks) + 'W'

        output = weeks + ' ' + days + ' ' + hours

        return output


    def getTotalHours(self):
        weeks = self.weeks
        days = self.days
        hours = self.hours

        total = 0
        total = (weeks * (7 * 24)) + (days * 24) + hours

        return total

    def __add__(self, other):
        if isinstance(other, TimeSpan) == False:
            raise TypeError("Timespan instance is expected")

        # output = self.clone()
        # output.hours = self.hours + other.hours
        # output.days = self.days + other.days
        # output.weeks = self.weeks + other.weeks

        hours = self.hours + other.hours
        days = self.days + other.days
        weeks = self.weeks + other.weeks

        output = TimeSpan(weeks, days, hours)
        return output

    def __mul__(self, other):

        if (type(other) != int):
            raise TypeError("An integer is expected")

        if (other<= 0):
            raise ValueError("Input must be greater than zero")

        hours = self.hours * other
        weeks = self.weeks * other
        days = self.days * other

        output = TimeSpan(weeks, days, hours)

        return output

    def __rmul__(self, other):
        return self.__mul__(other)











