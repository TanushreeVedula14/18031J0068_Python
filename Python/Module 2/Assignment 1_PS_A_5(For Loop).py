# Print sum of the individuals using for loop

n = int(input())

sum = 0
num = n

for i in range(num):
    rem = num % 10
    sum = sum + rem
    num = num // 10
print(sum)
