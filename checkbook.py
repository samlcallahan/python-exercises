import menu_functions as mf
import os.path as os

print("~~~ Welcome to your terminal checkbook! ~~~\n")

def checkbook_init():
    if os.exists("checkbook_log.txt")
        return open("checkbook_log.txt")
    else:
        open("checkbook_log.txt","x")
        mf.deposit(100)
        return open("checkbook_log.txt")

def menu_prompt(checkbook):
    print("What would you like to do? \n")

checkbook = checkbook_init()

menu_prompt(checkbook)