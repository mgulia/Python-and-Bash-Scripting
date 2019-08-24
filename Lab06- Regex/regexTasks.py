##################################
#Author:  Maanus Gulia
#email:   mgulia@purdue.edu
#ID:      ee364a15
#Date:    2/16/19
##################################

import os
import sys
import re
from pprint import pprint as pp
from uuid import UUID

#Module level Variables. (Write this statement verbatim).
######################################################
DataPath = os.path.expanduser("~ee364/DataFolder/Prelab06")

def getUrlParts(url):
    pattern = r'http://(www\.[a-zA-Z]+\.[a-zA-Z]+)/([a-zA-Z]+)/([a-zA-Z]+)'
    multiple = re.findall(pattern, url)

    return multiple[0]



def getQueryParameters(url):
    pattern = r'([a-zA-Z0-9_]+)=([a-zA-Z0-9.-]+)'
    multiple = re.findall(pattern, url)

    return(multiple)






def getRealMAC(sentence):
    pattern = r'\b[a-zA-Z0-9]{1}[a-zA-Z0-9]{1}[:-][a-zA-Z0-9]{1}[a-zA-Z0-9]{1}[:-][a-zA-Z0-9]{1}[a-zA-Z0-9]{1}[:-][a-zA-Z0-9]{1}[a-zA-Z0-9]{1}[:-][a-zA-Z0-9]{1}[a-zA-Z0-9]{1}[:-][a-zA-Z0-9]{1}[a-zA-Z0-9]{1}'
    multiple = re.findall(pattern, sentence)
    return (multiple[0])





def getData():
    filePath = os.path.join(DataPath, 'Employees.txt')
    data = []
    with open(filePath, 'r') as FILE:
        dataFILE = FILE.readlines()

    return(dataFILE)



def getRejectedEntries():
    data = getData()
    lineData = []
    pattern = r'\b([a-zA-Z]+)(,)? ([a-zA-Z]+)[,; ]+\n'
    for var in data:
        multiple = re.findall(pattern, var)
        if (len(multiple)>0):
            lineData.append(multiple)

    first = ''
    last = ''
    fullName = ''
    output = []
    for x in lineData:
        for y in x:
            if y[1] == ',':
                last = y[0]
                first = y[2]
                fullName = first + " " + last
                output.append(fullName)
            if y[1] == '':
                last = y[2]
                first = y[0]
                fullName = first + " " + last
                output.append(fullName)

    output.sort()
    return(output)




def getEmployeesWithIDs():
    data = getData()
    pattern = r'\b([a-zA-Z]+)(,)? ([a-zA-Z]+)[,; ]+(\{?[a-zA-Z0-9]{8}-?[a-zA-Z0-9]{4}-?[a-zA-Z0-9]{4}-?[a-zA-Z0-9]{4}-?[a-zA-Z0-9]{12}}?)'
    lineData = []
    for var in data:
        multiple = re.findall(pattern, var)
        if (len(multiple)>0):
            lineData.append(multiple)

    output = {}
    first = ''
    last = ''
    name = ''
    ID = ''
    updatedID = ''
    for x in lineData:
        for y in x:
            if y[1] == ',':
                last = y[0]
                first = y[2]
                fullName = first + " " + last
                ID = y[3]
                updatedID = str(UUID(ID))
                output[fullName] = updatedID
            if y[1] == '':
                last = y[2]
                first = y[0]
                fullName = first + " " + last
                ID = y[3]
                updatedID = str(UUID(ID))
                output[fullName] = updatedID

    return(output)




def getEmployeesWithOutIDs():
    data = getData()

    pattern = r'\b([a-zA-Z]+)(,)? ([a-zA-Z]+)[,; ]+((\(?[\d]{3}\)?[- ]?[\d]{3}-?[\d]{4}|(\d){10})|[A-Z][a-z]+$|[A-Za-z]+ [A-Za-z]+$)'
    lineData = []
    for var in data:
        multiple = re.findall(pattern, var)
        if (len(multiple)>0):
            lineData.append(multiple)
    first = ''
    last = ''
    fullName = ''
    output = []

    for x in lineData:
        for y in x:
            if y[1] == ',':
                last = y[0]
                first = y[2]
                fullName = first + " " + last
                output.append(fullName)
            if y[1] == '':
                last = y[2]
                first = y[0]
                fullName = first + " " + last
                output.append(fullName)

    output.sort()
    return(output)



def getEmployeesWithPhones():
    data = getData()
    phonePattern = r'[,; ](\(?[\d]{3}\)?[- ]?[\d]{3}[- ]?[\d]{4})'
    namePattern = r'\b([a-zA-Z]+)(,)? ([a-zA-Z]+)[,; ]'
    output = {}

    first = ''
    last = ''
    fullName = ''
    for var in data:
        multiple = re.findall(phonePattern, var)
        nameData = re.findall(namePattern, var)
        if len(multiple) == 1:
            for x in nameData:
                #print(x[1])
                if (x[1] == ','):
                    last = x[0]
                    first = x[2]
                    fullName = first + " " + last
                    output[fullName] = multiple[0]
                if (x[1] == ''):
                    last = x[2]
                    first = x[0]
                    fullName = first + " " + last
                    output[fullName] = multiple[0]

    return(output)





def getEmployeesWithStates():
    data = getData()
    statePattern = r'([a-zA-Z]+?[ ])?([a-zA-Z]+$)'
    namePattern = r'\b([a-zA-Z]+)(,)? ([a-zA-Z]+)[,; ]'
    output = {}

    first = ''
    last = ''
    fullName = ''
    stateName = ''
    stateFirst = ''
    stateLast = ''
    for var in data:
        multiple = re.findall(statePattern, var)
        nameData = re.findall(namePattern, var)
        if len(multiple) > 0:
            for z in multiple:
                if z[0] == '':
                    stateName = z[1]
                if z[0] != '':
                    stateFirst = z[0]
                    stateLast = z[1]
                    stateName = stateFirst+stateLast
        if len(multiple) == 1:
            for x in nameData:
                if (x[1] == ','):
                    last = x[0]
                    first = x[2]
                    fullName = first + " " + last
                    output[fullName] = stateName
                if (x[1] == ''):
                    last = x[2]
                    first = x[0]
                    fullName = first + " " + last
                    output[fullName] = stateName

    return(output)






