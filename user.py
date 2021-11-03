from PyInquirer import prompt
import csv
import json

user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New User - Name: ",
    },

]

def add_user():
    # This function should create a new user, asking for its name
    infos = prompt(user_questions)
    
    with open('users.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([infos["name"]])

    # print("User Added ! Welcome " + infos["name"])
    return True