##############################
#   Author: Maanus Gulia
#   email:  mgulia@purdue.edu
#   ID:     ee364a15
#   Date:   2/26/19
##############################

import os #List of module import statements
import sys #Each one on a line

#Module level Variables. (Write this statement verbatim.)
######################################################
DataPath = os.path.expanduser('')

class Rectangle:

    def __init__(self, llPoint, urPoint):
        self._valPoint(llPoint, urPoint)


    def _valPoint(self, llPoint, urPoint):
        if (llPoint[0] < urPoint[0] and llPoint[1] < urPoint[1]):
            self.llPoint = llPoint
            self.urPoint = urPoint
        else:
            raise ValueError("Coordinates of llPoint must be less than coordinates of urPoint")

    def isSquare(self):
        x1 = self.llPoint[0]
        y1 = self.llPoint[1]
        x2 = self.urPoint[0]
        y2 = self.urPoint[1]

        if (x2 - x1 == y2 - y1):
            #return True
            return True
        else:
            return False


    def intersectsWith(self, rect):
        x1 = self.llPoint[0]
        y1 = self.llPoint[1]
        x2 = self.urPoint[0]
        y2 = self.urPoint[1]

        rectX1 = rect.llPoint[0]
        rectY1 = rect.llPoint[1]
        rectX2 = rect.urPoint[0]
        rectY2 = rect.urPoint[1]

        if (rectX1 > x1 and rectX1 < x2 and rectY1 > y1 and rectY1 < y2):
            return True
        elif(rectX1 > x1 and rectX1 < x2 and rectY2 > y1 and rectY2 < y2):
            return True
        elif(rectX2 > x1 and rectX2 < x2 and rectY1 > y1 and rectY1 < y2):
            return True
        elif(rectX2 > x1 and rectX2 < x2 and rectY2 > y1 and rectY2 < y2):
            return True
        else:
            return False

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError("Rectangle 2 is not instance of Rectangle")

        rectX1 = self.llPoint[0]
        rectY1 = self.llPoint[1]
        rectX2 = self.urPoint[0]
        rectY2 = self.urPoint[1]

        otherX1 = other.llPoint[0]
        otherY1 = other.llPoint[1]
        otherX2 = other.urPoint[0]
        otherY2 = other.urPoint[1]

        rectLen = rectY2 - rectY1
        rectWidth = rectX2 - rectX1

        otherLen = otherY2 - otherY1
        otherWidth = otherX2 - otherX1

        rectArea = rectLen * rectWidth
        otherArea = otherLen * otherWidth
        if (rectArea == otherArea):
            return True
        else:
            return False








