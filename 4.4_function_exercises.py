def is_two(value):
    """
        Returns True if input is equivalent to the number 2 or string "2," otherwise returns False
    """
    if int(value) == 2:
        return True
    else:
        return False

def is_vowel(letter):
    """
        Returns True if input is a vowel, otherwise returns False
    """
    vowels = "aeiou"
    return letter.lower() in vowels

def is_consonant(letter):
    """
        Returns True if input is a consonant, otherwise returns False
    """
    return letter.isalpha() and not is_vowel(letter)

def capitalize_consonant_first_words(word):
    """
        If the word starts with a consonant, returns the capitalized version of the word, else returns the original word
    """
    if is_consonant(word[0]):
        return word.capitalize()
    else:
        return word

def calculate_tip(tip_percent, bill_total):
    """
        Returns the amount to tip, given a tip percentage between 0 and 1, and the total of a bill
    """
    if tip_percent > 1 or tip_percent < 0:
        tip_percent = float(input("Tip percentage must be between 0 and 1. Please enter a new tip percentage value: "))
    return tip_percent * bill_total

def apply_discount(original_price, discount_rate):
    """
        Given a price and discount rate, returns the price after the discount is applied
    """
    return original_price * (1 - discount_rate)

def handle_commas(number_string):
    """
        Takes a string comprised of numbers and commas, returns the number in the float datatype without commas
    """
    return float(number_string.replace(",",""))

def get_letter_grade(number_grade):
    """
        Takes a number and returns the corresponding letter grade
        Intended for numbers between 0-100, but will not fail with other numbers (the value of the result may be in question, though)
    """
    letter_grades = ["A", "B", "C", "D", "F"]
    cutoff = 90
    for i in range(4):
        if number_grade >= cutoff - (10 * i):
            return letter_grades[i]
    return letter_grades[4]

def remove_vowels(word):
    """
        Accepts a string and returns it with all vowels removed
    """
    for letter in word:
        if is_vowel(letter):
            word = word.replace(letter,"")
    return word

def normalize_name(raw_name):
    """
        Takes a string and returns a 'cleaned' version of it. This means:
            - no leading or trailing whitespaces
            - underscores instead of spaces
            - all lowercase
            - only valid python identifiers
    """
    name = raw_name
    for letter in raw_name:
        if not letter.isidentifier():
            name = name.replace(letter,"")
    name = name.strip()
    name = name.lower()
    name = name.replace(" ","_")
    return name

def cumsum(list_numbers):
    """
        Given a list of numbers, returns a list of the cumulative sum at that point in the list. examples:
        [1, 1, 1] => [1, 2, 3]
        [1, 2, 3, 5] => [1, 3, 6, 11]
    """
    cumulative_sum = []
    sum_so_far = 0
    for number in list_numbers:
        sum += number
        cumulative_sum.append(sum_so_far)
    return cumulative_sum

def twelveto24(time):
    """
        Takes a time in a 12hr format "hh:mm[am/pm]" and returns it in a 24 hr format "hh:mm"
    """
    if time[-2:] == "am":
        if time[:2] == "12":
            return "0" + time[2:-2]
        return time[:-2]
    elif time[-2:] == "pm":
        if time[:2] == "12":
            return time[:-2]
        colon_location = time.find(":")
        hour = int(time[0:colon_location]) + 12
        return str(hour) + time[colon_location:-2]
    else:
        print("You don't seem to have input a time in an appropriate format")

def col_index(column_name):
    """
        Takes a column name that is a string of letters and returns the corresponding column number
    """
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    column_name = column_name.upper()
    column = 0
    iteration = 0
    for letter in column_name:
        iteration += 1
        value = alphabet.find(letter) + 1
        exponent = len(column_name) - iteration
        column += value * (len(alphabet) ** exponent)
    return column
