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

#Write your code below this line 👇

import random

game_choices = [rock, paper, scissors]

computer_choice = random.choice(game_choices)


user_choice = input("Please make a choice: 1 - rock, 2 - paper, OR 3 - scissors: \n")
if user_choice == "1":
  user_choice = rock
elif user_choice == "2":
  user_choice = paper
elif user_choice == "3":
  user_choice = scissors
else:
  print("Invalid Selection: Please make a choice: 1 - rock, 2 - paper, OR 3 - scissors ")

if user_choice == computer_choice:
  print("User: ", user_choice)
  print("Computer: ", computer_choice)
  print("DRAW!!!!")
elif user_choice == rock and computer_choice == paper:
  print("User: ", user_choice)
  print("Computer: ", computer_choice)
  print("SORRY, YOU LOSE!")
elif user_choice == rock and computer_choice == scissors:
  print("User: ", user_choice)
  print("Computer: ", computer_choice)
  print("YOU WIN!!")
elif user_choice == paper and computer_choice == rock:
  print("User: ", user_choice)
  print("Computer: ", computer_choice)
  print("YOU WIN!!!!")
elif user_choice == paper and computer_choice == scissors:
  print("User: ", user_choice)
  print("Computer: ", computer_choice)
  print("SORRY, YOU LOSE!")
elif user_choice == scissors and computer_choice == rock:
  print("User: ", user_choice)
  print("Computer: ", computer_choice)
  print("SORRY, YOU LOSE!")
elif user_choice == scissors and computer_choice == paper:
  print("User: ", user_choice)
  print("Computer: ", computer_choice)
  print("YOU WIN!!")
else:
  print("Please pick a correct choice of rock, paper, or scissors")
  