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


####Player will select the option(Rock paper scissor)

player = input("What do you want to choose: rock paper scissors").lower()

print(player)


if player == "rock":
    print(rock)
elif player == "paper":
    print(paper)
else:
    print(scissors)
####Computer will select random option(Rock paper scissor)

computer_choice = random.choice(["rock" , "paper" , "scissors"])

print(computer_choice)

if computer_choice == "rock":
    print(rock)
elif computer_choice == "paper":
    print(paper)
else:
    print(scissors)


#### We will apply the logic for the game


if player == "rock" and computer_choice == "scissors":
        print("Player won the game")

elif player == "paper" and computer_choice == "rock":
        print("Player won the game")

elif player == "scissors" and computer_choice == "paper":
        print("Player won the game")

elif computer_choice == "rock" and player == "scissors":
        print("Computer won the game")

elif computer_choice == "paper" and player == "rock":
        print("Computer won the game")

elif computer_choice == "scissors" and player == "paper":
        print("Computer won the game")

else:
        print("Game is draw, play again")



































