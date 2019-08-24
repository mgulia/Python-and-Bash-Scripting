##############################
#   Author: Maanus Gulia
#   email:  mgulia@purdue.edu
#   ID:     ee364a15
#   Date:   2/28/19
##############################

import os # List of module import statements
import sys # Each one on a line
import math
import copy
from collections import defaultdict
from collections import UserList
from statistics import mean
from enum import Enum

# Module level Variables . ( Write this statement verbatim .)
# ######################################################
DataPath = os.path.expanduser('')

class Datum:

    def __init__(self, *args):
        self._validateArg(*args)

    def _validateArg(self, *args):
        flag = 0;
        for var in args:
            if (type(var) != float):
                flag = 1;
        if (flag == 0):
            self._storage = args
        else:
            raise TypeError("Argument needs to be float")

    def __str__(self):
        output = '('
        for var in self._storage:
            var = format(var, '.2f')
            output += var + ', '
        output = output[0:len(output)-2]
        output += ')'
        return output

    def __repr__(self):
        return repr(self._storage)

    def __hash__(self):
        return hash(self._storage)

    def distanceFrom(self, next):
        current = []
        other = []

        flag = 0

        for check in next:
            if type(check) != float:
                raise TypeError("Invalid Input")


        for x in self._storage:
            current.append(x)
        for y in next:
            other.append(y)

        difference = abs(len(current) - len(other))

        i = 0
        j = 0
        if difference != 0:
            if len(current) > len(other):
                while i < difference:
                    other.append(0.0)
                    i+=1
            if len(current) < len(other):
                while j < difference:
                    current.append(0.0)
                    j+=1
        x = 0
        sum = 0
        differenceSquared = 0
        distance = 0

        while x < len(current):
            differenceSquared = (current[x] - other[x])**2
            sum += differenceSquared
            x += 1

        distance = math.sqrt(sum)

        return distance


    def clone(self):
        final = copy.deepcopy(self)
        return final

    def __contains__(self, item):
        if type(item) != float:
            raise TypeError("Item is not float")

        if item in self._storage:
            return True
        else:
            return False

    def __len__(self):
        return len(self._storage)

    def __iter__(self):
        return iter(self._storage)

    def __neg__(self):
        other = self.clone()
        other2 = list(other)
        output = []
        for var in other2:
            var = var * -1
            output.append(var)


        output = tuple(output)
        other._storage = output

        return other

    def __getitem__(self, item):
        return self._storage[item]

    def __add__(self, next):


        if isinstance(next, Datum) == True:
            current = list(self._storage)
            other = list(next)
            difference = abs(len(current) - len(other))
            sum = []
            output = self.clone()

            i = 0
            j = 0
            if difference != 0:
                if len(current) > len(other):
                    while i < difference:
                        other.append(0.0)
                        i+=1
                if len(current) < len(other):
                    while j < difference:
                        current.append(0.0)
                        j+=1
            x = 0
            while x < len(current):
                sum.append(current[x] + other[x])
                x += 1

            output._storage = tuple(sum)
            return output

        elif type(next) == float:
            current = list(self._storage)
            newList = []
            for a in current:
                a += next
                newList.append(a)
            output = self.clone()

            output._storage = tuple(newList)
            return output
        else:
            raise TypeError("Argument must be type Datum or float")

    def __radd__(self, other):
        return self.__add__(other)


    def __sub__(self, next):

        if isinstance(next, Datum) == True:
            current = list(self._storage)
            other = list(next)
            difference = abs(len(current) - len(other))
            sum = []
            output = self.clone()

            i = 0
            j = 0
            if difference != 0:
                if len(current) > len(other):
                    while i < difference:
                        other.append(0.0)
                        i+=1
                if len(current) < len(other):
                    while j < difference:
                        current.append(0.0)
                        j+=1
            x = 0
            while x < len(current):
                sum.append(current[x] - other[x])
                x += 1

            output._storage = tuple(sum)
            return output

        elif type(next) == float:
            current = list(self._storage)
            newList = []
            for a in current:
                a -= next
                newList.append(a)
            output = self.clone()

            output._storage = tuple(newList)
            return output
        else:
            raise TypeError("Argument must be type Datum or float")

    def __mul__(self, next):

        if type(next) == float:
            current = list(self._storage)
            newList = []
            for a in current:
                a *= next
                newList.append(a)
            output = self.clone()

            output._storage = tuple(newList)
            return output
        else:
            raise TypeError("Argument must be type float")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, next):

        if (next == 0.0):
            raise ZeroDivisionError("Can't divide by zero")

        if type(next) == float:
            current = list(self._storage)
            newList = []
            for a in current:
                a /= next
                newList.append(a)
            output = self.clone()

            output._storage = tuple(newList)
            return output
        else:
            raise TypeError("Argument must be type float")

    def __gt__(self, other):

        if isinstance(other, Datum) == False:
            raise TypeError("Input not of type Datum")

        current = list(self._storage)
        input = list(other._storage)

        x = 0
        y = 0
        sum = 0
        differenceSquared = 0
        distance = 0

        while x < len(current):
            differenceSquared = (current[x]) ** 2
            sum += differenceSquared
            x += 1

        distanceCurrent = math.sqrt(sum)

        sum = 0
        differenceSquared = 0
        distance = 0

        while y < len(input):
            differenceSquared = (input[y]) ** 2
            sum += differenceSquared
            y += 1

        distanceInput = math.sqrt(sum)

        if(distanceCurrent > distanceInput):
            return True
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Datum) == False:
            raise TypeError("Input not of type Datum")

        current = list(self._storage)
        input = list(other._storage)

        x = 0
        y = 0
        sum = 0
        differenceSquared = 0
        distance = 0

        while x < len(current):
            differenceSquared = (current[x]) ** 2
            sum += differenceSquared
            x += 1

        distanceCurrent = math.sqrt(sum)

        sum = 0
        differenceSquared = 0
        distance = 0

        while y < len(input):
            differenceSquared = (input[y]) ** 2
            sum += differenceSquared
            y += 1

        distanceInput = math.sqrt(sum)

        if(distanceCurrent < distanceInput):
            return True
        else:
            return False

    #EQUAL TO
    def __eq__(self, other):
        if isinstance(other, Datum) == False:
            raise TypeError("Input not of type Datum")

        current = list(self._storage)
        input = list(other._storage)

        x = 0
        y = 0
        sum = 0
        differenceSquared = 0
        distance = 0

        while x < len(current):
            differenceSquared = (current[x]) ** 2
            sum += differenceSquared
            x += 1

        distanceCurrent = math.sqrt(sum)

        sum = 0
        differenceSquared = 0
        distance = 0

        while y < len(input):
            differenceSquared = (input[y]) ** 2
            sum += differenceSquared
            y += 1

        distanceInput = math.sqrt(sum)

        if(distanceCurrent == distanceInput):
            return True
        else:
            return False

    #NOT EQUAL TO
    def __ne__(self, other):
        if isinstance(other, Datum) == False:
            raise TypeError("Input not of type Datum")

        current = list(self._storage)
        input = list(other._storage)

        x = 0
        y = 0
        sum = 0
        differenceSquared = 0
        distance = 0

        while x < len(current):
            differenceSquared = (current[x]) ** 2
            sum += differenceSquared
            x += 1

        distanceCurrent = math.sqrt(sum)

        sum = 0
        differenceSquared = 0
        distance = 0

        while y < len(input):
            differenceSquared = (input[y]) ** 2
            sum += differenceSquared
            y += 1

        distanceInput = math.sqrt(sum)

        if(distanceCurrent != distanceInput):
            return True
        else:
            return False

    #GREATER THAN OR EQUAL TO
    def __ge__(self, other):
        if isinstance(other, Datum) == False:
            raise TypeError("Input not of type Datum")

        current = list(self._storage)
        input = list(other._storage)

        x = 0
        y = 0
        sum = 0
        differenceSquared = 0
        distance = 0

        while x < len(current):
            differenceSquared = (current[x]) ** 2
            sum += differenceSquared
            x += 1

        distanceCurrent = math.sqrt(sum)

        sum = 0
        differenceSquared = 0
        distance = 0

        while y < len(input):
            differenceSquared = (input[y]) ** 2
            sum += differenceSquared
            y += 1

        distanceInput = math.sqrt(sum)

        if(distanceCurrent >= distanceInput):
            return True
        else:
            return False

    #LESS THAN OR EQUAL TO
    def __le__(self, other):
        if isinstance(other, Datum) == False:
            raise TypeError("Input not of type Datum")

        current = list(self._storage)
        input = list(other._storage)

        x = 0
        y = 0
        sum = 0
        differenceSquared = 0
        distance = 0

        while x < len(current):
            differenceSquared = (current[x]) ** 2
            sum += differenceSquared
            x += 1

        distanceCurrent = math.sqrt(sum)

        sum = 0
        differenceSquared = 0
        distance = 0

        while y < len(input):
            differenceSquared = (input[y]) ** 2
            sum += differenceSquared
            y += 1

        distanceInput = math.sqrt(sum)

        if(distanceCurrent <= distanceInput):
            return True
        else:
            return False





