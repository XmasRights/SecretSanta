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
    hatOfNames = list(names)
    output     = []
    selctions  = recursiveHatPicking (names, hatOfNames, output)

    return output

def recursiveHatPicking(names, hatOfNames, output):
    if len(hatOfNames) == 0:
        print "THE HAT IS EMPTY"
        return output

    elif len(names) == 1 and hatOfNames[0] == names[0]:
        #if the last name in both lists are identical
        print "NAMES ABORT ON " + str(names[0]) + " and " + hatOfNames[0]
        output = []
        return output


    print "HAT OF NAMES before"
    print hatOfNames
    (pick, hatOut) = removeRandomName(hatOfNames)

    print "Hat of Names after removal of " + pick
    print hatOfNames

    if (pick != names[0]):
        print names[0] + " has picked " + pick
        output.append (names[0] + " has picked " + pick)
        del names[0]
        recursiveHatPicking(names, hatOut, output)
    else:
        print "Duplicate " + pick + " and " + names[0]
        print "HATout"
        print hatOut
        print "HAT OF NAMES"
        print hatOfNames


        recursiveHatPicking(names, hatOfNames, output)

def removeRandomName(names):
    randNo = random.randrange(0, len(names), 1)
    name = names[randNo]
    namesOut = list(names)
    del namesOut[randNo]

    return (name, names)

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

print "IN NAMES: "
print namesList

count = 0
while True:
    output = generateSecretSanta (namesList)

    if (output == []):
        break
    else:
        print output
        count += 1

print "Got through " + str(count) + " loops before a fault"
