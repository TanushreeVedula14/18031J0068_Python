# Write a function to return true if the last digit of given number is odd. else return false.

def true_false(num):
    rem = num % 10
    if rem % 2 != 0:
        print(True)
    else:
        print(False)

num = int(input("Enter num = "))

true_false(num)
