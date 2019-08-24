###############################
#   Author: Maanus Gulia
#   email:  mgulia@purdue.edu
#   ID:     ee364a15
#   Date:   1/30/19
###############################


import os   # List of module import statements
import sys  # Each one on a line
from collections import defaultdict

#Module level Variables. (Write this statement verbatim).
######################################################
DataPath = os.path.expanduser("~ee364/DataFolder/Prelab04")

def setReportFile(reportFile):
    temp = []
    reportData = []
    for line2 in reportFile:
        temp = line2.split()
        reportData.append(temp)
    return reportData

def getReportVirus(reportData):
    count = 0
    virus = []
    for var in reportData:
        if (count >= 4):
            virus.append(var[1])
        count += 1
    return virus

#GETS ALL THE DATA FROM TECHNICIANS.DAT
def getTechData():
    MapPath = DataPath + os.sep + "maps"
    filePath = os.path.join(MapPath, 'technicians.dat')
    data = []
    with open(filePath, 'r') as FILE:
        dataFile = FILE.readlines()
    count = 0
    techIds = []
    for line in dataFile:
        if (count >= 2):
            temp = line.split()
            data.append(temp)
            # techIds.append(data[3])
        count += 1
    return data

def getTechID(techName, change):

    techData = getTechData()
    techIds = []
    for var in techData:
        techIds.append(var[3])
    #RETURNS ALL THE IDS
    if change == 0:
        return techIds
    #RETURNS THE ID CORRESPONDING TO TECH NAME
    if change == 1:
        for x in techData:
            if (techName == x[0] + " " + x[1]):
                return x[3]

#RETURNS LIST OF USER IDS OR FILENAME OF REPORT CORRESPONDING TO USER ID
def getReportByID(techID, change):
    temp = []
    userIds = []
    foundReport = list()
    reports = os.listdir(DataPath + os.sep + "reports")
    ReportPath = DataPath + os.sep + "reports"
    for var in reports:
        fileReportPath = os.path.join(ReportPath, var)
        with open(fileReportPath, 'r') as FILER:
            reportFile = FILER.readline()
            temp.append(reportFile[0][9:])
            #\n ***
            if (techID in reportFile):
                foundReport.append(var)

            # if techID in reportFile:
            #foundReport.append(var)
    for x in temp:
        x = x.replace("\n", "")
        userIds.append(x)
    #returns user ids
    if change == 0:
        return userIds
    #returns file name of report corresponding to user id
    if change == 1:
        return foundReport

#RETURNS EVERYTHING FROM LINE 4 BELOW IN A REPORT
def getReportData(reportName):
    temp = []
    data = []
    reportPath = DataPath + os.sep + "reports"
    fileReportPath = os.path.join(reportPath, reportName)
    with open(fileReportPath, 'r') as FILER:
        reportFile = FILER.readlines()
    for line in reportFile[4:]:
        temp = line.split()
        data.append(temp)
    return(data)



def getVirusData():
    VirusPath = DataPath + os.sep + "maps"
    filePath = os.path.join(VirusPath, "viruses.dat")
    data = []
    with open(filePath, 'r') as FILE:
        dataFile = FILE.readlines()
    count = 0
    virusInfo = []
    for line in dataFile:
        if (count >= 2):
            temp = line.split()
            data.append(temp)
        count += 1
    returnData = []
    for x in data:
        x = x[4][1:]
    return data

#gets total cost
def costOfReport(reportName, virusMoney):
    reportData = getReportData(reportName)
    reportInfo = defaultdict(int)
    for trial, virus, units in reportData:
        reportInfo[virus] += int(units)
    totalCost = 0
    for reportKey in reportInfo:
        for virusKey in virusMoney:
            if (virusKey == reportKey):
                totalCost += reportInfo[reportKey] * virusMoney[virusKey]
    #print(totalCost)
    totalCost = format(totalCost, '.4f')
    totalCost = float(totalCost)
    return totalCost

