############################
#Author:    Maanus Gulia
#email:     mgulia@purdue.edu
#ID:        ee364a15
#Date:      1/17/2019
############################

import os   # List of module import statements
import sys  # Each one on a line
import re

#Module level Variables. (Write this statement verbatim.)
######################################################
DataPath = os.path.expanduser("~ee364/DataFolder/Lab10")

from measurement import calculateDistance


def getTuple(input):
    out = (0, 0)
    var = 0
    filePath = os.path.join(DataPath, "coordinates.dat")
    with open(filePath, 'r') as FILE:
        dataFile = FILE.readlines()
    group = []
    for line in dataFile:
        temp = line.split(",")
        group.append(temp)
    for i in group:
        temp = '"' + input + '"'
        if i[0] == temp:
            var = (float(i[2][2:-1]), float(i[3][2:-1]))

    if var == 0:
        return out
    else:
        return var


def getCost(sourceZip, destinationZip):

    part1 = getTuple(sourceZip)
    part2 = getTuple(destinationZip)

    output = calculateDistance(part1, part2)
    output *= .01

    output = float(format(output, '.2f'))


    return output



class Package:

    def __init__(self, source, destination):

        cost = getCost(source, destination)

        self.source = source
        self.destination = destination
        self.cost = cost

    def __str__(self):

        output = str(self.source) + " => " + str(self.destination) + ", Cost = $" + str(self.cost)

        return output

    def __gt__(self, other):
        if isinstance(other, Package) == False:
            raise TypeError("Type not of Package")

        if self.cost > other.cost:
            return True
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Package) == False:
            raise TypeError("Type not of Package")

        if self.cost < other.cost:
            return True
        else:
            return False

    def __eq__(self, other):
        if isinstance(other, Package) == False:
            raise TypeError("Type not of Package")

        if self.cost == other.cost:
            return True
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, Package) == False:
            raise TypeError("Type not of Package")

        if self.cost != other.cost:
            return True
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, Package) == False:
            raise TypeError("Type not of Package")

        if self.cost != other.cost:
            return True
        else:
            return False

    def __ge__(self, other):
        if isinstance(other, Package) == False:
            raise TypeError("Type not of Package")

        if self.cost >= other.cost:
            return True
        else:
            return False

    def __le__(self, other):
        if isinstance(other, Package) == False:
            raise TypeError("Type not of Package")

        if self.cost <= other.cost:
            return True
        else:
            return False




def getNumberPattern():
    pattern = r'(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])'
    return pattern




def getTagPattern():
    #pattern = r'(?P<url>((http://|https://|ftp://|ftps://)[a-z]+\.[a-z]+\.[a-z]+))'
    #pattern = r'(>(?P<text>(.*?))<)'
    pattern = r'((?P<url>((http://|https://|ftp://|ftps://)[a-z]+\.[a-z]+\.[a-z]+))">(?P<text>(.*?))<)'

    return pattern


