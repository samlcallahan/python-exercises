import time
import sys

checkbook_file = "checkbook_log.txt"

def get_checkbook():
    checkbook_read = open(checkbook_file, "r+")
    checkbook = [eval(line) for line in checkbook_read]
    return checkbook

def write_checkbook(log_dict):
    destination = open(checkbook_file, "a+")
    if log_dict["id"] == 0:
        destination.write(str(log_dict))
    else:
        destination.write("\n" + str(log_dict))

def last_id(checkbook_dict):
    return checkbook_dict[-1]["id"]

def balance():
    checkbook = get_checkbook()
    last_entry = checkbook[-1]
    return last_entry["balance"]

def withdrawal(amount,category="withdrawal",id_number=1):
    checkbook = get_checkbook()
    if id_number != 0:
        id_number = last_id(checkbook) + 1
    created = time.ctime(time.time())
    if id_number == 0:
        new_balance = -amount
    else:
        new_balance = balance() - amount
    log_dict = {"id" : id_number, "category" : category, "created" : created, "modified" : created, "description" : "", "amount" : -amount, "balance" : new_balance}
    write_checkbook(log_dict)

def deposit(amount,category="deposit",id_number=1):
    withdrawal(-amount,category,id_number)

def modify(trans_id, column, new_value):
    checkbook = get_checkbook()
    if checkbook[column] == new_value or checkbook["category"] == "modify":
        return
    modified = time.ctime(time.time())
    id_number = last_id(checkbook) + 1
    category = "modify"
    old_value = checkbook[column]
    new_balance = checkbook[id_number - 1]["balance"]
    if column == "category":
        amount = -checkbook[id_number]["amount"]
        new_balance = recalculate_balance(id_number,amount)
    elif column == "amount":
        new_balance = recalculate_balance(id_number,new_value)
    log_dict = {"id" : id_number, "category" : category, "created" : modified, "description" : "", "entry" : trans_id, "column" : column, "old" : old_value, "new": new_value, "balance" : new_balance}
    write_checkbook(log_dict)
    
def recalculate_balance(id_number,new_amount):
    checkbook = get_checkbook()
    checkbook[id_number]["amount"] = new_amount
    checkbook[id_number]["balance"] = checkbook[id_number-1]["balance"] + new_amount
    for id_no in range(id_number + 1,last_id(checkbook) + 1):
        if 
        checkbook[id_no]["balance"] = checkbook[id_no - 1]["balance"] +
    return new_balance
# def search(key, category ="All",limit=10,offset=0):


def exit():
    sys.exit("Thanks for using the terminal checkbook!")
