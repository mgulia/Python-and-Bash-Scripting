##############################
#   Author: Maanus Gulia
#   email:  mgulia@purdue.edu
#   ID:     ee364a15
#   Date:   4/17/19
##############################

import os # List of module import statements
import sys # Each one on a line
from collections import defaultdict
from measurement import calculateDistance
from enum import Enum

# Module level Variables . ( Write this statement verbatim .)
# ######################################################
DataPath = os.path.expanduser('~ee364/DataFolder/Lab14')

def createDict():
    filePath = os.path.join(DataPath, 'locations.dat')
    data = []

    with open(filePath, 'r') as FILE:
        dataFile = FILE.readlines()

    count = 0
    #print(dataFile[0])
    for line in dataFile:
        if (count >= 1):
            temp = line.split(',')
            #print(temp)
            data.append(temp)
        count+=1

    out = defaultdict(str)
    coord = ()

    for var in data:
        temp = var[0]
        var[2] = var[2][2:]
        var[2] = var[2][:-1]
        var[2] = float(var[2])

        temp = var[0][1:]
        temp = temp[:-1]
        #print(temp)

        var[3] = var[3][2:]
        var[3] = var[3][:-1]
        var[3] = float(var[3])

        #print(var[3])
        coord = (var[2], var[3])
        out[temp] = coord

    return out

class Direction(Enum):

    Incoming = 1
    Outgoing = 2
    Both = 3

class Leg:

    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def __str__(self):
        output = ''
        output += self.source[-5:] + ' => ' + self.destination[-5:]
        return output

    def calculateLength(self, locationMap):
        source = self.source[-5:]
        dest = self.destination[-5:]

        zip1 = locationMap[source]
        zip2 = locationMap[dest]

        distance = calculateDistance(zip1, zip2)
        distance = format(distance, '.2f')
        distance = float(distance)

        return distance

class Trip:

    def __init__(self, person, legs):
        self.person = person
        self.legs = legs


    def calculateLength(self, locationMap):

        totalDistance = 0

        for var in self.legs:
            source = var.source[-5:]
            dest = var.destination[-5:]

            zip1 = locationMap[source]
            zip2 = locationMap[dest]

            distance = calculateDistance(zip1, zip2)
            distance = format(distance, '.2f')
            distance = float(distance)

            totalDistance += distance

        totalDistance = format(totalDistance, '.2f')
        totalDistance = float(totalDistance)

        return(totalDistance)

    def getLegsByZip(self, zipCode, dir):

        output = []

        if dir.value == Direction.Incoming.value:
            for x in self.legs:
                if zipCode in x.destination:
                    output.append(x)

        if dir.value == Direction.Outgoing.value:
            for y in self.legs:
                if zipCode in y.source:
                    output.append(y)

        if dir.value == Direction.Both.value:
            for z in self.legs:
                if zipCode in z.destination or zipCode in z.source:
                    output.append(z)

        return (output)

    def getLegsByState(self, zipCode, dir):

        output = []

        if dir.value == Direction.Incoming.value:
            for x in self.legs:
                if zipCode in x.destination:
                    output.append(x)

        if dir.value == Direction.Outgoing.value:
            for y in self.legs:
                if zipCode in y.source:
                    output.append(y)

        if dir.value == Direction.Both.value:
            for z in self.legs:
                if zipCode in z.destination or zipCode in z.source:
                    output.append(z)

        return (output)


class RoundTrip(Trip):

    def __init__(self, person, legs):

        size = len(legs)
        sourceZip = legs[0].source[-5:]
        destZip = legs[size-1].destination[-5:]

        if sourceZip != destZip or size < 2:
            raise ValueError("Wrong input")

        super().__init__(person, legs)



    def getShortestTrip(self, source, destination, stops):

        data = createDict()
        distance1 = 0
        distance2 = 0
        total = 0
        output = []

        for var in stops:
            zip1 = data[source[-5:]]
            zip2 = data[var[-5:]]
            distance1 = calculateDistance(zip1, zip2)

            zip1 = data[var[-5:]]
            zip2 = data[destination[-5:]]
            distance2 = calculateDistance(zip1, zip2)

            total = distance1 + distance2

            output.append(total)

        # minimum = min(output)
        # print (minimum)


        return output



