
#######################################################
#   Author:     Maanus Gulia
#   email:      mgulia@purdue.edu
#   ID:         ee364a15
#   Date:       3/29/19
#######################################################

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from BasicUI import *
import re
import math


class Consumer(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(Consumer, self).__init__(parent)

        self.setupUi(self)
        self.txtElements = [self.txtStudentID, self.txtStudentName, self.txtComponentName_20, self.txtComponentName_19, self.txtComponentName_18, self.txtComponentName_17, self.txtComponentName_16, self.txtComponentName_15, self.txtComponentName_14, self.txtComponentName_13, self.txtComponentName_12, self.txtComponentName_11, self.txtComponentName_10, self.txtComponentName_9, self.txtComponentName_8, self.txtComponentName_7, self.txtComponentName_6, self.txtComponentName_5, self.txtComponentName_4, self.txtComponentName_3, self.txtComponentName_2, self.txtComponentName_1, self.txtComponentCount_20, self.txtComponentCount_19, self.txtComponentCount_18, self.txtComponentCount_17, self.txtComponentCount_16, self.txtComponentCount_15, self.txtComponentCount_14, self.txtComponentCount_13, self.txtComponentCount_12, self.txtComponentCount_11, self.txtComponentCount_10, self.txtComponentCount_9, self.txtComponentCount_8, self.txtComponentCount_7, self.txtComponentCount_6, self.txtComponentCount_5, self.txtComponentCount_4, self.txtComponentCount_3, self.txtComponentCount_2, self.txtComponentCount_1]
        self.chkGraduate.stateChanged.connect(self.enable_save)
        self.btnClear.setDisabled(False)
        self.btnLoad.setDisabled(False)
        self.btnSave.setDisabled(True)
        self.cboCollege.currentIndexChanged.connect(self.enable_save)
        for var in self.txtElements:
            var.textChanged.connect(self.enable_save)

        self.btnClear.clicked.connect(self.clear_data)
        self.btnLoad.clicked.connect(self.loadData)
        self.btnSave.clicked.connect(self.save_data)


    def clear_data(self):

        self.cboCollege.setCurrentIndex(0)
        self.chkGraduate.setChecked(False)
        for var in self.txtElements:
            var.setText('')
        self.btnSave.setDisabled(True)
        self.btnLoad.setDisabled(False)


    def enable_save(self):
        self.btnLoad.setDisabled(True)
        self.btnSave.setDisabled(False)



    def save_data(self):

        gradState = self.chkGraduate.checkState()
        #print(gradState)
        studentName = self.txtStudentName.text()
        #print(studentName)
        collegeMajor = self.cboCollege.currentText()
        #print(collegeMajor)
        studentID = self.txtStudentID.text()
        #print(studentID)

        if (gradState == 0):
            gradState = "false"
        else:
            gradState = "true"

        compName = [self.txtComponentName_1, self.txtComponentName_2, self.txtComponentName_3, self.txtComponentName_4, self.txtComponentName_5, self.txtComponentName_6, self.txtComponentName_7, self.txtComponentName_8, self.txtComponentName_9, self.txtComponentName_10, self.txtComponentName_11, self.txtComponentName_12, self.txtComponentName_13, self.txtComponentName_14, self.txtComponentName_15, self.txtComponentName_16, self.txtComponentName_17, self.txtComponentName_18, self.txtComponentName_19, self.txtComponentName_20]
        compNameVal = []
        for var1 in compName:
            temp = var1.text()
            compNameVal.append(temp)

        #print(compNameVal)

        count = [self.txtComponentCount_1, self.txtComponentCount_2, self.txtComponentCount_3, self.txtComponentCount_4, self.txtComponentCount_5, self.txtComponentCount_6, self.txtComponentCount_7, self.txtComponentCount_8, self.txtComponentCount_9, self.txtComponentCount_10, self.txtComponentCount_11, self.txtComponentCount_12, self.txtComponentCount_13, self.txtComponentCount_14, self.txtComponentCount_15, self.txtComponentCount_16, self.txtComponentCount_17, self.txtComponentCount_18, self.txtComponentCount_19, self.txtComponentCount_20]
        countVal = []
        for var2 in count:
            temp = var2.text()
            countVal.append(temp)

        #print(countVal)

        with open('target.xml', 'w') as FILE:
            FILE.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            FILE.write("<Content>\n")
            FILE.write('    <StudentName graduate="' + gradState + '">' + studentName + '</StudentName>\n')
            FILE.write('    <StudentID>' + studentID + '</StudentID>\n')
            FILE.write('    <College>' + collegeMajor + '</College>\n')
            FILE.write('    <Components>\n')

            for idx, x in enumerate(compNameVal):
                if compNameVal[idx] != "" and compNameVal[idx] != "":
                    FILE.write('        <Component name="' + compNameVal[idx] + '" count="' + countVal[idx] + '" />\n')

            FILE.write('    </Components>\n')
            FILE.write('</Content>\n')

            # .checkState # check box
            # .text # text fileds
            # .currentText #cbocollege



    def loadData(self):
        """
        *** DO NOT MODIFY THIS METHOD! ***
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        You must modify the method below.
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadDataFromFile(filePath)

    def loadDataFromFile(self, filePath):
        """
        Handles the loading of the data from the given file name. This method will be invoked by the 'loadData' method.
        
        *** YOU MUST USE THIS METHOD TO LOAD DATA FILES. ***
        *** This method is required for unit tests! ***
        """

        #pass

        with open(filePath, 'r') as FILE:
            dataFile = FILE.readlines()

        #print(dataFile)

        namePattern = r'>(.*)</StudentName>'
        studentName = re.findall(namePattern, dataFile[2])
        self.txtStudentName.setText(studentName[0])


        idPattern = r'<StudentID>(.*)</StudentID>'
        idName = re.findall(idPattern, dataFile[3])
        self.txtStudentID.setText(idName[0])



        collegePattern = r'<College>(.*)</College>'
        collegeName = re.findall(collegePattern, dataFile[4])

        if collegeName[0] == "Aerospace Engineering":
            self.cboCollege.setCurrentIndex(1)
        elif collegeName[0] == "Civil Engineering":
            self.cboCollege.setCurrentIndex(2)
        elif collegeName[0] == "Computger Engineering":
            self.cboCollege.setCurrentIndex(3)
        elif collegeName[0] == "Electrical Engineering":
            self.cboCollege.setCurrentIndex(4)
        elif collegeName[0] == "Industrial Engineering":
            self.cboCollege.setCurrentIndex(5)
        elif collegeName[0] == "Mechanical Enigneering":
            self.cboCollege.setCurrentIndex(6)

        if 'true' in dataFile[2]:
            self.chkGraduate.setChecked(True)

        else:
            self.chkGraduate.setChecked(False)

        countPattern = r'<Component name=.* count="([0-math.inf]+)" />'
        entireString = ''
        for idx, var in enumerate(dataFile):
            entireString += dataFile[idx]
        #print(entireString)

        countData = re.findall(countPattern, entireString)
        #print(countData)

        textPattern = r'<Component name="(.*)" count="[0-math.inf]+" />'
        textData = re.findall(textPattern, entireString)
        #print(textData)

        x = 1
        while (x <= 20 and x < len(countData)+1):
        #while(x <= 20):
            if x==1:
                self.txtComponentCount_1.setText(countData[x - 1])
                self.txtComponentName_1.setText(textData[x-1])
            elif x==2:
                self.txtComponentCount_2.setText(countData[x - 1])
                self.txtComponentName_2.setText(textData[x-1])
            elif x==3:
                self.txtComponentCount_3.setText(countData[x - 1])
                self.txtComponentName_3.setText(textData[x-1])

            elif x==4:
                self.txtComponentCount_4.setText(countData[x - 1])
                self.txtComponentName_4.setText(textData[x-1])

            elif x==5:
                self.txtComponentCount_5.setText(countData[x - 1])
                self.txtComponentName_5.setText(textData[x-1])

            elif x==6:
                self.txtComponentCount_6.setText(countData[x - 1])
                self.txtComponentName_6.setText(textData[x-1])

            elif x==7:
                self.txtComponentCount_7.setText(countData[x - 1])
                self.txtComponentName_7.setText(textData[x-1])

            elif x==8:
                self.txtComponentCount_8.setText(countData[x - 1])
                self.txtComponentName_8.setText(textData[x-1])

            elif x==9:
                self.txtComponentCount_9.setText(countData[x - 1])
                self.txtComponentName_9.setText(textData[x-1])

            elif x==10:
                self.txtComponentCount_10.setText(countData[x - 1])
                self.txtComponentName_10.setText(textData[x-1])

            elif x==11:
                self.txtComponentCount_11.setText(countData[x - 1])
                self.txtComponentName_11.setText(textData[x-1])

            elif x == 12:
                self.txtComponentCount_12.setText(countData[x - 1])
                self.txtComponentName_12.setText(textData[x-1])

            elif x == 13:
                self.txtComponentCount_13.setText(countData[x - 1])
                self.txtComponentName_13.setText(textData[x-1])

            elif x == 14:
                self.txtComponentCount_14.setText(countData[x - 1])
                self.txtComponentName_14.setText(textData[x-1])

            elif x == 15:
                self.txtComponentCount_15.setText(countData[x - 1])
                self.txtComponentName_15.setText(textData[x-1])

            elif x == 16:
                self.txtComponentCount_16.setText(countData[x - 1])
                self.txtComponentName_16.setText(textData[x-1])

            elif x == 17:
                self.txtComponentCount_17.setText(countData[x - 1])
                self.txtComponentName_17.setText(textData[x-1])

            elif x == 18:
                self.txtComponentCount_18.setText(countData[x - 1])
                self.txtComponentName_18.setText(textData[x-1])

            elif x == 19:
                self.txtComponentCount_19.setText(countData[x - 1])
                self.txtComponentName_19.setText(textData[x-1])

            elif x == 20:
                self.txtComponentCount_20.setText(countData[x - 1])
                self.txtComponentName_20.setText(textData[x-1])

            x += 1
        #     print(x)
        # print(textData[16])
        # print(countData[16])









if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()