class Data(UserList):

    def __init__(self, input = None):

        emptyList = []
        if input is None:
            super().__init__(emptyList)
        else:
            for var in input:
                if isinstance(var, Datum) == False:
                    raise TypeError("Each element in list must be of type Datum")
            super().__init__(input)

    def computeBounds(self):
        list1 = self

        size = 0
        sizeList = []
        maxSize = 0
        for var1 in list1:
            size = len(var1)
            sizeList.append(size)

        maxSize = max(sizeList)
        fixedList = []
        for var2 in list1:
            fixedList.append(list1.helperPadding(var2, maxSize))



        data = defaultdict(str)
        fixedData = {}

        for var3 in fixedList:
            for idx, var3 in enumerate(var3):
                data[str(idx)] += str(var3) + ","

        fixedData = self.convertDictToFloats(data)

        minList = []
        maxList = []
        temp = []
        for var4 in fixedData:
            minList.append(min(fixedData[var4]))
            maxList.append(max(fixedData[var4]))

        output = []

        minDatum = Datum(*minList)
        maxDatum = Datum(*maxList)
        output.append(minDatum)
        output.append(maxDatum)
        output = tuple(output)


        return (output)
    

    def computeMean(self):
        list1 = self

        size = 0
        sizeList = []
        maxSize = 0
        for var1 in list1:
            size = len(var1)
            sizeList.append(size)

        maxSize = max(sizeList)
        fixedList = []
        for var2 in list1:
            fixedList.append(list1.helperPadding(var2, maxSize))



        data = defaultdict(str)
        fixedData = {}

        for var3 in fixedList:
            for idx, var3 in enumerate(var3):
                data[str(idx)] += str(var3) + ","

        fixedData = self.convertDictToFloats(data)


        avgList = []
        temp = []
        for var4 in fixedData:
            avgList.append(mean(fixedData[var4]))

        output = []

        avgDatum = Datum(*avgList)

        return (avgDatum)


    def helperPadding(self, data, maxSize):
        i = 0
        difference = maxSize - len(data)
        list1 = list(data)
        if len(data) != maxSize:
            while i < difference:
                list1.append(0.0)
                i += 1
        output = tuple(list1)

        return output

    def convertDictToFloats(self, data):
        temp = []
        tempList = []
        newList = []
        for var in data:
            tempList = []
            newList = []
            temp = data[var].split(',')
            temp = temp[0:len(temp) -1]
            for loop in temp:
                loop = float(loop)
                newList.append(loop)
            data[var] = newList
        return (data)

    def append(self, input):
        if isinstance(input, Datum) == False:
            raise TypeError("Input must be of type Datum")
        super().append(input)

    def count(self, input):
        if isinstance(input, Datum) == False:
            raise TypeError("Input must be of type Datum")
        return (super().count(input))

    def index(self, x: int, input):
        if isinstance(input, Datum):
            raise TypeError("Input must be of type Datum")
        return (super().index(x, input))


    def insert(self, x: int, input):
        if isinstance(input, Datum) == False:
            raise TypeError("Input must be of type Datum")
        return (super().insert(x, input))

    def remove(self, input):
        if isinstance(input, Datum) == False:
            raise TypeError("Input must be of type Datum")
        super().insert(input)

    def __setitem__(self, key, value):
        if isinstance(value, Datum) == False:
            raise TypeError("Input must be of type Datum")
        super().__setitem__(key, value)


    def extend(self, input):
        if isinstance(input, Datum) == False:
            raise TypeError("Input must be of type Datum")
        super().extend(input)







