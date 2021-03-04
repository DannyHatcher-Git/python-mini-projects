# Dictoionary assigning words to numbers
import random
answers = {"scissors": 1, "rock": 0, "paper": 2}
# print(answers["scissors"])  # print assigned number
computer = random.choice(["scissors", "rock", "paper"])
# computer = random.choice(list(answers.keys())) # randomly choose something in the list which is from the var dictionary keys (words)
# computer = random.choice(list(answers.values())) # randomly choose something in the list which is from the var dictionary value (number)
user = input("Please pick rock, paper or scissors: ")

# checking answers dictionary and if the user input doesn't match then ask again
# replace ["scissors etc"] with list(answer.keys())
while user not in ['scissors', 'paper', 'rock']:
    user = input("Make sure you put rock, paper or scissors: ")

# print("USER -" + user + "\nCOMPUTER -" + computer) # Long form
# print("USER - {0} \nCOMPUTER - {1}".format(user,computer)) # using fomrat at the end with reference to the variables

print(f"USER - {user} \nCOMPUTER - {computer}")

user_choice = answers[user]
computer_choice = answers[computer]


if (user_choice < computer_choice and abs(user_choice - computer_choice) == 1) or (user_choice > computer_choice and abs(user_choice - computer_choice) == 2):
    print(f"USER with {user} - WIN!")
elif user_choice == computer_choice:
    print("==TIE==")
else:
    print(f"COMPUTER with {computer} - WIN!")


# first question (user < computer) second qeustion (user - computer =1) both true I win
# first question(0 rock < 1 scissor [true]) and second question(0 rock - 1 scissor ==1 [true]) win
# first question(0 rock < 2 paper [true]) and second question(0 rock - 2 paper ==1 [false]) lose (second)
# first question(1 scissors < 2 paper [true]) and second question(1 scissors - 2 paper ==1 [true]) win
# first question(1 scissors < 0 rock [false]) and second question(1 scissors - 0 rock ==1 [true]) lose (first)
# (issue) first question(2 paper < 0 rock [false]) and second question(2 paper - 0 rock ==1 [false]) lose (both)
# first question(2 paper < 1 scissors [false]) and second question(2 paper - 1 scissors ==1 [true]) lose (first)
# (solution) first question(2 paper > 0 rock [true]) and second question(2 paper - 0 rock ==2 [true]) win
