import csv

# recupere la liste des spender, et creer un objet contenant le nom du spender et ce qu'il a dépensé {name: amount}
def get_user_list_exp():
    user_list = dict([])

    with open('users.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
     for row in spamreader:
       user_list[row[0]] = 0

    return user_list


def get_status():
  # recupere la list d'objets contenant le nom du spender et ce qu'il a dépensé {name: amount}
  user_list = get_user_list_exp()

  with open('expense_report.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
     for row in spamreader:
      #  additionne la nouvelle depense au total des depense du spender
       new_amount = user_list[row[2]] + float(row[0])
       user_list[row[2]] = new_amount
  
  print("Amount of money everybody spent: ")
  print(user_list)
  print("not enough time, you'll have to do the maths sorry :'( ")
  return True
       