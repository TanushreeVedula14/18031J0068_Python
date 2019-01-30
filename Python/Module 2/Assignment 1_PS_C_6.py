rows = int(input())

for i in range(1,rows):
    for j in range(65,65+7):
        a = chr(j)
        print(a,a.reverse(),end=" ")
    print()
    
