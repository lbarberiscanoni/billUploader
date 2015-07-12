import requests
import json
import subprocess

#convert word docx into txt files so they can be read
subprocess.call("textutil -convert txt Files/*.docx", shell=True)

#find all the text files and put them in a list
rawBillList = subprocess.check_output("find Files/ -name " + "*.txt", shell=True)
billList = [n.replace("Files//", "") for n in rawBillList.split()]

#loop over every text version of the bill
for bill in billList:
    with open("Files/" + bill, "r") as file:
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

        #now that we have all the data from the bill, let's push it to Firebase
        firebaseToken = "SrnTxDeDHNnETjwfDVxOSc930oaIdMdI6NsUNqBk"

        dataBaseURL = "https://yig-bill-tracker.firebaseio.com/.json"
        dataBaseURL += "?auth=" + firebaseToken

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

        billPushed = requests.post(url = dataBaseURL, data = json.dumps(bill))

        str(json.loads(billPushed.content).values()[0])

        if billPushed.status_code == requests.codes.ok:
            new_id = str(json.loads(billPushed.content).values()[0])
            new_url = "https://yig-bill-tracker.firebaseio.com/"+new_id+"/.json"
            new_data = {}
            new_data["id"] = new_id
            billPushed = requests.patch(url = new_url, data = json.dumps(new_data))
# this is just for now so that every time the script runs it's refreshed
#subprocess.call("rm Files/*.txt", shell=True)
