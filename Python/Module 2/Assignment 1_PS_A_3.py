# Program to convert binary to decimal

n = int(input())

decimal = 0
p = 0
binary = n

while(binary != 0):
    rem = binary % 10
    decimal = decimal + rem * pow(2,p)
    binary = binary//10
    p += 1
print(decimal)

