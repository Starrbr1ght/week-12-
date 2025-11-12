# Objective:
# Students will learn how to compare values using Python’s comparison operators and interpret Boolean results.

# Topics Covered:
# ==, !=, >, <, >=, <=

# Key Notes:

# Comparison operators compare two values and return either True or False.

# Remember: = is assignment, while == is comparison.

a = 3
b = 4
print(a) #output of 3
print(b) #output of 4
print(a==b) #output false
print(a == b)   # False, checks for equality
print(a != b)   # True, checks if not equal to another value
print(a > b)    # False, checks for greater than
print(a < b)    # True, checks for less than
print(a >= b)   # False, checks for greater than or equal to
print(a <= b)   # True, this one chacks for less than or equal to


#predict the output of the following comparisons:
10 > 5 #output true
7 == 2 * 3 + 1 #output true
8 != 8 # output false
4 <= 2 + 2 #output true

# Write 3 examples that result in True and 3 that result in False.

12 == 2 * 8 - 4 #output true
12 != 11 #output true
25 > 12 + 4 #output true
17 < 10 #output false
10 == 12 #output false
13 >= 25 #output false




# Create a simple grade-checking condition:

# practice problem :
# where a student must check if their score is greater than or equal to 60 to pass a test.
#asking student for score
score = int(input("what is your score?"))
#make this program for all grading spectrums
#if thre score is between 90-100 .. you got an A
#if the score is between 80-89 -- you got a B
#if the score is between 70-79 -- you got a C
#if the score is between 61-69 ... you got a D
#else you failed
if score >= 90:
    print("you got an A")
elif score  >= 80 and score <= 89:
    print("you got a B!")
elif score >= 70 and score <= 79:
   print("you got a C")
elif score >= 60  and score <= 69:
     print("you got a D")
else:
     print("you failed.")
#ask for password
password = input("what is your password?")
if len(password) >= any(char.isdigit() for char in password):
    print("password is valid")
else:
    print("password is invalid." \
    "it musct be atleast 8 characters long and contain atleast one digit")
# The password must be at least 8 characters long and contain at least one digit.password = "mypassword1"