class DataClass(Enum):
    Class1 = 1
    Class2 = 2

class DataClassifier:

    def __init__(self, group1, group2):

        if isinstance(group1, Data) == False:
            raise TypeError("Must be of type Data")
        if isinstance(group2, Data) == False:
            raise TypeError("Must be of type Data")

        if group1 is None:
            raise ValueError("group 1 cannot be empty")
        if group2 is None:
            raise ValueError("group2 cannot be empty")

        self._class1 = group1
        self._class2 = group2

    def classify (self, input):

        data1 = self._class1
        data2 = self._class2
        space1 = 0
        space2 = 0

        i = 0
        for var in data1:
            space1 += self.distance(var, input)
            i += 1
        avg1 = space1 / i

        j = 0
        for var2 in data2:
            space2 += self.distance(var2, input)
            j += 1
            avg2 = space2 / j


        if avg1 < avg2:
            return DataClass.Class1
        else:
            return DataClass.Class2



    def distance(self, coord1, coord2):
        length1 = len(coord1)
        length2 = len(coord2)

        coord1 = list(coord1)
        coord2 = list(coord2)

        difference = abs(length1 - length2)

        i = 0
        j = 0
        if difference != 0:
            if length1 > length2:
                while i < difference:
                    coord2.append(0.0)
                    i += 1
            if length1 < length2:
                while j < difference:
                    coord1.append(0.0)
                    j += 1

        x = 0
        sum = 0
        differenceSquared = 0
        distance = 0

        while x < len(coord1):
            differenceSquared = (coord1[x] - coord2[x]) ** 2
            sum += differenceSquared
            x += 1

        distance = math.sqrt(sum)

        return distance

