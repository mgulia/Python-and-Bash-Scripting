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
DataPath = os.path.expanduser("~ee364/DataFolder/Lab13")

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

    def __init__(self, company, source, destination):

        cost = getCost(source, destination)

        self.company = company
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

    def __add__(self, other):
        if isinstance(other, Package) == False:
            raise TypeError("Wrong type")
        if self.company != other.company:
            raise ValueError("Not of the same company")

    def __radd__(self, other):
        return self.__add__(other)

def extract(input):
    companyPattern = r'"([a-zA-Z_ ]+)"'
    companyName = re.findall(companyPattern, input)
    companyName = companyName[0]

    coordPattern = r'([0-9]{5})'
    coords = re.findall(coordPattern, input)

    source = coords[0]
    dest = coords[1]



    info = []
    info.append(companyName)
    info.append(source)
    info.append(dest)

    return info




def loadPackages():
    filePath = os.path.join(DataPath, "packages.dat")
    with open(filePath, 'r') as FILE:
        dataFile = FILE.readlines()
    #print(dataFile)
    data = []
    count = 0
    for line in dataFile:
        if (count > 0):
            temp = extract(line)
            data.append(temp)
        count += 1


    packageList = []

    for var in data:
        obj = Package(var[0], var[1], var[2])
        packageList.append(obj)














