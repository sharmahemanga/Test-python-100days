from operator import concat
b = ""
fruits = ["Apple", "Peach", "Pear"]

for i in fruits:
    if b == "":
        b = concat(b, i + "Pie")
    else:
        b = concat(b, ", " + i + "Pie")

print(b)
