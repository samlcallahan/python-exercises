import menu_functions as mf
import os.path
import locale
from tabulate import tabulate

locale.setlocale( locale.LC_ALL, '' )

log_file = "checkbook_log.txt"
currency_codes = eval(open("currency_codes.txt", "r+").read())
conversion_rates = eval(open("conversion_rates.txt", "r+").read())

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
    print("4) Modify past transactions")
    print("5) Show history")
    print("6) Show balance in alternate currency")
    print("7) Exit")
    choice = input("Your choice? ")
    while choice not in "1234567":
        print("Invalid choice: " + choice)
        choice = input("Your choice?")
    return choice

def menu_option(choice):
    if choice == "1":
        balance = currency_format(mf.balance())
        print(f"Your current balance is {balance}.\n")
        return
    elif choice == "2":
        amount = amount_input("How much would you like to withdraw?")
        mf.withdraw(amount)
        return
    elif choice == "3":
        amount = amount_input("How much would you like to deposit?")
        mf.deposit(amount)
        return
    elif choice == "4":
        id_to_mod, amount = modify_prompt()
        mf.modify(id_to_mod, amount)
        return
    elif choice == "5":
        show_history(only_transactions=False, limit=None)
    elif choice == "6":
        code = curr_code_input()
        balance, currency_name = currency_conversion(mf.balance(),code)
        print(f"Your current balance is {balance:n} in {currency_name}s")
    elif choice == "7":
        mf.exit()

def modify_prompt():
    '''
    enter transaction number
    browse past transactions
    new value? (negative to switch deposit to withdrawal or vice-versa)
    '''
    print("1) I know the ID of the transaction I'd like to modify")
    print("2) I'd like to browse past transactions to find the ID number")
    choice = input("Your choice? ")
    while choice not in "12":
        print("Invalid choice: " + choice)
        choice = input("Your choice?")
    if choice == "1":
        id_to_mod = id_input()
        new_amount = amount_input()
    elif choice == "2":
        show_history(limit=None)
        id_to_mod = id_input()
        new_amount = amount_input()
    return id_to_mod, new_amount

def currency_format(number):
    return locale.currency(number,grouping=True)

def id_input():
    checkbook = mf.get_checkbook()
    id_to_mod = input("ID number?")
    while not id_to_mod.isnumeric() or int(id_to_mod) >= len(checkbook) or checkbook[int(id_to_mod)]["category"] != "transaction":
        print("Invalid ID: " + id_to_mod + "\n")
        id_to_mod = input("ID number?")
    id_to_mod = int(id_to_mod)
    return id_to_mod

def amount_input(prompt_message="New amount?"):
    amount = input(prompt_message)
    while not (amount[0] == "-" and amount[1:].isnumeric()) and not amount.isnumeric():
        print("Invalid amount: " + amount + "\n")
        amount = input(prompt_message)
    amount = int(amount)
    return amount

def curr_code_input():
    for code in currency_codes:
        print(code)
    curr_code = input("Which currency?")
    while curr_code not in currency_codes:
        curr_code_input()
    return curr_code

def show_history(only_transactions=True, limit=20, offset=0):
    checkbook = mf.get_checkbook()
    start = len(checkbook) - offset
    if limit is None:
        end = 0
    else:
        end = start - limit
    if not only_transactions:
        to_print = checkbook[end:start]
        to_print.reverse()
    else:
        to_print = [entry for entry in checkbook if entry["category"] == "transaction"]
        to_print = to_print[end:start]
        to_print.reverse()
    if only_transactions:
        headers_list = ["ID", "Type", "Date", "Amount", "Balance"]
    else:
        headers_list = ["ID", "Type", "Date", "Related Entries", "Amount", "Balance"]
    for index, entry in enumerate(to_print):
        to_print[index] = printable_entry(entry,only_transactions=only_transactions)
    print(tabulate(to_print,headers=headers_list))

def printable_entry(entry, only_transactions=True):
    if only_transactions:
        print_item = [entry["id"], 
                      "Deposit" if entry["amount"] > 0 else "Withdrawal",
                      entry["created"],
                      currency_format(abs(entry["amount"])),
                      currency_format(entry["balance"])]
    else:
        print_item = [entry["id"], 
                      entry["category"],
                      entry["created"],
                      entry["entry"]if entry["category"] == "modify" else ", ".join(entry["mods"]),
                      currency_format(entry["amount"]) if entry["category"] == "transaction" else None,
                      currency_format(entry["balance"])]
    return print_item

def currency_conversion(value,currency_code):
    currency_data = conversion_rates[currency_codes.index(currency_code)]
    return value * currency_data[1], currency_data[0]


checkbook_init()

option = menu_prompt()

while True:
    menu_option(option)
    option = menu_prompt()