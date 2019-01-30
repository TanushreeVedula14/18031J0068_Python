l = int(input("Enter low = "))
h = int(input("Enter high = "))

a = 0
b = 1
c = 0

for i in range(h):
    if c <= h:
        if c >= l:
            print(c)
        a = b
        b = c
        c = a + b
