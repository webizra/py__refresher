# DAY3: control flow and logical operator 

# rollercoaster app
print("welcome to the rollercoaster")
# height = int(input("what is your height in cm?"))
# if else condition using the comparison operators > < >= <= == !=
# if height >= 120:
#     print("you can ride the rollercoaster:")
# else:
#     print("sorry, you can't ride a rollercoaster")

# if else condition using the modulo operator %
# the modulo operator is used to get the remainder of a division, 
# the % is considered an arithmetic operator in python
# number = int(input("which number dp you want to choose"))
# if number % 2 == 0:
#     print("this is an even number")
# else:
#     print("this is an odd number")

# nested if/else statements
# if height >= 120:
#     print("you can ride the rollercoaster:")
#     age = int(input("what is your age?"))
#     if age <= 12:
#         print("you have a child discount, please pay $5")
#     elif age <= 18:
#         print("you can pay $7")
#     else:
#         print("please pay $12")
# else:
#     print("sorry, you can't ride a rollercoaster")

# bmi calculator with if else statements
# weight = float(input('enter your weight in m:'))
# height = float(input("what is your height in cm?"))
# bmi = round(weight / height ** 2 )


# if bmi < 18.5:
#     print (f"your bmi is {bmi}, you re underweight.")
# elif bmi < 25:
#     print (f"your bmi is {bmi}, you have a normal weight")
# elif bmi < 30:
#     print (f"your bmi is {bmi}, you are overweight")
# elif bmi < 35:
#     print (f"your bmi is {bmi}, you are obese")
# else:
#     print (f"your bmi is {bmi}, you are clinically obese")

# how to find a leap year, coding challenge
# this is how you work out whether a particular year is a leap year or not
# if the year is evenly divisible by 4 its a leap year
# except the year is also evenly divisible by 100 then its not a leap year
# unless the year is also evenly divisible by 400 then its now a leap year
# e.g. the year 2000
# 2000 / 4 = 500 (a leap year)
# 2000 / 100 = 20 (not a leap year)
# 2000 / 400 = 5 (a leap year)
# so year 2000 was a leap year

# e.g. the year 2100 was not a leap year
# 2100 / 4 = 525 (a leap year)
# 2100 / 100 = 21 (not a leap year)
# 2100 / 400 = 5.25 (not a leap year)
# year = int(input("which year do you want to check"))
# if year % 4 == 0:
#     print("leap year")
#     if year % 100 == 0:
#         print("not leap year") 
#         if year % 400 == 0:
#             print("leap year")
#         else:
#             print("not leap year")
#     else:
#         print("leap year")
# else:
#     print("not a leap year")

# rollercoaster app with multiple if statements
# print("welcome to the rollercoaster")
# height = int(input("what is your height in cm?"))
# bill = 0

# if height >= 120:
#     print("you can ride the rollercoaster:")
#     age = int(input("what is your age?"))
#     if age <= 12:
#         bill = 5
#         print("child tickets are $5")
#     elif age <= 18:
#         bill = 7
#         print("teens tickets are $7")
#     elif age >= 45 and age <= 55:
#         print("it's fine, you can have a free ride on us!")
#     else:
#         bill = 12
#         print("adults tickets are $12")
#     wantsPhoto = input("do you want a photo taken Y or N.")
#     if wantsPhoto == "Y":
#         bill += 3
#     print(f"your final bill is {bill}")
# else:
#     print("sorry, you have to grow taller before you can ride")

# # building a love calculator with logical operators in python
# print("welcome to the love calculator")
# name1 = input("what is your name?\n")
# name2 = input("what is their name?\n")

# combinedStr = name1 + name2
# lowerCaseString = combinedStr.lower()

# # now lets count number of times letters from the words true love appeared
# t = lowerCaseString.count("t")
# r = lowerCaseString.count("r")
# u = lowerCaseString.count("u")
# e = lowerCaseString.count("e")

# true = t + r + u + e

# l = lowerCaseString.count("l")
# o = lowerCaseString.count("o")
# v = lowerCaseString.count("v")
# e = lowerCaseString.count("e")

# love = l + o + v + e
# loveScore = int(str(true) + str(love))
# print(loveScore)
# if loveScore < 10 or loveScore > 90:
#     print(f"your love score is {loveScore}, you go together like coke and mentos")
# elif loveScore>= 40 and loveScore <=50:
#     print(f"your love score is {loveScore}, you are alright together")
# else:
#     print(f"your score is {loveScore}")

# the treasure island app, your mission is to find the treasure
# print("welcome to treasure island.")
# print("your mission is to find the treasure.")
# choice1 = input('you\'re at a crossroad, where do you want to go? Type "left" or "right". ').lower()
# if choice1 == "left":
#     choice2 = input('you\'ve come to a lake. there is an island in the middle of the lake. type "wait" to wait for a boat. type "swim" to swim accros').lower()
#     if choice2 == "wait":
#         choice3 = input("you have arrived at the island unharmed. there is a house with 3 doors. one red, one yellow and one blue. which color do you choose ").lower()
#         if choice3 == "red":
#             print("its a room full of fire. game over.")
#         elif choice3 == "yellow":
#             print("you found the treasure you win.")
#         elif choice3 == "blue":
#             print("you fell into a pit, you loser")
#         else:
#             print("you wasted too much time, game over")
#     else:
#         print("you got attacked by an angry bird")
# else:
#     print("you have fallen into a hole. game over")

print("welcome to the rollercoaster")