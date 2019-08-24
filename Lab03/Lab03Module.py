################################
#   Author: Maanus Gulia
#   email:  mgulia@purdue.edu
#   ID:     ee364a15
#   Date:   1/29/19
################################

import os   # List of module import statements
import sys  # Each one on a line

#Module level Variables. (Write this statement verbatim.)
######################################################
DataPath = os.path.expanduser("~ee364/DataFolder/Lab03")


def getStateByCounty(county):
    countiesPath = os.path.join(DataPath, "counties.dat")
    countiesData = []
    with open(countiesPath, 'r') as FILE3:
        dataFile3 = FILE3.readlines()

    count = 0
    lat = []
    long = []
    for line3 in dataFile3:
        if (count >= 2):
            temp = line3.split(" ")
            countiesData.append(temp)
        count += 1

    flag = 0
    for var3 in countiesData:
        var3[1] = var3[1][1:]
        if (var3[17] == county):
            flag = 1
            lat.append(var3[0])
            long.append(var3[9])

    if(flag == 0):
        raise ValueError("County name does not exist")

    #print(lat)
    #print(long)
        # print(len(var3[2]))
        # var3[2] = var3[3][:nameLength-1]

    #print(countiesData)

    #GOT LONG AND LAT
    coordPath = os.path.join(DataPath, "coordinates.dat")
    coordData = []
    with open(coordPath, 'r') as FILE2:
        dataFile2 = FILE2.readlines()

    count = 0
    for line2 in dataFile2:
        if (count >= 2):
            temp = line2.split("         ")
            coordData.append(temp)
        count += 1

    for var2 in coordData:
        var2[2] = var2[2].replace("    ", "")
        var2[2] = var2[2].replace("\n", "")


    zipCodes = []
    for i in coordData:
        for j in lat:
            for k in long:
                if (i[0] == j and i[1] == k):
                    zipCodes.append(i[2])

    #print(zipCodes)
    #GOT ZIP CODES

    filePath = os.path.join(DataPath, "zip.dat")
    zipData = []
    with open(filePath, 'r') as FILE:
        dataFile = FILE.readlines()
    count = 0
    for line in dataFile:
        if (count >= 2):
            temp = line.split("      ")
            zipData.append(temp)
        count += 1

    flag = 0
    for var in zipData:
        var[0] = var[0].replace(', ', "")
        var[2] = var[2].replace('\n', "")


    states = set()

    for a in zipData:
        for b in zipCodes:
            if (a[2] == b):
                states.add(a[0])

    return (states)





def getCount(state):
    #LabPath = DataPath + os.sep + "Lab03"
    filePath = os.path.join(DataPath, "zip.dat")
    zipData = []
    with open(filePath, 'r') as FILE:
        dataFile = FILE.readlines()
    count = 0
    for line in dataFile:
        if (count >= 2):
            temp = line.split("      ")
            zipData.append(temp)
        count += 1

    zipCodes = []

    flag = 0
    for var in zipData:
        var[0] = var[0].replace(', ', "")
        var[2] = var[2].replace('\n', "")

        if(var[0] == state):
            zipCodes.append(var[2])
            flag = 1

    if(flag == 0):
        raise ValueError("State name does not exist")

    #ZIPCODES[] CONTAIN THE ZIPCODE DATA

    coordPath = os.path.join(DataPath, "coordinates.dat")
    coordData = []
    with open(coordPath, 'r') as FILE2:
        dataFile2 = FILE2.readlines()

    count = 0
    for line2 in dataFile2:
        if (count >= 2):
            temp = line2.split("         ")
            coordData.append(temp)
        count += 1

    lat = []
    long = []
    for var2 in coordData:
        var2[2] = var2[2].replace("    ", "")
        var2[2] = var2[2].replace("\n", "")

    for loop in coordData:
        for inner in zipCodes:
            if (loop[2] == inner):
                lat.append(loop[0])
                long.append(loop[1])

    #LAT[] AND LONG[] HAVE THE CORRESPONDING DATA FROM COORDINATES

    countiesPath = os.path.join(DataPath, "counties.dat")
    countiesData = []
    with open(countiesPath, 'r') as FILE3:
        dataFile3 = FILE3.readlines()

    count = 0
    for line3 in dataFile3:
        if (count >= 2):
            temp = line3.split("        ")
            countiesData.append(temp)
        count += 1

    for var3 in countiesData:
        var3[1] = var3[1][1:]
        #print(len(var3[2]))
        #var3[2] = var3[3][:nameLength-1]

    county = set()

    for loop3 in countiesData:
        for latx in lat:
            for longx in long:
                if (loop3[0] == latx and loop3[1] == longx):
                    county.add(loop3[2])

    num = len(county)

    return (num)


