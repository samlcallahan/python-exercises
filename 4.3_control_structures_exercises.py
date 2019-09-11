day = input("Day of the week?")
if day.capitalize() == "Monday":
    print("It's Monday!")
else:
    print("It's not Monday!")

day = input("Day of the week?")
weekend = ["Saturday", "Sunday"]
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
if day.capitalize() in weekend:
    print("It's the weekend!")
elif day.capitalize() in weekdays:
    print("It's a weekday. :(")
else:
    print("You've found the eighth day of the week!!")

hours_worked = 80
hourly_rate = 35.89
if hours_worked <= 40:
    paycheck = hours_worked * hourly_rate
else:
    paycheck = (hours_worked - 40) * hourly_rate * 1.5 + 40 * hourly_rate

i = 5
while i <= 15:
    print(i)
    i += 1

i = 0
while i <=100:
    print(i)
    i += 2

i = 100
while i >= -10:
    print(i)
    i -= 5

n = 2
while n < 1000000:
    print(n)
    n = n ** 2

n = 100
while n >= 5:
    print(n)
    n -= 5

def times_table():
    number = int(input("Number?"))
    for i in range(1,11):
        print(f'{number} x {i} = {number * i}')

times_table()

for i in range(1,10):
    print(str(i) * i)

number = int(input("Odd number between 1 and 50?"))
def is_valid(number):
    return 1 <= number and number <= 50 and number % 2 != 0

valid_number = is_valid(number)

while not valid_number:
    number = int(input("Invalid number, please enter an odd number between 1 and 50"))
    valid_number = is_valid(number)

print("Number to skip: " + str(number))
for n in range(1,51,2):
    if n == number:
        print("Yikes! Skipping number: " + str(number))
        continue
    print("Here is an odd number: " + str(n))

def is_positive(number):
    return number > 0

def positive_prompt():
    number = int(input("Positive number?"))
    positive = is_positive(number)

    while not positive:
        number = int(input("That wasn't a positive number; try again:"))
        positive = is_positive(number)
    return number

number = positive_prompt()

for i in range(number + 1):
    print(i)

number = positive_prompt()

for i in range(number):
    print(number - i)

for i in range(1,101):
    message = str(i)
    if i % 3 == 0:
        message = "Fizz"
        if i % 5 == 0:
            message += "Buzz"
    elif i % 5 == 0:
        message = "Buzz"
    print(message)

make_another = True

while make_another:
    number = int(input("What number would you like to go up to?"))
    print("Here is your table!")
    print("number | squared | cubed")
    print("-" * 6 + " | " + "-" * 7 + " | " + "-" * 5)
    for i in range(number):
        first = str(i)
        square = str(i ** 2)
        cube = str(i ** 3)
        print(first + " " * (7-len(first)) + "| ", end="")
        print(square + " " * (8-len(square)) + "| ", end="")
        print(cube)
    make_another = input("Another table? (Y/N)") == "Y"

def minus_or_plus(grade,plus_cutoff,minus_cutoff,letter_grade):
    if grade >= plus_cutoff:
        letter_grade += "+"
    elif grade < minus_cutoff:
        letter_grade += "-"
    return letter_grade

continue_grades = True

while continue_grades:
    grade = int(input("Enter a grade between 0 and 100: "))
    if grade >= 88:
        letter_grade = minus_or_plus(grade,99,92,"A")
    elif grade >= 80:
        letter_grade = minus_or_plus(grade,87,82,"B")
    elif grade >= 67:
        letter_grade = minus_or_plus(grade,78,70,"C")
    elif grade >= 60:
        letter_grade = minus_or_plus(grade,66,62,"D")
    else:
        letter_grade = "F"
    print(letter_grade)
    continue_grades = input("Continue?(Y/N)").upper() == "Y"

favorite_books = [{"title" : "Anna Karenina"}]