def getVirusFromReport(reportName):
    temp = []
    data = set()
    reportPath = DataPath + os.sep + "reports"
    fileReportPath = os.path.join(reportPath, reportName)
    with open(fileReportPath, 'r') as FILER:
        reportFile = FILER.readlines()
    count = 0
    for line in reportFile:
        if (count >= 4):
            temp = line.split()
            temp = temp[1]
            data.add(temp)
        count += 1
    return (data)

def convertVirusFormat(virusName):
    virusData = getVirusData()
    virusID = ''
    for var in virusData:
        if var[0] == virusName:
            virusID = var[2]
    return (virusID)

def virusIdName(virusID):
    virusData = getVirusData()
    name = ''
    for var in virusData:
        if var[2] == virusID:
            name = var[0]
    return (name)

def virusIdCost(virusID):
    virusData = getVirusData()
    cost = 0
    for var in virusData:
        if var[2] == virusID:
            cost = var[4]
    cost = cost.replace("$", "")
    cost = float(cost)
    return cost

def virusUnitsInReport(reportName, virus):
    reportData = getReportData(reportName)
    units = 0
    for var in reportData:
        if var[1] == virus:
            units += int(var[2])
    return units

# gets cost of 1 speicifc virus in a report
def virusCostInReport(reportName, virusID):
    reportData = getReportData(reportName)
    totalCost = 0
    cost = 0
    numUnits = virusUnitsInReport(reportName, virusID)
    cost = virusIdCost(virusID)
    totalCost = numUnits * cost
    #totalCost = format(totalCost, '.4f')
    #totalCost = float(totalCost)
    return totalCost

def virusCostAcrossAllReports(virusID):
    reports = os.listdir(DataPath + os.sep + "reports")
    #print(reports)
    virusTotalCost = 0
    for var in reports:
        virusTotalCost += virusCostInReport(var, virusID)

    virusTotalCost = round(virusTotalCost, 2)
    # virusTotalCost = format(virusTotalCost, '.4f')
    # virusTotalCost = float(virusTotalCost)
    #print(virusTotalCost)
    return virusTotalCost

def userIdToName(userID):
    techData = getTechData()
    #print(techData)
    name = ''
    for var in techData:
        if var[3] == userID:
            name = var[0] + ' ' + var[1]
    return name

def reportToUserID(reportName):
    temp = []
    data = []
    reportPath = DataPath + os.sep + "reports"
    fileReportPath = os.path.join(reportPath, reportName)
    with open(fileReportPath, 'r') as FILE:
        reportFile = FILE.readlines()
        userID = reportFile[0][9:]
        userID = userID.replace("\n", "")
    return userID

#Part 1
def getTechWork(techName):
    techData = getTechData()
    reportData = []
    techID = getTechID(techName, 1)
    reportName = ''
    reportName = getReportByID(techID, 1) #report name is a list
    #print(reportName)
    for var in reportName:
        reportData.append(getReportData(var))
    #print("ReportData")
    #print(reportData)
    #reportData = getReportData(reportName) #reportData will be a list of list
    info = defaultdict(int)
    #create the dictionary in this part
    value = 0
    name = ''

    for line in reportData:
        for trial, virus, units in line:
            name = virusIdName(virus)
            info[name] += int(units)
    """
    for trial, virus, units in reportData:
        name = virusIdName(virus)
        info[name] += int(units)
    #print(dict(info))
    """
    return dict(info)




#PART 2
def getStrainConsumption(virusName):
    techData = getTechData
    virusID = convertVirusFormat(virusName)
    reports = os.listdir(DataPath + os.sep + "reports")


    #print(reports)
    strain = defaultdict(int)
    units = 0
    userID = ''
    name = ''
    for var in reports:
        units = virusUnitsInReport(var, virusID)
        userID = reportToUserID(var)
        name = userIdToName(userID)
        strain[name] += units
    #print(strain)
    return dict(strain)




