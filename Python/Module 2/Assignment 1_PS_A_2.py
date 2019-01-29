# Print 'n' even numbers using while loop

n = int(input())
count = 0
sum = 0
i = 1

while count < n:
    if i % 2 == 0:
        sum += i
        #print(i)
        count += 1
    i += 1

print(sum)
    
