# DAY 2: UNDERSTANDING DATATYPES AND HOW TO MANIPULATE STRINGS

# datatypes in python

# string
# integer
# float // short for a floating point num
# boolean // True and False

# the method of pulling out a particular element from a string is called subscripting
# print('hello'[4])

# mathematical operators in python
#  + - * /  // in python, a division result is always a floating point num
# 2**2 = 4 // 2**3 = 8
# ** means power of a num
# PEMDAS: just like bodmas, its basically state the order of priority
# short for; parenthesis (), exponents ** multiplication *, division /, addition +, subtraction - 
# depending on the position left and right, calculations always start from the left


# BMI calculator
#          weight(kg)
# BMI = ---------------
#         height**2(m**2)

# weight = input('enter your weight in kg:\n ')
# height = input('enter your height in m:\n ')
# bmi = int(weight) / float(height) **2
# convert_bmi_to_int = int(bmi)
# print(convert_bmi_to_int)
# note: \n means new line character

""" weight = input("what is your weight in kg?\n")
height = input("enter your height in m:\n")
bmi = int(weight) / float(height) ** 2
print (round(bmi)) """

# number manipulation and F strings in python
# rounding numbers
# print(round(2.666666666, 1)) // the second arg is the num it is rounded up to
# flow division in python //: this helps to chop off decimal point and returns a whole num
result = 8.5 // 2
result //=2
print(result)

score = 0
height= 1.8
isWinning = True
print('your score is ' + str(score) + " and your height in meter is " + str(height))
# using f-string: f-string provides a simpler way of embedding expressions in curly braces inside string literals
# print(f'your score is {score}, your height is {height}, you re winning is {isWinning}')

# building a tip calculator

# print('welcome to the tip calculator!')
# bill = float(input ('what was the total bill? N'))
# tip = int(input('how much tip would you like to give? 10, 12, or 15?'))
# people= int(input('how many people to split the bill'))
# bill_with_tip = tip / 100 * bill + bill
# print(bill_with_tip)
