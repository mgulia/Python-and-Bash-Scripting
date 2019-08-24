##########################################
#   Author:     Maanus Gulia
#   email:      mgulia@purdue.edu
#   ID:         ee364a15
#   Date:       2/13/19
##########################################

import os   #List of module import statements
import sys  #Each one on a line

#Module level Variables. (Write this statement verbatim.)
######################################################
DataPath = os.path.expanduser("~ee364/DataFolder/Lab05")



def getPinFor(name, date):

    #creates dictionary for names
    nameDict = {}
    filePath = os.path.join(DataPath, "people.dat")
    data = []
    with open(filePath, 'r') as FILE:
        dataFile = FILE.readlines()
    for line in dataFile[2:]:
        data.append(line.split())

    for var1 in data:
        nameDict[var1[0] + " " + var1[1]] = var1[3]

    #print(nameDict)

    #pinInfo has the pin data and dateInfo has the row of dates
    pinInfo = []
    pinPath = os.path.join(DataPath, "pins.dat")
    with open(pinPath, 'r') as FILE2:
        dataFile2 = FILE2.readlines()
    for add in dataFile2[3:]:
        pinInfo.append(add.split())
    #print(pinInfo)

    dataInfo = dataFile2[1].split()
    index = 0
    for idx, found in enumerate(dataInfo):
        if found == date:
            index = idx




    userID = nameDict[name]
    pin = ''
    #print(userID)


    for check in pinInfo:
        if check[0] == userID:
            pin = check[index]

    return(pin)





def getUserOf(pin, date):
    # creates dictionary for names
    nameDict = {}
    filePath = os.path.join(DataPath, "people.dat")
    data = []
    with open(filePath, 'r') as FILE:
        dataFile = FILE.readlines()
    for line in dataFile[2:]:
        data.append(line.split())

    for var1 in data:
        nameDict[var1[0] + " " + var1[1]] = var1[3]

    #print(nameDict)

    # pinInfo has the pin data and dateInfo has the row of dates
    pinInfo = []
    pinPath = os.path.join(DataPath, "pins.dat")
    with open(pinPath, 'r') as FILE2:
        dataFile2 = FILE2.readlines()
    for add in dataFile2[3:]:
        pinInfo.append(add.split())
    #print(pinInfo)

    dataInfo = dataFile2[1].split()
    index = 0
    flag1 = 0
    for idx, found in enumerate(dataInfo):
        if found == date:
            index = idx
            flag1 = 1

    if (flag1 == 0):
        raise ValueError("Date does not exist")

    #print(index)

    userID = ''
    name = ''
    flag2 = 0
    for check in pinInfo:
        if check[index] == pin:
            userID = check[0]
            flag2 = 1

    if (flag2 == 0):
        raise ValueError("Pin doesn't exist")

    for loop in nameDict:
        if nameDict[loop] == userID:
            name = loop

    return(name)





def getUsersOn(date):
    # creates dictionary for names
    nameDict = {}
    filePath = os.path.join(DataPath, "people.dat")
    data = []
    with open(filePath, 'r') as FILE:
        dataFile = FILE.readlines()
    for line in dataFile[2:]:
        data.append(line.split())

    for var1 in data:
        nameDict[var1[0] + " " + var1[1]] = var1[3]

    # print(nameDict)

    # pinInfo has the pin data and dateInfo has the row of dates
    pinInfo = []
    pinPath = os.path.join(DataPath, "pins.dat")
    with open(pinPath, 'r') as FILE2:
        dataFile2 = FILE2.readlines()
    for add in dataFile2[3:]:
        pinInfo.append(add.split())
    # print(pinInfo)

    dataInfo = dataFile2[1].split()
    index = 0
    for idx, found in enumerate(dataInfo):
        if found == date:
            index = idx

    idSet = set()





def getResourcesOn(date):
    filePath = os.path.join(DataPath, "log.dat")
    data = []
    with open(filePath, 'r') as FILE:
        dataFile = FILE.readlines()
    for line in dataFile[3:]:
        data.append(line.split())

    logDict1 = {}
    for loop in data:
        logDict1[loop[0]] = loop[2]



    #print(logDict1)

    #print(data)




def getDifference(slot1, slot2):

    #set up
    filePath = os.path.join(DataPath, "slots.dat")
    data = []
    with open(filePath, 'r') as FILE:
        dataFile = FILE.readlines()
    timeSlot = dataFile[1].split()
    for line in dataFile[3:]:
        data.append(line.split())

    index1 = 0
    index2 = 0
    for idx, first in enumerate(timeSlot):
        if first == slot1:
            index1 = idx
    for idx2, second in enumerate(timeSlot):
        if second == slot2:
            index2 = idx2

    numStudents = 0
    for var in data:
        if(var[index1] == '1' and var[index2] == '0'):
            numStudents += 1

    return(numStudents)




def getCommon(slot1, slot2):
    # set up
    filePath = os.path.join(DataPath, "slots.dat")
    data = []
    with open(filePath, 'r') as FILE:
        dataFile = FILE.readlines()
    timeSlot = dataFile[1].split()
    for line in dataFile[3:]:
        data.append(line.split())

    index1 = 0
    index2 = 0
    for idx, first in enumerate(timeSlot):
        if first == slot1:
            index1 = idx
    for idx2, second in enumerate(timeSlot):
        if second == slot2:
            index2 = idx2

    numStudents = 0
    for var in data:
        if (var[index1] == '1' and var[index2] == '1'):
            numStudents += 1

    return (numStudents)




def helperMissing(slot1):
    # set up
    filePath = os.path.join(DataPath, "slots.dat")
    data = []
    with open(filePath, 'r') as FILE:
        dataFile = FILE.readlines()
    timeSlot = dataFile[1].split()
    for line in dataFile[3:]:
        data.append(line.split())

    index1 = 0
    for idx, first in enumerate(timeSlot):
        if first == slot1:
            index1 = idx

    return (index1)




def getMissing(slots):


    # set up
    filePath = os.path.join(DataPath, "slots.dat")
    data = []
    with open(filePath, 'r') as FILE:
        dataFile = FILE.readlines()
    timeSlot = dataFile[1].split()
    for line in dataFile[3:]:
        data.append(line.split())

    numStudents = 0
    temp = 0
    index = 0
    flag = 0
   # print(data)

    indexList = []
    for done in slots:
        index = helperMissing(done)
        indexList.append(index)

    #print(indexList)

    for var in data:
        for loop in indexList:
            if var[loop] == 0:
                flag += 1
            else:
                flag = 1
                if(flag == len(indexList)):
                    numStudents += 1
        flag = 1

    #print("Num")
    #print(numStudents)
    return(numStudents)


















