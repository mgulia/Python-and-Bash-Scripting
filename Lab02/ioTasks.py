############################
#Author:    Maanus Gulia
#email:     mgulia@purdue.edu
#ID:        ee364a15
#Date:      1/17/2019
############################

import os   # List of module import statements
import sys  # Each one on a line

#Module level Variables. (Write this statement verbatim.)
######################################################
DataPath = os.path.expanduser("~ee364/DataFolder/Prelab02")


#PART 1
def getMaxDifference(symbol):

    if(symbol != 'AAPL' and symbol != 'AMZN' and symbol != 'FB' and symbol !='MSFT' and symbol != 'TSLA'):
        return 'None'

    filePath = os.path.join(DataPath, symbol + '.dat')
    data = []

    with open(filePath, 'r') as FILE:
        dataFile = FILE.readlines()

    count = 0
    for line in dataFile:
        if (count >= 2):
            temp = line.split(',')
            data.append(temp)
        count += 1

    max = float(data[0][4]) - float(data[0][5])
    date = data[0][0]

    for x in data:
        if ((float(x[4]) - float(x[5])) > max):
            max = float(x[4]) - float(x[5])
            date = x[0]

    return date




#PART 2
def getGainPercent(symbol):

    if (symbol != 'AAPL' and symbol != 'AMZN' and symbol != 'FB' and symbol != 'MSFT' and symbol != 'TSLA'):
        return 'None'

    filePath = os.path.join(DataPath, symbol + '.dat')
    data = []

    with open(filePath, 'r') as FILE:
        dataFile = FILE.readlines()

    count = 0
    for line in dataFile:
        if (count >= 2):
            temp = line.split(',')
            data.append(temp)
        count += 1

    percent = 0.0
    total = len(data)
    count = 0

    for x in data:
        if (float(x[1]) > float(x[3])):
            count += 1

    percent = float((count/total) * 100)
    percent = format(percent, '.4f')
    percent = float(percent)

    return percent



#PART 3
def getVolumeSum(symbol, date1, date2):

    if (symbol != 'AAPL' and symbol != 'AMZN' and symbol != 'FB' and symbol != 'MSFT' and symbol != 'TSLA'):
        return 'None'

    filePath = os.path.join(DataPath, symbol + '.dat')
    data = []

    with open(filePath, 'r') as FILE:
        dataFile = FILE.readlines()

    count = 0
    for line in dataFile:
        if (count >= 2):
            temp = line.split(',')
            data.append(temp)
        count += 1

    sum = 0
    volume1 = 0
    volume2 = 0
    strReturn = ''

    if (date1 >= date2):
        return 'None'

    for x in data:
        if (x[0] == date1):
            volume1 = float(x[2])
        if (x[0] == date2):
            volume2 = float(x[2])


    sum = int(volume1 + volume2)

    return sum




#PART 4
def getBestGain(date):

    aaplData = []
    amznData = []
    fbData = []
    msftData = []
    tslaData = []

    #APPLE Data
    filePath = os.path.join(DataPath, 'AAPL.dat')
    with open(filePath, 'r') as FILE:
        dataFile = FILE.readlines()

    count = 0
    for line1 in dataFile:
        if (count >= 2):
            temp = line1.split(',')
            aaplData.append(temp)
        count += 1

    aaplGain = 0
    for a in aaplData:
        if(a[0] == date):
            aaplGain = ((float(a[1]) - float(a[3])) / float(a[3])) * 100


    #AMAZON Data
    filePath = os.path.join(DataPath, 'AMZN.dat')
    with open(filePath, 'r') as FILE:
        dataFile = FILE.readlines()

    count = 0
    for line2 in dataFile:
        if (count >= 2):
            temp = line2.split(',')
            amznData.append(temp)
        count += 1

    amznGain = 0
    for b in amznData:
        if(b[0] == date):
            amznGain = ((float(b[1]) - float(b[3])) / float(b[3])) * 100


    #FaceBook Data
    filePath = os.path.join(DataPath, 'FB.dat')
    with open(filePath, 'r') as FILE:
        dataFile = FILE.readlines()

    count = 0
    for line3 in dataFile:
        if (count >= 2):
            temp = line3.split(',')
            fbData.append(temp)
        count += 1

    fbGain = 0
    for c in fbData:
        if(c[0] == date):
            fbGain = ((float(c[1]) - float(c[3])) / float(c[3])) * 100

    #MICROSFOT Data
    filePath = os.path.join(DataPath, 'MSFT.dat')
    with open(filePath, 'r') as FILE:
        dataFile = FILE.readlines()

    count = 0
    for line4 in dataFile:
        if (count >= 2):
            temp = line4.split(',')
            msftData.append(temp)
        count += 1

    msftGain = 0
    for d in msftData:
        if(d[0] == date):
            msftGain = ((float(d[1]) - float(d[3])) / float(d[3])) * 100


    #TESLA Data
    filePath = os.path.join(DataPath, 'TSLA.dat')
    with open(filePath, 'r') as FILE:
        dataFile = FILE.readlines()

    count = 0
    for line5 in dataFile:
        if (count >= 2):
            temp = line5.split(',')
            tslaData.append(temp)
        count += 1

    tslaGain = 0
    for e in tslaData:
        if(e[0] == date):
            tslaGain = ((float(e[1]) - float(e[3])) / float(e[3])) * 100


    maximum = max(aaplGain, amznGain, fbGain, msftGain, tslaGain)
    maximum = format(maximum, '.4f')
    maximum = float(maximum)

    return maximum





#PART 5
def getAveragePrice(symbol, year):

    if (symbol != 'AAPL' and symbol != 'AMZN' and symbol != 'FB' and symbol != 'MSFT' and symbol != 'TSLA'):
        return 'None'

    filePath = os.path.join(DataPath, symbol + '.dat')
    data = []

    with open(filePath, 'r') as FILE:
        dataFile = FILE.readlines()

    count = 0
    for line in dataFile:
        if (count >= 2):
            temp = line.split(',')
            data.append(temp)
        count += 1

    sum = 0
    volume1 = 0
    volume2 = 0
    strReturn = ''


    for x in data:
        x[0] = x[0][0:4]

    dailyAvg = 0
    annualAvg = 0
    dayCount = 0
    for y in data:
        if(int(y[0]) == year):
            dailyAvg += (float(y[1]) + float(y[3])) / 2
            dayCount += 1

    annualAvg = dailyAvg / dayCount
    annualAvg = format(annualAvg, '.4f')
    annualAvg = float(annualAvg)
    return annualAvg



#PART 6
def getCountOver(symbol, price):

    if (symbol != 'AAPL' and symbol != 'AMZN' and symbol != 'FB' and symbol != 'MSFT' and symbol != 'TSLA'):
        return 'None'

    filePath = os.path.join(DataPath, symbol + '.dat')
    num = 0
    data = []


    with open(filePath, 'r') as FILE:
        dataFile = FILE.readlines()

    count = 0
    for line in dataFile:
        if (count >= 2):
            temp = line.split(',')
            data.append(temp)
        count += 1

    for x in data:
        if(float(x[1]) >= price and float(x[3]) >= price and float(x[4]) >= price and float(x[5]) >= price):
            num += 1

    return num










