import requests
import json

firebaseToken = "SrnTxDeDHNnETjwfDVxOSc930oaIdMdI6NsUNqBk"

dataBaseURL = "https://yig-bill-tracker.firebaseio.com/.json"
dataBaseURL += "?auth=" + firebaseToken

authorName = raw_input("name :")
authorLastName = raw_input("last name :")
authorID = authorName + "-" + authorLastName
authorSchool = raw_input("school :")
billTitle = "a-bill-to-" + raw_input("title :")
section1 = raw_input("section 1 :")
section2 = raw_input("section 2 :")
section3 = raw_input("section 3 :")
section4 = raw_input("section 4 :")
section5 = raw_input("mm/dd/yyyy :")

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
