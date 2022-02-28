# FUNCTIONS IN PYTHON

# def myFunction():
#     print("hello this is my first function")
#     print("i just hope you will like it")

# myFunction() 

# def turnRight():
#     turnLeft()
#     turnLeft()
#     turnLeft()

# def jump():
#     move()
#     turnLeft()



#  the while loop is the loop that will continue going while a particular condition is true
# while not at_goal():
# # while goal != true
#     jump()

# differences between for loops and while loops
# for loops re mainly used when you are iterating over something, may be items in the loop
# and you need to do something with each item that you iterating over
# for example you re iterating over a list of fruits
# fruits = ["apples", "pear", "Orange"]
# for fruit in fruits:
#     print("make sense")

# # or using the for loop with the range function
# for number in range (1, 6):
#     print(number) 
# meanwhile, in while loop, you don't really care about the number of sequence 
# you re iterating over, you just want to carry out a function until you
# a certain condition is met
# note: while loops are a little bit more dangerous than
# than for loops, because in for loops you re setting ahead of time how many
# times you want to iterate over ocurences
# but in while loop, its keeps going forever until a certain true condition because false
# and if you have a condition that never becomes false, then your while loop becomes what is called
# an Infinite loop.

# while not at_goal():
#     if wallInFront():
#         jump()
#     else:
#         move()