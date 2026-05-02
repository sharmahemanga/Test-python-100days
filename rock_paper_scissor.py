# This code is a fun game of rock, paper, scissor. The computer asks you to pick a value, and then computer picks a value randomly.

import random as rn
''
available_values = ["Rock", "Paper", "Scissor"]
your_input = input("What would you like to select from Rock, Scissor, Paper? ")
computer_picks = rn.choice(available_values)
print(f"The computer has picked - {computer_picks}")
if computer_picks == "Rock":
    if your_input == "Scissor":
        print("Oh no. You lost :(")
    elif your_input == "Paper":
        print("Congratulations. You won")
    else:
        print("It is a draw")
elif computer_picks == "Scissor":
    if your_input == "Paper":
        print("Oh no. You lost :(")
    elif your_input == "Rock":
        print("Congratulations. You won")
    else:
        print("It is a draw")
elif computer_picks == "Paper":
    if your_input == "Rock":
        print("Oh no. You lost :(")
    elif your_input == "Scissor":
        print("Congratulations. You won")
    else:
        print("It is a draw")
else:
    print("You have picked an incorrect value")