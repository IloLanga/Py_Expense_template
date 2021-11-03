from PyInquirer import prompt
from examples import custom_style_2
from expense import expense_questions,new_expense, get_user_list
from group_expense import group_expense_questions, new_group_expense
from user import user_questions, add_user


def ask_option():
    main_option = {
        "type":"list",
        "name":"main_options",
        "message":"Expense Tracker v0.1",
        "choices": ["New Expense","New Group Expense","Show Status","New User"]
    }
    option = prompt(main_option)
    if (option['main_options']) == "New Expense":
        new_expense()
        ask_option()
    if (option['main_options']) == "New Group Expense":
        new_group_expense()
        ask_option()
    if (option['main_options']) == "New User":
        add_user()
        ask_option()

def main():
    ask_option()

main()