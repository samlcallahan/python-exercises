from datetime import date
import time
import sys

checkbook_file = "checkbook_log.txt"

def get_checkbook():
    checkbook_read = open(checkbook_file, "r+")
    checkbook = [eval(line) for line in checkbook_read]
    return checkbook

def write_checkbook():
    return open(checkbook_file, "a+")

def last_id(checkbook_dict):
    return checkbook_dict[-1]["id"]

def balance():
    checkbook = get_checkbook()
    last_entry = checkbook[-1]
    return last_entry["balance"]

def withdrawal(amount,category="withdrawal",id_number=1):
    checkbook = write_checkbook()
    checkbook_dict = get_checkbook()
    if id_number != 0:
        id_number = last_id(checkbook_dict) + 1
    created = str(date.today())
    if id_number == 0:
        new_balance = -amount
    else:
        new_balance = balance() - amount
    log_dict = {"id" : id_number, "category" : category, "created" : created, "modified" : created, "description" : "", "amount" : -amount, "balance" : new_balance}
    to_append = str(log_dict)
    if id_number == 0:
        checkbook.write(to_append)
    else:
        checkbook.write("\n" + to_append)

def deposit(amount,category="deposit",id_number=1):
    withdrawal(-amount,category,id_number)

def modify(trans_id, column, new_value):
    checkbook_dict = get_checkbook()
    checkbook = write_checkbook()

# def search(key, category = "All"):


def exit():
    sys.exit("Thanks for using the terminal checkbook!")
