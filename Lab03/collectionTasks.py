###############################################
#   Author:     Maanus Gulia
#   email:      mgulia@purdue.edu
#   ID:         ee364a15
#   Date:       1/23/19
###############################################

import os   # List of module import statements
import sys  # Each one on a line

# Module level Variables. (Write this statement verbatim).
#######################################################
DataPath = os.path.expanduser("~ee364/DataFolder/Prelab03")


#PART 1
def getComponentCountByProject(projectID, componentSymbol):

    MapPath = DataPath + os.sep + "maps"
    CircuitPath = DataPath + os.sep + "circuits"
    #Creates list of data in projects.dat
    filePath = os.path.join(MapPath, "projects.dat")
    projects = []
    with open(filePath, 'r') as FILE:
        dataFile = FILE.readlines()
    count = 0
    for line in dataFile:
        if (count >= 2):
            temp = line.split("          ")
            projects.append(temp)
        count += 1
    for var in projects:
        var[0] = var[0][4:]

    circuits = []

    valueFlag = 0
    for i in projects:
        if (i[1] == projectID + '\n'):
            circuits.append(i[0])
            valueFlag = 1

    if valueFlag == 0:
        raise ValueError("Project ID Provided Does Not Exist")


    flagC = 0
    components = []
    for c in circuits:

        filePathC = os.path.join(CircuitPath, 'circuit_' + c + '.dat')

        with open(filePathC, 'r') as FILEC:
            dataFileC = FILEC.readlines()

        for lineC in dataFileC:
            if (lineC == 'Components:\n'):
                flagC = 1
            if (flagC == 1):
                components.append(lineC)
        flagC = 0


    #Resistor Component
    if componentSymbol == 'R':
        rCount = 0
        filePathR = os.path.join(MapPath, 'resistors.dat')
        with open(filePathR, 'r') as FILER:
            dataFileR = FILER.readlines()
        for comp in dataFileR:

            comp = comp[:7]

            if (('  ' + comp + '\n') in components):
                rCount += 1

        return rCount

    #Capacitor Component
    if componentSymbol == 'C':
        capCount = 0
        filePathCap = os.path.join(MapPath, 'capacitors.dat')
        with open(filePathCap, 'r') as FILECAP:
            dataFileCap = FILECAP.readlines()
        for comp in dataFileCap:

            comp = comp[:7]

            if (('  ' + comp + '\n') in components):
                capCount += 1

        return capCount

    #Inductor Component:
    if componentSymbol == 'I':
        iCount = 0
        filePathI = os.path.join(MapPath, 'inductors.dat')
        with open(filePathI, 'r') as FILEI:
            dataFileI = FILEI.readlines()
        for comp in dataFileI:

            comp = comp[:7]

            if (('  ' + comp + '\n') in components):
                iCount += 1

        return iCount

    if componentSymbol == 'T':
        tCount = 0
        filePathT = os.path.join(MapPath, 'transistors.dat')
        with open(filePathT, 'r') as FILET:
            dataFileT = FILET.readlines()
        for comp in dataFileT:

            comp = comp[:7]

            if (('  ' + comp + '\n') in components):
                tCount += 1

        return tCount



