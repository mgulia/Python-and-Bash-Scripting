##############################
#   Author: Maanus Gulia
#   email:  mgulia@purdue.edu
#   ID:     ee364a15
#   Date:   1/22/19
##############################

import os   #List of module import statements
import sys  #Each one on a line

#Module level Variables. (Write this statement verbatim.)
######################################################
DataPath = os.path.expanduser("~ee364/DataFolder/Lab02")

def getCodeFor(stateName):

    filePath = os.path.join(DataPath, "zip.dat")
    data = []
    zipCodes = []
    emptyList = []

    with open(filePath, 'r') as FILE:
        dataFile = FILE.readlines()

    count = 0
    for line in dataFile:
        if (count >= 2):
            temp = line.split(' ')
            data.append(temp)
        count += 1

    count = 0
    length = 0
    for lineData in data:
        length = len(lineData)
        if (lineData[0] == stateName):
            zipCodes.append(lineData[length-1])



    numZip = []
    for x in zipCodes:
        x = int(x)
        numZip.append(x)

    numZip = sorted(numZip)
    strZip = []

    for y in numZip:
        strZip.append(str(y))

    return(strZip)



def getMinLatitude(stateName):

    filePath = os.path.join(DataPath, "coordinates.dat")
    data = []
    with open(filePath, 'r') as FILE:
        dataFile = FILE.readlines()

    count = 0
    for line in dataFile:
        if (count >= 2):
            temp = line.split(' ')
            data.append(temp)
        count += 1

    #print(data)

    zipCodes = getCodeFor(stateName)

    latitudes = []

    length = 0
    lat = ' '
    zip = ' '
    for i in data:
        length = len(i)
        lat = i[0]
        zip = i[length-1]
        #print(i)

        for j in zipCodes:

            if (int(zip) == int(j)):
                latitudes.append(float(lat))

    minLat = 0
    minLat = min(latitudes)

    return minLat





