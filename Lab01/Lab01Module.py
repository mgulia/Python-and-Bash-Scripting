###################################
#   Author: Maanus Gulia
#   email: mgulia@purdue.edu
#   ID: ee364a15
#   Date: 1/15/19
###################################

import os #List of module import statements
import sys #Each one on a line

def findLongest():

    countArray = []
    count = 0
    staticNum = 1000000
    tempNum = 0

    for num in range(staticNum):

        #countArrays.append(num)
        count = 1
        tempNum = num +1
        while(tempNum > 1):
           # print ("Temp Num")
           # print (tempNum)
            #print ("Count")
           # print (count)
            if (tempNum % 2 == 0):
                tempNum = tempNum // 2
                count += 1


            elif (tempNum % 2 == 1):
                tempNum = (3*tempNum) + 1
                count += 1


        countArray.append(count)

    max = 0
    tempMax = countArray[1]

    for var in range(len(countArray)):

        if (max < countArray[var]):
            max = countArray[var]

    answer = 1
    for i in range(len(countArray)):
        if (countArray[i] == max):
            answer = i + 1

    #return countArray
    return answer


def findSmallest():

    n1 = 1
    n2 = 0
    n3 = 0
    n4 = 0
    n5 = 0
    n6 = 0

    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    sum5 = 0
    sum6 = 0

    flag  = 0

    smallNum = 0
    n = 0
    while(flag == 0):
   # while(n < 125876):
        n2 = 2 * n1
        n3 = 3 * n1
        n4 = 4 * n1
        n5 = 5 * n1
        n6 = 6 * n1

        #print (n1)

        n1Str = str(n1)
        n2Str = str(n2)
        n3Str = str(n3)
        n4Str = str(n4)
        n5Str = str(n5)
        n6Str = str(n6)

        for a in n1Str:
            sum1 += int(a)
        for b in n2Str:
            sum2 += int(b)
        for c in n3Str:
            sum3 += int(c)
        for d in n4Str:
            sum4 += int(d)
        for e in n5Str:
            sum5 += int(e)
        for f in n6Str:
            sum6 += int(f)



        if (sum1 == sum2 and sum1 == sum3 and sum1 == sum4 and sum1 == sum5 and sum1 == sum6):
            flag == 1
            smallNum = n1
        """
        if (n == 125874):
            print (sum1)
            print ("Sum1")
            print (sum2)
            print ("Sum2")
        """
        n1 += 1
        #n += 1
        sum1 = 0
        sum2 = 0
        sum3 = 0
        sum4 = 0
        sum5 = 0
        sum6 = 0
       # print(n1)
        #print("n1")
    #print (smallNum)
    #print("Small Num")
    return smallNum

#smallestNum = findSmallest()
#print (smallestNum)