#PART 2
def getComponentCountByStudent(studentName, componentSymbol):

    MapPath = DataPath + os.sep + "maps"
    CircuitPath = DataPath + os.sep + "circuits"

    # Gets student identity
    filePath = os.path.join(MapPath, 'students.dat')
    data = []

    with open(filePath, 'r') as FILE:
        dataFile = FILE.readlines()

    count = 0
    for line in dataFile:
        if (count >= 2):
            temp = line.split()
            data.append(temp)
        count += 1

    identity = ''
    flag = 0
    for var in data:
        if (var[0] + " " + var[1]) == studentName:
            identity = var[3]
            flag = 1


    if (flag == 0):
        raise ValueError("Student Name Does Not Exist")

    projectPath = os.path.join(MapPath, "projects.dat")
    projects = []
    with open(projectPath, 'r') as FILE2:
        dataFile2 = FILE2.readlines()
    count = 0
    for line in dataFile2:
        if (count >= 2):
            temp = line.split("          ")
            projects.append(temp)
        count += 1

    for a in projects:
        a[0] = a[0][4:]

    flagC = 0
    dashFlag = 0
    components = []
    for loop in projects:
        filePathC = os.path.join(CircuitPath, 'circuit_' + loop[0] + '.dat')
        with open(filePathC, 'r') as FILEC:
            dataFileC = FILEC.readlines()

            for lineC in dataFileC:
                if (identity in lineC):
                    flagC = 1
                if(lineC == 'Components:\n'):
                    dashFlag = 1

                if(flagC == 1 and dashFlag == 1 and lineC != 'Components:\n' and lineC != '-------------\n'):
                    components.append(lineC)
            flagC = 0
            dashFlag = 0

    comp = []
    for k in components:
        k = k[2:]
        k = k.replace("\n", "")
        comp.append(k)


    # Resistor Component
    if componentSymbol == 'R':
        rCount = 0
        filePathR = os.path.join(MapPath, 'resistors.dat')
        with open(filePathR, 'r') as FILER:
            dataFileR = FILER.readlines()
        for traverse in dataFileR:

            traverse = traverse[:7]
            if (traverse in comp):
                rCount += 1

        return rCount

    # Inductor Component
    if componentSymbol == 'I':
        iCount = 0
        filePathI = os.path.join(MapPath, 'inductors.dat')
        with open(filePathI, 'r') as FILEI:
            dataFileI = FILEI.readlines()
        for traverseI in dataFileI:

            traverseI = traverseI[:7]

            if (traverseI in comp):
                iCount += 1

        return iCount

    # Capacitor Component
    if componentSymbol == 'C':
        capCount = 0
        filePathCap = os.path.join(MapPath, 'capacitors.dat')
        with open(filePathCap, 'r') as FILECap:
            dataFileCap = FILECap.readlines()
        for traverseCap in dataFileCap:

            traverseCap = traverseCap[:7]

            if (traverseCap in comp):
                capCount += 1

        return capCount

    #Transistor
    if componentSymbol == 'T':
        tCount = 0
        filePathT = os.path.join(MapPath, 'transistors.dat')
        with open(filePathT, 'r') as FILET:
            dataFileT = FILET.readlines()
        for traverseT in dataFileT:

            traverseT = traverseT[:7]

            if (traverseT in comp):
                tCount += 1

        return tCount



#PART 3
def getParticipationByStudent(studentName):

    MapPath = DataPath + os.sep + "maps"
    CircuitPath = DataPath + os.sep + "circuits"

    #Gets student identity
    filePath = os.path.join(MapPath, 'students.dat')
    data = []

    with open(filePath, 'r') as FILE:
        dataFile = FILE.readlines()

    count = 0
    for line in dataFile:
        if(count >= 2):
            temp = line.split()
            data.append(temp)
        count += 1

    identity = ''
    flag = 0
    for var in data:
        if (var[0] + " " + var[1]) == studentName:
            identity = var[3]
            flag = 1

    if (flag == 0):
        raise ValueError("Student Name does not exist")


    projectPath = os.path.join(MapPath, "projects.dat")
    projects = []
    with open(projectPath, 'r') as FILE2:
        dataFile2 = FILE2.readlines()
    count = 0
    for line in dataFile2:
        if (count >= 2):
            temp = line.split("          ")
            projects.append(temp)
        count += 1

    for a in projects:
        a[0] = a[0][4:]

    circuit = ''
    found = False
    projectSet = set()

    for i in projects:
        circuit = i[0]
        found = getParticipationByStudentHelper(circuit, identity)
        if (found == True):
            i[1] = i[1].replace("\n", "")
            projectSet.add(i[1])

    return projectSet


