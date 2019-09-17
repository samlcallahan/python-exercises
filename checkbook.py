import menu_functions as mf
import os.path
import locale

locale.setlocale( locale.LC_ALL, '' )

log_file = "checkbook_log.txt"

print("~~~ Welcome to your terminal checkbook! ~~~\n")

def checkbook_init():
    if os.path.exists(log_file):
        if mf.get_checkbook() == []:
            mf.deposit(100,id_number=0)
        return
    else:
        open(log_file,"x")
        mf.deposit(100,id_number=0)
        return

def menu_prompt():
    print("What would you like to do? \n")
    print("1) View your current balance")
    print("2) Make a withdrawal")
    print("3) Make a deposit")
    print("4) Exit")
    choice = input("Your choice? ")
    while choice not in "1234":
        print("Invalid choice: " + choice + "\n")
        choice = input("Your choice? \n")
    return choice

def menu_option(choice):
    if choice == "1":
        balance = locale.currency(mf.balance(),grouping=True)
        print(f"Your current balance is {balance}.\n")
        return
    elif choice == "2":
        amount = float(input("How much would you like to withdraw?\n"))
        mf.withdrawal(amount)
        return
    elif choice == "3":
        amount = float(input("How much would you like to deposit?\n"))
        mf.deposit(amount)
        return
    elif choice == "4":
        mf.exit()

def modify_prompt():

def description_prompt():
    
checkbook_init()

option = menu_prompt()

while True:
    menu_option(option)
    option = menu_prompt()