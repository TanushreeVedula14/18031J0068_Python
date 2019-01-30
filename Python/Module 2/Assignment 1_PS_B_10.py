str = input()

dict = {}

for i in range(len(str)):
    if str[i] in dict:
        continue
    else:
        dict[str[i]] = str.count(str[i])
        
dict1 = {}

for key, value in dict.items():
    if value in dict1:
        dict1[value].append(key)
    else:
        dict1[value] = [key]
        
print(dict1)
