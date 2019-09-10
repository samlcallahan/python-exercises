def print_type(variable):
    print(variable)
    print(type(variable))

print_type(99.9)
print_type("False")
print_type(False)
print_type('0')
print_type(0)
print_type(True)
print_type('True')
print_type([{}])
print_type({'a' : []})

""" 
string
bool
float
bool
string
float
list of lists? depends on implementation
string
lots of ways to do this one. I suppose a dictionary might be most appropriate """

# Prediction: TypeError
'1' + 2

# Prediciton: 2
6 % 4

# Prediction: int
type(6 % 4)

# Prediction: type
type(type(6 % 4))

# Prediction: TypeError
'3 + 4 is' + 3 + 4

# Prediction: False
0 < 0

# Prediction: False
'False' == False

# Prediction: False
'True' == True

# Prediction: True
5 >= -5

# Prediction: True
!False or False
# Actually, SyntaxError
# not False or False would have returned the expected result

# Prediction: True
True or "42"

# Prediction: 1
6 % 5

# Prediction: False
5 < 4 and 1 == 1

# Prediction: False
'codeup' == 'codeup' and 'codeup' == 'Codeup'

# Prediction: SyntaxError on !==
4 >= 0 and 1 !== '1'

# Prediction: True
6 % 3 == 0

# Prediction: True
5 % 2 != 0

# Prediction: TypeError
[1] + 2

# Prediction: [1, 2]
[1] + [2]

# Prediction: [1, 1]
[1] * 2

# Prediction: [2]
[1] * [2]
# Actually, got a TypeError

# Prediction: True
[] + [] == []

# Prediction: TypeError
{} + {}

daily_rate = 3

days_rented = [3, 5, 1]

total_cost = sum(days_rented) * daily_rate

google_rate = 400

amazon_rate = 380

facebook_rate = 350

facebook_time = 10

google_time = 6

amazon_time = 4

total_pay = facebook_rate * facebook_time + google_rate * google_time +amazon_rate * amazon_time

if university_class.full = False and not university_class.schedule.isdisjoint(student.schedule):
    university_class.enroll(student)

if (purchase_size > 2 or member.premium == True) and not offer.expiration:
    offer.apply()

username = 'codeup'
password = 'notastrongpassword'

password_length_at_least_five = len(password) >= 5
username_length_no_more_than_twenty = len(username) <= 20
password_is_not_username = password != username
no_starting_or_ending_whitespace = username.strip() == username and password.strip() == password