#Part 3
def getTechSpending():
    reports = os.listdir(DataPath + os.sep + "reports")
    #print (reports)
    virusData = getVirusData()
    virusMoney = {}
    for x in virusData:
        x[4] = x[4].replace('$', "")
        x[4] = float(x[4])
        virusMoney[x[2]] = x[4]
    #print(virusMoney)
    #print(costOfReport('report_8C8067A7-4210-48DC-8F75-6A9606415CA6.dat', virusMoney))
    info = defaultdict(float)
    name = ''
    userID = ''
    cost = 0
    for var in reports:
        cost = costOfReport(var, virusMoney)
        userID = reportToUserID(var)
        name = userIdToName(userID)
        info[name] += cost
    #print(info)
    for key in info:
        info[key] = round(info[key], 2)

    return dict(info)



def getVirusCostDict():
    VirusPath = DataPath + os.sep + "maps"
    filePath = os.path.join(VirusPath, "viruses.dat")
    data = []
    with open(filePath, 'r') as FILE:
        dataFile = FILE.readlines()[2:]
    count = 0
    virusInfo = []
    virusCostDict = {}
    for line in dataFile:
        temp = line.split()
        virusCostDict[temp[2]] = [temp[0], float(temp[4].lstrip('$'))]

    return virusCostDict

#Part 4
def getStrainCost():
    reports = os.listdir(DataPath + os.sep + "reports")
    totalStrainCost = defaultdict(float)
    virusCostDict = getVirusCostDict()
    Path = DataPath + os.sep + "reports/"
    for report in reports:
        with open(Path + report, "r") as FILE:
            dataFile = FILE.readlines()[4:]
        for line in dataFile:
            trial, virus, units = line.split()
            totalStrainCost[virusCostDict[virus][0]] += virusCostDict[virus][1] * int(units)

    for key in totalStrainCost.keys():
        totalStrainCost[key] = round(totalStrainCost[key], 2)

    return dict(totalStrainCost)



#PART 5
def getAbsentTechs():
    reports = os.listdir(DataPath + os.sep + "reports")
    MapPath = DataPath + os.sep + "maps"
    filePath = os.path.join(MapPath, 'technicians.dat')
    data = []
    with open(filePath, 'r') as FILE:
        dataFile = FILE.readlines()
    count = 0
    techIds = []
    for line in dataFile:
        if(count >= 2):
            temp = line.split()
            data.append(temp)
            #techIds.append(data[3])
        count += 1
    for loopData in data:
        techIds.append(loopData[3])
    userIds = []
    temp = []
    ReportPath = DataPath + os.sep + "reports"
    for var in reports:
        fileReportPath = os.path.join(ReportPath, var)
        with open(fileReportPath, 'r') as FILER:
            reportFile = FILER.readlines()
            #print (reportFile[0])
            temp.append(reportFile[0][9:])
    for x in temp:
        x = x.replace("\n", "")
        userIds.append(x)
    absentIds = set()
    for i in techIds:
        if (i not in userIds):
            absentIds.add(i)
    #print('absent')
    #print(absentIds)
    absentNames = set()
    for a in absentIds:
        for b in data:
            if a == b[3]:
                absentNames.add(b[0] + " " + b[1])

    return (absentNames)



#PART 6
def getUnusedStrains():
    reports = os.listdir(DataPath + os.sep + "reports")
    #print(reports)
    allVirus = {}
    virus = getVirusData()
    for x in virus:
        allVirus[x[0]] = x[2]
    listOfViruses = []
    virusesInReport = getVirusFromReport('report_8C8067A7-4210-48DC-8F75-6A9606415CA6.dat')
    for var in reports:
        temp = getVirusFromReport(var)
        listOfViruses.append(temp)
    unused = set()
    usedVirus = set()
    for key in allVirus:
        for loop in listOfViruses:
            if (allVirus[key] in loop):
                usedVirus.add(allVirus[key])
    for index in allVirus:
        if allVirus[index] not in usedVirus:
            unused.add(index)
    return (unused)











