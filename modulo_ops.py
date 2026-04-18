# Test Modulo operations
try:
    x = int(input("Enter the number: \n"))
    z = x % 2
    print(z)
    if z == 0:
        print(f"{x} is an even number")
    else:
        print(f"{x} is not an even number")
except ValueError:
    print("the entered value must be a number")
