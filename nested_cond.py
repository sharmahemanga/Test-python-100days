# This code checks if the user is above 120 cm and more than 18 years old before he is allowed to take the ride
height = int(input("what is your height: \n"))
age = int(input("what is your age: \n"))
if height >= 120:
    if age < 12:
        print("Please pay $5")
    elif age >=12 and age<18:
        print("Please pay $7 ")
    else:
        print("Please pay $20")
else:
    print("Sorry, you must be atleast 120cm tall to take the ride")
