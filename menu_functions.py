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

def overwrite_checkbook(checkbook):
    destination = open(checkbook_file,"w")
    writeable_checkbook = [str(entry) for entry in checkbook]
    destination.writelines(writeable_checkbook)

def last_id(checkbook_dict):
    return checkbook_dict[-1]["id"]

def balance():
    checkbook = get_checkbook()
    last_entry = checkbook[-1]
    return last_entry["balance"]

def transaction(amount, id_number=1):
    log_dict = create_entry("transaction", amount, id_number=id_number)
    write_checkbook(log_dict)

def deposit(amount, id_number=1):
    transaction(amount, id_number)

def withdraw(amount):
    transaction(-amount)

def modify(trans_id, new_value):
    entry_log = create_entry("modify", id_to_mod=trans_id, new_value=new_value)
    checkbook = recalculate_balances(trans_id, entry_log)
    entry_log["balance"] = checkbook[-1]["balance"]
    checkbook = checkbook.append(entry_log)
    overwrite_checkbook(checkbook)

def create_entry(category, amount=0, id_to_mod=None, new_value=None, id_number=1):
    checkbook = get_checkbook()
    entry = {}
    if id_number != 0:
        id_number = last_id(checkbook) + 1
    created = time.ctime(time.time())
    entry["id"] = id_number
    entry["category"] = category
    entry["created"] = created
    if category == "modify":
        entry = mod_entry(id_to_mod, new_value, entry)
    else:
        entry = trans_entry(amount, entry)
    return entry

def trans_entry(amount, entry_stub):
    entry_stub["modified"] = entry_stub["created"]
    entry_stub["amount"] = amount
    entry_stub["mods"] = []
    if entry_stub["id"] != 0:
        entry_stub["balance"] = balance() + amount
    else:
        entry_stub["balance"] = amount
    return entry_stub

def mod_entry(id_to_mod, new_value, entry_stub):
    checkbook = get_checkbook()
    entry_stub["entry"] = id_to_mod
    entry_stub["old"] = checkbook[id_to_mod]["amount"]
    entry_stub["new"] = new_value
    return entry_stub

def recalculate_balances(id_number, mod_entry_stub):
    checkbook = get_checkbook()
    old = mod_entry_stub["old"]
    new = mod_entry_stub["new"] * -(old < 0)
    mod_id = mod_entry_stub["id"]
    checkbook[id_number]["amount"] = new
    checkbook[id_number]["modified"] = mod_entry_stub["created"]
    checkbook[id_number]["mods"].append(mod_id)
    difference = new - old
    for i in range(id_number, last_id(checkbook) + 1):
        checkbook[i]["balance"] += difference
    return checkbook

def exit():
    sys.exit("Thanks for using the terminal checkbook!")
