# PYTHON LOOPS
# fruits = ["apple", "peach", "pear"]
# for fruit in fruits:
#     print(fruit)

# calculating total height with the for loop
# studentHeights = input("type in a list of student height ").split()
# for n in range(0, len(studentHeights)):
#     studentHeights[n] = int(studentHeights[n])
# totalHeight = 0
# for height in studentHeights:
#     totalHeight += height
# print(totalHeight)

# studentNumber = 0
# for student in studentHeights:
#     studentNumber += 1
# print(studentNumber)
# averageHeight = round(totalHeight / studentNumber)
# print(averageHeight)

# calculating the highscore using the max function
# studentScores = input("input the list of students scores\n").split()
# for n in range(0, len(studentScores)):
#     studentScores[n] = int(studentScores[n])
# print(studentScores)
# print(min(studentScores))
# print(max(studentScores))

# calculating the highscore using the for loop
# highestScore = 0
# for Score in studentScores:
#     if Score > highestScore:
#         highestScore = Score
# print(f"the highest score in the class is: {highestScore}")

# using the for loop and the range function
# total = 0
# for number in range(1, 101):
#     total += number
# print(total)
# calculating even numbers using the for loop and the range function
# total = 0
# for number in range (2, 101, 2):
#     total += number
# print (total)
# # or
# total2 = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#         total2 += number
# print (total2)

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("fizzbuzz")
#     elif number % 3 == 0:
#         print("fizz")
#     elif number % 5 == 0:
#         print("buzz")
#     else:
#         print(number)

# the password generator project
import random
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", 
"l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", 
"w", "x", "y", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
 "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("welcome to the pypassword generator!")
nrLetters = int(input("how many letters would you like in your password\n"))
nrSymbols = int(input(f"how many symbols would you like\n"))
nrNumbers = int(input(f"how many numbers would you like\n"))

# easy level password using just string
password = ""
for character in range(1, nrLetters + 1):
    password  += random.choice(letters)
for character in range(1, nrSymbols + 1):
    password  += random.choice(symbols)
for character in range(1, nrNumbers + 1):
    password  += random.choice(numbers)
print(password)

# hard level password using list
passwordList = []
for character in range(1, nrLetters + 1):
    passwordList  += random.choice(letters)
for character in range(1, nrSymbols + 1):
    passwordList  += random.choice(symbols)
for character in range(1, nrNumbers + 1):
    passwordList  += random.choice(numbers)
random.shuffle(passwordList)
# print(passwordList)
# converting it back into a string 
passWord = ""
for char in passwordList:
    passWord += char
print(f"your password is: {passWord}")

