# Print sum of the individuals using while loop

n = int(input())

sum = 0
num = n

while num != 0:
    rem = num % 10
    sum = sum + rem
    num = num // 10
print(sum)



