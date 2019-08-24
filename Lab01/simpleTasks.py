################################
#   Author: Maanus Gulia
#   email: mgulia@purdue.edu
#   ID: ee364a15
#   Date:   January 11, 2019
################################

import os
import sys

#Module level Variables. (Write this statement verbatim.)
######################################################
DataPath = os.path.expanduser("~ee364/DataFolder/Prelab01")



def find(pattern):
    filePath = os.path.join(DataPath, 'sequence.txt')
    with open(filePath, 'r') as FILE:
        sequence = FILE.read()

    patternLength = len(pattern)
    subList = []
    finalList = []
    subString = ''

    for index, value in enumerate(sequence):
        if index == (len(sequence) - len(pattern) + 1):
            break
        subList.append(sequence[index:index+len(pattern)])

    for number in subList:
        flag = 0
        for idx, char in enumerate(pattern):
            if char is 'X' or char is number[idx]:
                continue
            else:
                flag = 1
                break

        if flag is 0:
            finalList.append(number)

    return finalList



def getStreakProduct(sequence, maxSize, product):
    match = []
    subDigits = 1
    reset = 1
    subStr = ''
    subSubDigits = 1

    for var in sequence:
        subStr = subStr + var
        subDigits = 1
        for x in subStr:
            subDigits = subDigits * int(x)
        if (subDigits >= product):
            if subDigits == product and len(subStr)<=maxSize:
                match.append(subStr)


            while subDigits >= product:
                subStr = subStr[1:]
                subDigits = 1
                for y in subStr:
                    subDigits = subDigits * int(y)
                    if subDigits == product and len(subStr)<=maxSize:
                        match.append(subStr)


            subDigits = int(subDigits)

    return match





def writePyramids(filePath, baseSize, count, char):
    pyramidHeight = (baseSize - 1) // 2 + 1
    pyList = []
    pyramidStr = ''
    rowNum = 1
    space = baseSize//2
    with open(filePath, 'w') as FILE:
        while(rowNum<=baseSize):
            pyramidStr = ""
            for i in range(rowNum):
                pyramidStr += char

            pyramidStr.center(baseSize, " ")
            rowNum += 2
            for j in range(count):
                FILE.write(pyramidStr.center(baseSize, " "))
                if j is not count - 1:
                    FILE.write(" ")
            FILE.write("\n")



def getStreaks(sequence, letters):
    allStreaks = []
    streaks = []
    subString = ''
    index = 1

    subString += sequence[0]

    for i in sequence[1:]:
        if sequence[index] == sequence[index-1]:
            subString += sequence[index]
        elif sequence[index] != sequence[index-1]:
            allStreaks.append(subString)
            subString = ''
            subString += sequence[index]

        index = index + 1
    allStreaks.append(subString)

    for j in allStreaks:
        if j[0] in letters:
            streaks.append(j)

    return streaks



def findNames(nameList, part, name):

    matches = []
    nameUpper = name.upper()
    nameLower = name.lower()
    nameStr = nameUpper[0] + nameLower[1:]

    if (part != "F" and part!= "L" and part!= "FL"):
        return matches

    for var in nameList:
        if (part == 'F'):
            if (var.find(nameStr + " ") != -1):
                matches.append(var)
        if (part == 'L'):
            if (var.find(" " + nameStr) != -1):
                matches.append(var)
        if (part == 'FL'):
            if (var.find(nameStr) != -1):
                matches.append(var)

    return matches





def convertToBoolean(num, size):

    list = []
    if (type(num)!=int or type(size)!=int):
        return list

    binary = bin(num)
    binaryStr = binary[2:]

    if (type(num)==int and type(size)==int):
        for var in binaryStr:
            if (var == '1'):
                list.append(True)
            elif (var == '0'):
                list.append(False)

        listSize = len(list)
        xtra = size - listSize

        if (xtra > 0):
            for i in range(xtra):
                list.insert(0, False)

    return list





def convertToInteger(boolList):

    # Verify that the input parameter is a list, return 'None' if not
    if (isinstance(boolList, list) == False):
        strReturn = 'None'
        return strReturn

    # Verify that the list is not empty and return if 'None' if it is
    strReturn = ''
    if (len(boolList) == 0):
        strReturn = 'None'
        return strReturn

    # Verify that all elements are boolean, and return 'None' otherwise
    check = 0
    for var in boolList:
        if (isinstance(var, bool) == False):
            check += 1
    if (check > 0):
        strReturn = 'None'
        return strReturn

    binaryStr = ''
    binaryToInt = 0
    for i in boolList:
        if (i == True):
            binaryStr += '1'
        elif(i == False):
            binaryStr += '0'

    binaryToInt = int(binaryStr, 2)


    return binaryToInt

