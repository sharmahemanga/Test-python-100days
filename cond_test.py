# this is to test various conditional statements
try:
    height = int(input("what is your height in cm? : "))
    if height >= 80:
        print("you are eligible for the ride. Please issue the ticket.")
    else:
        print("you are not eligible for the ride. Hence the ticket cannot be issues.")

except ValueError:
    print("Ensure only integer is populated")
