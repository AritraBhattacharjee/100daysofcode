"""
    Author : ARITRA BHATTACHARJEE
    Date : 04-03-2022(DD-MM-YYYY)
"""

# we can create lists,dictionaries,etc with one line of code

# List Comprehensions
n = int(input("Enter the range : "))
lst = [i for i in range(0,n+1) if i%2==0]
print(lst)

# Dictionary Comprehensions
dct = {i : f"item{i}" for i in range(0,n+1) if i%3 ==0}
print(dct)