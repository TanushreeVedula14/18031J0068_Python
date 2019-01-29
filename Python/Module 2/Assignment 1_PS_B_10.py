str = input()

dict = {}
count = 0

for i in str:
    if i in dict:
        count += 1
        list[i] += i
        dict(count,list)
    else:
        count = 1
        list[i] += i
        dict(count,list)
        
print(dict)
