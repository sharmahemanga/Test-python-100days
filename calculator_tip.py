# create a tip calculator

print("Welcome to the tip calculator!")
while True:
    try:
        bill = int(input("what was the total bill? "))
        tip_per = int(input("How much tip would you like to give? 10, 12 or 15 "))
        number_ppl = int(input("how many members? "))
        tip_amount = round((bill*tip_per)/100, 2)
        amount_per = round((tip_amount+bill)/number_ppl,2)
        print(amount_per)
        break
    except ValueError:
        print("invalid data type. Enter whole number")
