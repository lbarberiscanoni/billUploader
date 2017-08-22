import requests
import json
import subprocess

#find all teh files and put them in a list
rawLegislationList = subprocess.check_output("find Legislation2/ -name " + "*.txt", shell=True)
legislationList = [n.replace("Legislation2//", "") for n in rawLegislationList.split()]
for legislation in legislationList:
    with open ("Legislation2/" + legislation, "r") as file:
        current = file.read()
        new = current.split("\014")

        def getIndex(a):
            indexNumber = new.index(a)
            return indexNumber

        def showIndex(a):
            print "Index of " + str(a) + " " + str(getIndex(a))

        def getAllIndices(listToCheck, stringToCheck):
            listOfIndices = []
            for i, j in enumerate(listToCheck):
                if j == stringToCheck:
                    listOfIndices.append(i)
            print listOfIndices
            print str(len(listOfIndices))

        print len(new)
        for bill in new:
            print "----------------------------"
            billSections = bill.split("\n")
        with open(legislation, "w") as file:
            file.write((new))

def doStuff():
    with open("Legislation2/" + bill, "r") as file:
        current = file.read()
        #remove this line that is not at all needed in the database
        new = current.replace("BE IT HEREBY ENACTED BY THE YMCA MODEL LEGISLATURE OF SOUTH CAROLINA", "").split()

        def getIndex(a):
            indexNumber = new.index(a)
            return indexNumber

        def showIndex(a):
            print "Index of " + str(a) + " " + str(getIndex(a))

        print "Dissected bill:"
        print new

        authorName = new[getIndex("Name:") + 1: getIndex("Last-Name:")][0]
        authorLastName = new[getIndex("Last-Name:") + 1: getIndex("School:")][0]
        authorID = authorName + "-" + authorLastName
        print authorID

        authorSchool = new[getIndex("School:") + 1: getIndex("A-Bill-to:")][0]
        print authorSchool

        billTitle = " ".join(new[getIndex("A-Bill-to:") + 1: getIndex("Section1:")]).replace(" ", "-")
        print billTitle

        section1 = " ".join(new[getIndex("Section1:") + 1: getIndex("Section2:")])
        print section1

        section2 = " ".join(new[getIndex("Section2:") + 1: getIndex("Section3:")])
        print section2

        section3 = " ".join(new[getIndex("Section3:") + 1: getIndex("Section4:")])
        print section3

        section4 = " ".join(new[getIndex("Section4:") + 1: getIndex("Section5:")])
        print section4

        section5 = new[getIndex("Section5:") + 1]
        print section5

        bill = {
                "authorID": authorID,
                "school": authorSchool,
                "billTitle": billTitle,
                "section1": section1,
                "section2": section2,
                "section3": section3,
                "section4": section4,
                "section5": section5,
                "billLocation": "not yet sorted",
                "billStatus": "not yet sorted",
                "division": "not yet sorted",            
        }

        print bill
