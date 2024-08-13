# Recursive Functions = function calling itself
# eg:- factorial of n! = n*(n-1)!   factorial of 0! = 1

def fact(n):
    if n==0:
        return 1
    else:
        res = n*fact(n-1)
        return res

result = fact(5)
print(result)




