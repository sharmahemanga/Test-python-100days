# Test the random module in python
# import random as rn
# import my_module as md
# random_number = rn.randint(300, 320)
# print(random_number)
# if random_number == md.my_favourite_number:
#     print("wow what a surprise!!")
# else:
#     print("better luck next time")

# Testing random function to check heads or Tails

import random as rn

your_pick = input("what will you would like to pick? \"Heads\" or \"Tails\" ?").lower()
print(your_pick)
spin_result = rn.choice(["heads", "tails"])
print(spin_result)
if your_pick == spin_result:
    print("You have won the toss. What would you like to do?")
else:
    print("You lost the toss")