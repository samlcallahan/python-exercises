from datetime import date
import sys

def load_checkbook():
    checkbook_file = open("checkbook_log.txt", "r+")
    checkbook_write = open("checkbook_log.txt", "a+")
    checkbook = [eval(line) for line in checkbook_file]
    last_id = checkbook[-1]["id"]
    return checkbook, checkbook_write, last_id

def balance():
    checkbook, checkbook_write, last_id = load_checkbook()
    last_entry = checkbook[-1]
    return last_entry["balance"]

def withdrawal(amount):
    checkbook, checkbook_write, last_id = load_checkbook()
    id = last_id + 1
    created = str(date.today())
    new_balance = balance() - amount
    log_dict = {"id" : id, "category" : "withdrawal", "created" : created, "modified" : created, "description" : "", "amount" : -amount, "balance" : new_balance}
    to_append = str(log_dict)
    checkbook_write.write("\n" + to_append)

def deposit(amount):
    checkbook, checkbook_write, last_id = load_checkbook()
    id = last_id + 1
    created = str(date.today())
    new_balance = balance() + amount
    log_dict = {"id" : id, "category" : "deposit", "created" : created, "modified" : created, "description" : "", "amount" : amount, "balance" : new_balance}
    to_append = str(log_dict)
    checkbook_write.write("\n" + to_append)

# def modify(trans_id, column, new_value):


# def search(key, category = "All"):


def exit():
    sys.exit("Thanks for using the terminal checkbook!")
