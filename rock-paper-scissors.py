
# CACHIPUN - Chile
import random
print("Choose your poisin")
print("1 = rock")
print("2 = paper")
print("3 = scissors")
player = input("Pick your poison: ")  # Player choice

answers = ["rock", "paper", "scissors"]  # list of possible answers

computer = random.choice(answers)  # Computer player (random)
if player == "1" and computer == "rock":
    print("Draw")
if player == "1" and computer == "paper":
    print("Computer win")
if player == "1" and computer == "scissors":
    print("You win")
if player == "2" and computer == "scissors":
    print("Draw")
if player == "2" and computer == "rock":
    print("Computer win")
if player == "2" and computer == "paper":
    print("You win")
if player == "3" and computer == "rock":
    print("Draw")
if player == "3" and computer == "paper":
    print("Computer win")
if player == "3" and computer == "scissors":
    print("You win")
