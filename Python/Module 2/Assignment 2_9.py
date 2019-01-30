# round_sum(16, 17, 18) → 60
# round_sum(12, 13, 14) → 30
# round_sum(6, 4, 4) → 10

def round_sum(x,y,z):
    return round10(x) + round10(y) + round10(z)

def round10(num):
    rd = num % 10
    if rd >= 5:
        return num + 10 - rd
    return num - rd

x = int(input("Enter x = "))
y = int(input("Enter y = "))
z = int(input("Enter z = "))

result = round_sum(x,y,z)

print(str(result))

