str = input("String = ")

if str == str[::-1]:
    print("{} is a palindrome".format(str))
else:
    print("{} is not a palindrome".format(str))
