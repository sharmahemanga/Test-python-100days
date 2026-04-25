# This code checks if the user is above 120 cm and more than 18 years old before he is allowed to take the ride
height = int(input("what is your height: \n"))
age = int(input("what is your age: \n"))
bill = 0
if height >= 120:
    if age < 12:
        bill = 7
        print("Please pay $5")
    elif age >= 12 | age < 18:
        bill = 12
        print("Please pay $7 ")
    else:
        bill = 20
        print("Please pay $20")
    need_pic = input("Do you want a photo (y/n)? \n")
    if need_pic == "y":
        bill += 3
    print(f"total price of the ticket including the pic is {bill}")
else:
    print("Sorry, you must be atleast 120cm tall to take the ride")
