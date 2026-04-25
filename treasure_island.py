# Practice project for treasure island week 3
try:
    print("Welcome to the Treasure Island")
    direction = input("You are at the crossRoad. Where do you want to go? \"left\" or \"right\"? ").lower()
    if direction == "left":
        swim_wait = input("Do you want to swim or do you want to wait? ")
        if swim_wait == "wait":
            door = input("Which door do you want to select. Red, yellow or Blue? ")
            if door == "yellow":
                print("Congratulations! You win!")
            elif door == "Blue" or door == "Red":
                print("Sorry. It is game over")
            else:
                print("Please select out of the 3 colour options provided.")
        else:
            print("Sorry, it is game over.")
    elif direction == "Right":
        print("Sorry it is game over.")
    else:
        print("It is a wrong value. Enter the right value")
except ValueError:
    print('You should\'ve entered a valid value')





