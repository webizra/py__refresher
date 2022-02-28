# DAY 1 OF PYTHON: WORKING WITH STRINGS AND VARIABLES
# python is a general purpose programming language, meaning, it can be used
# to create a variety of different programs, websites, softwares, automate task,
# data analysis, data science, etc

#1 how to move to next line in python

print('hello world\nhello world')
# joining strings together
print('hello' + ' ' + 'angela')

# 2 concatenating strings // you can't concatenate integers
print('hello' " " + input('what is your name?'))
# to concatenate a string and an integer you need convert it into a strings
# and then store it in a variable

num_char = len(input('what is your name?'))
converted_int = str(num_char)
print('your name has ' + converted_int + ' characters')

# 2 input function and the len function 

print(len('hello ' + input('what is your name?')))
print('hello' " " +input('what is your name'))

# variable naming

a = input('a:')
b = input ('b:')

print('a = ' + a)
print('b = ' + b)

c = a
a = b
b = c

result = 4/ 2
result /=2
print(result)

score = 0
height = 1.8
isWinning = True