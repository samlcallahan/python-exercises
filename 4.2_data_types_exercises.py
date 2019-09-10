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