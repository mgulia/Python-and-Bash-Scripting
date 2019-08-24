##############################
#   Author: Maanus Gulia
#   email:  mgulia@purdue.edu
#   ID:     ee364a15
#   Date:   2/5/19
##############################

import os   # List of module import statements
import sys  # Each one on a line
from collections import defaultdict

# Module level Variables. (Write this statement verbatim.)
#######################################################
DataPath = os.path.expanduser("~ee364/DataFolder/Lab04")


def getData(provider):

    data = []
    dataDict = defaultdict(float)
    providerPath = DataPath + os.sep + "providers"
    filePath = os.path.join(providerPath, provider + ".dat")
    with open(filePath, 'r') as FILE:
        reportFile = FILE.readlines()
    count = 0
    for line in reportFile:
        if (count >= 3):
            temp = line.split()
            data.append(temp)
        count += 1
    name = ''
    price = 0
    for var in data:
        name = var[0] + " " + var[1]
        var[3] = float(var[3].replace("$", ""))
        price = var[3]
        dataDict[name] = price

    return dict(dataDict)


def getMinAcrossProviders(sbc, change):

    files = os.listdir(DataPath + os.sep + "providers")
    priceSet = set()
    minPrice = 0
    dataDict = {}
    nameDict = {}
    minProvider = ''
    for var in files:
        var = var.replace(".dat", "")
        dataDict = getData(var)
        for x in dataDict:
            if x == sbc:
                priceSet.add(dataDict[x])
                nameDict[var] = dataDict[x]
    minPrice = min(priceSet)
    for key in nameDict:
        if nameDict[key] == minPrice:
            minProvider = key
    if change == 0:
        return minPrice
    if change == 1:
        return minProvider


def getDifference(provider1, provider2):

    files = os.listdir(DataPath + os.sep + "providers")
    if (provider1 + ".dat") not in files:
        raise ValueError("File not in folder")
    if (provider2 + ".dat") not in files:
        raise ValueError("File not in folder")
    prov1Dict = getData(provider1)
    prov2Dict = getData(provider2)
    names1 = set()
    names2 = set()
    finalSet = set()
    for x in prov1Dict:
        names1.add(x)
    for y in prov2Dict:
        names2.add(y)
    for var in names1:
        if var not in names2:
            finalSet.add(var)

    return finalSet



def getPriceOf(sbc, provider):

    files = os.listdir(DataPath + os.sep + "providers")
    if (provider + ".dat") not in files:
        raise ValueError("File not in folder")
    outputPrice = 0
    provDict = getData(provider)
    flag = 0
    for key in provDict:
        if key  == sbc:
            outputPrice = provDict[key]
            flag = 1
    if (flag == 0):
        raise ValueError("SBC does not exist in file")

    return outputPrice



def checkAllPrices(sbcSet):

    dataDict = {}
    t = ()

    minPrice = 0
    minProvider = ''

    for var in sbcSet:
        minPrice = getMinAcrossProviders(var, 0)
        minProvider = getMinAcrossProviders(var, 1)

        t = minPrice, minProvider

        dataDict[var] = t

    return dataDict










