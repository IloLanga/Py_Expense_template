from PyInquirer import prompt, print_json, Separator
import csv
import json
import regex

def get_user_list():
    user_list = []

    with open('users.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
     for row in spamreader:
       user_list.append(row[0])

    return user_list

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": get_user_list(),
    },

]


def new_expense(*args):

    amount = ""
    while not (amount.isdigit()):
      infos = prompt(expense_questions)
      amount = infos["amount"]
      if not (amount.isdigit()):
        print("Amount must be an number, try again")

    with open('expense_report.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([infos["amount"], infos["label"], infos["spender"]])

    print("Expense Added !")
    print(infos["spender"] + " spent " + infos["amount"] + " for " + infos["label"])
    return True


