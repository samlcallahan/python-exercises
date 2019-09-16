import functions_exercises
from functions_exercises import is_two
from functions_exercises import handle_commas as commas

functions_exercises.is_vowel("a")
functions_exercises.is_vowel("!")
functions_exercises.is_vowel("B")
functions_exercises.is_vowel("A")

is_two(0b10)
is_two(2)
is_two("2")
is_two(1)
is_two("a")
is_two("!") # does not handle non-numeric strings well

commas("100000")
commas("1,0,0,0,0,0,")
commas("asbdasd,,") # didn't handle float(this) well
commas(1000000) # couldn't run this.replace()

import itertools as it

list1 = ["a","b","c"]
list2 = [1,2,3]

combinations_letter_number = list(it.product(list1,list2))

ways_to_combine_letter_number = len(combinations_letter_number)

list_letters = ["a","b","c","d"]

combinations_letters = list(it.combinations(list_letters,2))

ways_to_combine_letters = len(combinations_letters)

import json

profiles = open('profiles.json')

profiles_data = json.load(profiles)

user_total = len(profiles_data)

active_total = len([x for x in profiles_data if x["isActive"]])

inactive_total = len([x for x in profiles_data if not x["isActive"]])

def clean_balance(bal_string):
    return float(bal_string.replace("$","").replace(",",""))

cleaned_balances = [clean_balance(x["balance"]) for x in profiles_data]

total_balance = sum(cleaned_balances)

average_balance = total_balance / len(cleaned_balances)

user_lowest_balance = [x["name"] for x in profiles_data if clean_balance(x["balance"]) == min(cleaned_balances)]

user_highest_balance = [x["name"] for x in profiles_data if clean_balance(x["balance"]) == max(cleaned_balances)]

from collections import Counter

fruit_counts = Counter([x["favoriteFruit"] for x in profiles_data])

most_common_fruit = max(fruit_counts,key=fruit_counts.get)

least_common_fruit = min(fruit_counts,key=fruit_counts.get)

total_unreads = sum([int(x["greeting"][-len("  unread messages.")]) for x in profiles_data])