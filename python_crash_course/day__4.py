import random
# randomInt = random.randint(1, 10)
# print(randomInt)

# randomFloat = random.random() * 5
# print(randomFloat)

# loveScore = random.randint(1, 100)
# print(f"your love score is {loveScore}")

# the use of random seed
# a seed number is used to save the state of a random function
# it specifies the starting point when a computer generates a random number
# this can be any number, but it usually comes from the current system's clock or time

# A computer counts seconds from January 1, 1970 — a system called Unix time. 
# At time I am writing this sentence it is 11:01:46 EST on February 5, 2017: 
# 1486310506 seconds after 1-1-1970 (you can find the current Unix time here). 
# Having such a large range for seeds (0 to 1+ billion)
# pretty much ensures that you don’t get the same random seed isn’t used twice — unless you want to.
# note: if you want to get the same random number, then always use seed to specify that number
# 
# uses of random seed
# this is used in the generation of a pseudo-random encryption key
# Encryption keys are an important part of computer security. These are the kind of secret keys
# which used to protect data from unauthorized access over the internet.

# random.seed(3)
# # print a random number between 1 and 1000.
# print(random.randint(1, 1000))  
# # if you want to get the same random number again then,
# random.seed(3) 
# print(random.randint(1, 1000))  
# # If seed function is not used
# # Gives totally unpredictable responses.
# print(random.randint(1, 1000))

# testSeed = int(input("create a seed number:\n"))
# randomSide = random.randint(0, 1)
# if randomSide == 1:
#     print("Heads")
# else:
#     print("Tails")

# python list, usually called a data structure
# stateInNigeria = ["imo", "enugu", "fct", "kaduna", "kano", "katsina", "anambra", "abia", "ebonyi", "osun"]
# stateInNigeria.append("rivers")
# stateInNigeria.extend(["lagos", "Ibadan"])
# print(stateInNigeria)

# the split string method in lists and the random seed number
# friendsSeed = int(input("create a seed number\n"))
# random.seed(friendsSeed)
# namesOfFriends = input("give me everybody's names\n")
# # splitting the names in arrrays
# names = namesOfFriends.split(", ")
# # getting the total number of items in list using the len()
# totalNum = len(names)
# # this allows us to generate random numbers between o and the last index
# randomChoice = random.randint(0, totalNum -1)
# personThatPays = names[randomChoice]
# print(personThatPays + " is going to buy the meal today")

# # a shorter way to write the above last 2 lines of code
# personThatPays = random.choice(names)

# creating a rock paper scissors game
# the rules of the game
# rock wins against scissors
# scissors win against paper
# paper wins against rock

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
else:
  print(game_images[user_choice])

  computer_choice = random.randint(0, 2)
  print("Computer chose:")
  print(game_images[computer_choice])

  if user_choice == 0 and computer_choice == 2:
    print("You win!")
  elif computer_choice == 0 and user_choice == 2:
    print("You lose")
  elif computer_choice > user_choice:
    print("You lose")
  elif user_choice > computer_choice:
    print("You win!")
  elif computer_choice == user_choice:
    print("It's a draw") 
