from PyInquirer import prompt, print_json, Separator
import csv
import json

def get_user_list():
    user_list = []
    with open('users.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
     for row in spamreader:
       user_list.append({'name': row[0]})

    return user_list

group_expense_questions = [
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
        "type":"checkbox",
        "name":"spenders",
        "message":"New Expense - Spenders: ",
        "choices": get_user_list(),
    },

]


def new_group_expense(*args):
    spenders = []
    amount = ""

    while (len(spenders) == 0) or (not amount.isdigit()):
      expense_info = prompt(group_expense_questions)
      spenders = expense_info["spenders"]

      if (len(spenders) == 0):
        print("No one paid ? You must choose at least one spender.")
      amount = expense_info["amount"]

      if not (amount.isdigit()):
        print("Amount must be an number, try again")

    amount = int(expense_info["amount"]) / len(spenders)
    label = expense_info["label"]



    with open('expense_report.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for spender in spenders:
          spamwriter.writerow([amount, label, spender])

    print("Expense Added !")
    print("spenders spent " + str(amount) + " each for " + label)
    return True


