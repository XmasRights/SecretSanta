#!/usr/bin/env python

import sys
import random

###############################
# Helpful Functions           #
###############################

def getList(filename):
    content = []
    with open(filename, "r") as f:
        for line in f:
            formatted = line.rstrip('\n').rstrip('\r')
            content.append(formatted)
    return content

def generateSecretSanta(names):
    output = []
    count  = 0
    while output == []:
        namesList = list(names)
        hatList   = list(names)
        recursiveHatPicking (namesList, hatList, output)
        print "Output: " + str(output)
        count = count + 1

    print "Had to run recursion " + str(count) + " times"

    return output

def recursiveHatPicking(names, hatOfNames, output):

    print "Names: " + str(names)
    print "Hat:   " + str(hatOfNames)

    if len(hatOfNames) == 0:
        print "THE HAT IS EMPTY"
        return

    elif len(names) == 1 and hatOfNames[0] == names[0]:
        #if the last name in both lists are identical
        print "NAMES ABORT ON " + str(names[0]) + " and " + hatOfNames[0]
        del output[:]
        return

    pick = removeRandomName(hatOfNames)

    if (pick != names[0]):
        print names[0] + " has picked " + pick
        output.append (names[0] + " has picked " + pick)
        del names[0]
        recursiveHatPicking(names, hatOfNames, output)
    else:
        print "Duplicate " + pick + " and " + names[0]
        print "HAT OF NAMES"
        print hatOfNames
        hatOfNames.append(pick)
        recursiveHatPicking(names, hatOfNames, output)

def removeRandomName(names):
    randNo = random.randrange(0, len(names), 1)
    name = names[randNo]
    del names[randNo]
    return name

###############################
# Main                        #
###############################

if (len(sys.argv) != 2):
    print "Usage: Santa.py <input file name>"
    sys.exit()
else:
    print "Success"

inFile     = sys.argv[1]
namesList  = getList(inFile)

generatedList = generateSecretSanta(namesList)