def getParticipationByStudentHelper(circuit, identity):

    MapPath = DataPath + os.sep + "maps"
    CircuitPath = DataPath + os.sep + "circuits"

    filePath = os.path.join(CircuitPath, 'circuit_' + circuit + '.dat')
    found = False

    with open(filePath, 'r') as FILE:
        dataFile = FILE.readlines()

        for line in dataFile:
            if (identity in line):
                found = True

    return found


#PART 4
def getParticipationByProject(projectID):
    # Gets student identity

    MapPath = DataPath + os.sep + "maps"
    CircuitPath = DataPath + os.sep + "circuits"

    filePath = os.path.join(MapPath, 'projects.dat')
    data = []

    with open(filePath, 'r') as FILE:
        dataFile = FILE.readlines()

    count = 0
    for line in dataFile:
        if (count >= 2):
            temp = line.split()
            data.append(temp)
        count += 1

    circuits = []
    valueFlag = 0
    for var in data:
        if (var[1] == projectID):
            circuits.append(var[0])
            valueFlag = 1

    if(valueFlag == 0):
        raise ValueError("Project ID does not exist")

    participants = []
    counterC = 0
    flag = 0
    for i in circuits:
        filePathC = os.path.join(CircuitPath, 'circuit_' + i + '.dat')
        with open(filePathC, 'r') as FILEC:
            dataFileC = FILEC.readlines()

            for lineC in dataFileC:
                if (lineC == 'Components:\n'):
                    flag = 1
                if(counterC >= 2 and flag == 0 ):
                    participants.append(lineC)
                counterC = counterC + 1
        counterC = 0
        flag = 0

    students = set()
    filePathS = os.path.join(MapPath, 'students.dat')
    with open(filePathS, 'r') as FILES:
        dataFileS = FILES.readlines()

    countS = 0
    dataS = []
    for lineS in dataFileS:
        if(countS >= 2):
            temp = lineS.split()
            dataS.append(temp)
        countS += 1

    studentName = ''

    for w in dataS:
        w[0] = w[0][:len(w[0])-1]

        #\N VERY IMPORTANT
        for z in participants:
            if ((w[3]+'\n') == z):
                studentName = w[0] + ", " + w[1]
                students.add(studentName)


    return students



#PART 6
def getProjectByComponent(componentIDs):

    MapPath = DataPath + os.sep + "maps"
    CircuitPath = DataPath + os.sep + "circuits"

    # Creates list of data in projects.dat
    filePath = os.path.join(MapPath, "projects.dat")
    projects = []
    with open(filePath, 'r') as FILE:
        dataFile = FILE.readlines()
    count = 0
    for line in dataFile:
        if (count >= 2):
            temp = line.split("          ")
            projects.append(temp)
        count += 1
    for var in projects:
        var[0] = var[0][4:]

    projectSet = set()

    for x in projects:
        filePathC = os.path.join(CircuitPath, 'circuit_' + x[0] + '.dat')

        with open(filePathC, 'r') as FILEC:
            dataFileC = FILEC.readlines()

        for a in dataFileC:
            for b in componentIDs:

                if('  ' + b + '\n' == a):
                    x[1] = x[1].replace("\n", "")
                    projectSet.add(x[1])

    return(projectSet)



