import random


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

Choose_Value = input("Enter the value: rock paper scissors ")

print(Choose_Value)

Computer_Choose = ["rock" , "paper" , "scissors"]

print(random.choice(Computer_Choose))

if Choose_Value == "rock" and Computer_Choose == "rock":
    print("Match is tai")

elif Choose_Value == "rock" or "scissors" and Computer_Choose == "paper":
    print("you win")

elif Choose_Value == "Paper"  and Computer_Choose == "rock" or "scissors":
    print("You loose")

else:
    print("Loose")
























