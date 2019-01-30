# Write a function to return 2 the power on n, where n is input to the function.

def num_pow(num):
    
    product = 1
    
    for i in range(num):
        product = product * 2

    return product

num = int(input("Enter power of 2 = "))

pro = num_pow(num)

print("Result = "+str(pro))
