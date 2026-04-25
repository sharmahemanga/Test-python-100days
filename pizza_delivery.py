# This code is to test the conditional statements and write a program to determine the price of a pizza

size = input("what size do you want? S, M, L: ")
pepperoni = input("Do you want pepperoni on your pizza (y/n): ")
extra_cheese = input("Do you want extra cheese? y or n: ")
bill = 0
small_pizza = 15
medium_pizza = 20
large_pizza = 25
cheese_price = 1
pepperoni_price = 2

if size == "S":
    if pepperoni == "y":
        bill = pepperoni_price + small_pizza
    else:
        bill = small_pizza
    if extra_cheese == "y":
        bill += 1
    print(f"your total bill is {bill}")
elif size == "L":
    if pepperoni == "y":
        bill = pepperoni_price + large_pizza
    else:
        bill = large_pizza
    if extra_cheese == "y":
        bill += 1
    print(f"your total bill is {bill}")
else:
    if pepperoni == "y":
        bill = pepperoni_price + medium_pizza
    else:
        bill = medium_pizza
    if extra_cheese == "y":
        bill += 1
    print(f"your total bill is {bill}")

