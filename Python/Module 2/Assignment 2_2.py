# Write a function to display biggest of given 3 numbers.

def biggest(x,y,z):
    if x > y:
        print("{} is biggest".format(x))
    elif y > z:
        print("{} is biggest".format(y))
    else:
        print("{} is biggest".format(z))

x = int(input("Enter 'x' = "))
y = int(input("Enter 'y' = "))
z = int(input("Enter 'z' = "))

biggest(x,y,z)