#PART 7
def getCommonByProject(projectID1, projectID2):

    MapPath = DataPath + os.sep + "maps"
    CircuitPath = DataPath + os.sep + "circuits"

    filePath = os.path.join(MapPath, "projects.dat")
    projects = []
    with open(filePath, 'r') as FILE:
        dataFile = FILE.readlines()
    count = 0
    for line in dataFile:
        if (count >= 2):
            temp = line.split("          ")
            projects.append(temp)
        count += 1
    for var in projects:
        var[0] = var[0][4:]



    circuit1 = []
    circuit2 = []

    for var in projects:
        if (var[1] == projectID1 + '\n'):

            filePathC = os.path.join(CircuitPath, 'circuit_' + var[0] + '.dat')

            with open(filePathC, 'r') as FILEC:
                dataFileC = FILEC.readlines()

            compFlag = 0
            for a in dataFileC:
                if (compFlag == 1 and a != '-------------\n'):
                    circuit1.append(a[2:])
                if (a == 'Components:\n'):
                    compFlag = 1

        if (var[1] == projectID2 + '\n'):

            filePathC2 = os.path.join(CircuitPath, 'circuit_' + var[0] + '.dat')

            with open(filePathC2, 'r') as FILEC2:
                dataFileC2 = FILEC2.readlines()

            comp2Flag = 0
            for b in dataFileC2:
                if (comp2Flag == 1 and b != '-------------\n'):
                    circuit2.append(b[2:])
                if (b == 'Components:\n'):
                    comp2Flag = 1


    common = set()

    for c1 in circuit1:
        for c2 in circuit2:
            if (c1 == c2):
                c1 = c1.replace("\n", "")
                common.add(c1)


    return common



#Part 9
def getCircuitByStudent(studentNames):

    MapPath = DataPath + os.sep + "maps"
    CircuitPath = DataPath + os.sep + "circuits"

    # Gets student identity
    filePath = os.path.join(MapPath, 'students.dat')
    data = []

    with open(filePath, 'r') as FILE:
        dataFile = FILE.readlines()

    count = 0
    for line in dataFile:
        if (count >= 2):
            temp = line.split()
            data.append(temp)
        count += 1

    """
    identity = ''
    flag = 0
    for var in data:

        if (var[0] + " " + var[1]) == studentNames:
            identity = var[3]
            flag = 1
        # elif (flag != 1):
        # raise ValueError("Student Name Does Not Exist")
    """

    identity = set()
    flag = 0
    for q in studentNames:

        for var in data:
            if (var[0] + " " + var[1]) == q:
                identity.add(var[3])
                flag = 1

        if (flag == 0):
            raise ValueError("Student Name does not exist")


    projectPath = os.path.join(MapPath, "projects.dat")
    projects = []
    with open(projectPath, 'r') as FILE2:
        dataFile2 = FILE2.readlines()
    count = 0
    for line in dataFile2:
        if (count >= 2):
            temp = line.split("          ")
            projects.append(temp)
        count += 1

    for a in projects:
        a[0] = a[0][4:]

    flagC = 0
    dashFlag = 0
    components = []
    circuitSet = set()

    for loop in projects:
        filePathC = os.path.join(CircuitPath, 'circuit_' + loop[0] + '.dat')
        with open(filePathC, 'r') as FILEC:
            dataFileC = FILEC.readlines()

            for lineC in dataFileC:
                for loopID in identity:
                    if (loopID in lineC):
                        circuitSet.add(loop[0])

    return circuitSet


#PART 10
def getCircuitByComponent(componentIDs):

    MapPath = DataPath + os.sep + "maps"
    CircuitPath = DataPath + os.sep + "circuits"

    # Creates list of data in projects.dat
    filePath = os.path.join(MapPath, "projects.dat")
    projects = []
    with open(filePath, 'r') as FILE:
        dataFile = FILE.readlines()
    count = 0
    for line in dataFile:
        if (count >= 2):
            temp = line.split("          ")
            projects.append(temp)
        count += 1
    for var in projects:
        var[0] = var[0][4:]


    circuitSet = set()


    for x in projects:
        filePathC = os.path.join(CircuitPath, 'circuit_' + x[0] + '.dat')

        with open(filePathC, 'r') as FILEC:
            dataFileC = FILEC.readlines()

        for a in dataFileC:

            for b in componentIDs:

                if('  ' + b + '\n' == a):
                    circuitSet.add(x[0])

    return(circuitSet)



