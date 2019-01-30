# Write a function to display give number is odd or even.

def odd_even(num):
    if num % 2 == 0:
        print("{} is even.".format(num))
    else:
        print("{} is odd.".format(num))

num = int(input("Enter num = "))

odd_even(num)
