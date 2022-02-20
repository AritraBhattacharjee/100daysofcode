"""
    Author : ARITRA BHATTACHARJEE
    Date : 19-02-2022(DD-MM-YYYY)
"""

# When a function is calling itself, with changed values as parameters,  it is called a recursive function and the process is called recursion. One base case is required for recursion, which helps the recursion to stop at a desired point of time, else it would never stop.

# Factorial of a number

def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return (n*fact(n-1))

n = int(input("Enter a number : "))
print(fact(n))


# Fibonacci Series
def fibonacci(n):
    if(n==0):
        return 0
    if n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

a = int(input("Enter the range for fibonacci series : "))
for i in range(a):
    print(fibonacci(i),end=" ")

"""
    Topics Learnt : 
        1. Recursion
"""