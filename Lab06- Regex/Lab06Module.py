##################################
#   Author:     Maanus Gulia
#   email:      mgulia@purdue.edu
#   ID:         ee364a15
#   Date:       2/19/19
##################################

import os   # List of module import statements
import sys  # Each one on a line
import re
from pprint import pprint as pp

#Module level Variables. (Write this statement verbatim.)
######################################################
DataPath = os.path.expanduser('')


def extractArguments(commandline):
    pattern = r'[+\\]{1}([a-z]){1}[ ]+([/!?<>=@#$%^&*\(\)\~_\-+\{\}\[\]:;\'\",\.`a-zA-Z0-9]+)'
    mutliple = re.findall(pattern, commandline)

    return (mutliple)




def extractNumerics(sentence):
    pattern = r'[-+]?[\d]{1}[\.]{1}[\d]+[eE]?[-+]?[\d]+|[-+]?[\d]+[\.][\d]+|[-+]?[\d]+'
    multiple = re.findall(pattern, sentence)

    return multiple




