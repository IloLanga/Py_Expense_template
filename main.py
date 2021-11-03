from PyInquirer import prompt
from examples import custom_style_2
from expense import expense_questions,new_expense, get_user_list
from group_expense import group_expense_questions, new_group_expense
from user import user_questions, add_user
from status import get_status


def ask_option():
    main_option = {
        "type":"list",
        "name":"main_options",
        "message":"Expense Tracker v0.1",
        "choices": ["New Expense","New Group Expense","Show Status","New User"]
    }
    # Nouvelle dépense
    option = prompt(main_option)
    if (option['main_options']) == "New Expense":
        new_expense()
        ask_option()

    # Nouvelle dépense de groupe
    if (option['main_options']) == "New Group Expense":
        new_group_expense()
        ask_option()

    # Nouvel utilisateur
    if (option['main_options']) == "New User":
        add_user()
        ask_option()

    # Montrer le status des depenses des utilisateurs
    if (option['main_options']) == "Show Status":
        get_status()
        ask_option()

def main():
    ask_option()

main()