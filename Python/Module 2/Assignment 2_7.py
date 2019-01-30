# Given 2 ints, a and b, return their sum. However, sums in the range 10..19
# inclusive, are forbidden, so in that case just return 20.


def sorta_sum(x,y):
    return x + y

x = int(input("Enter 'x' = "))
y = int(input("Enter 'y' = "))

sum = sorta_sum(x,y)

if sum >= 10 and sum <= 20:
    print("Result = 20")
else:
    print("Result = "+str(sum))
