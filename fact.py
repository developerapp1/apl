# def factorial(n): 
#     if n == 0: 
#         return 1
#     else: 
#         return n * factorial(n - 1)  
# num = int(input("Enter any number"))
# result = factorial(num) 
# print(result)



def factorial(n): 
    if n == 0: 
        return 1
    else: 
        return n * factorial(n - 1)  
num = 5
result = factorial(num) 
print(result)