# Given a string, return a new string where the first and last chars have been exchanged.

def front_back(string):
    for i in string:
        if len(string) <= 0:
            return string
        else:
            return string[-1:] + string[1:-1] + string[:1]

string = input("Enter string = ")

result = front_back(string)

print("Result = "+str(result))
        

