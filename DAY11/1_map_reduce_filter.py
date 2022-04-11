

num = ["1","2","3","4","5","6","7","8","9","0"]

# For typecasting each element to integer, two ways 

for item in range(len(num)):
    num[item] = int(num[item])

print(num)

#The map function way: Map function is a function that implements a specific function to the whole list
num = list(map(int,num))
print(num)

# we can implement any function on a list using map function

cube = list(map(lambda x:x*x*x,num))  # making a list of cube of all elements in the list cube
print(cube)


# Filter : Makes a list for numbers which return true for a function
def is_greater5(n):
    return n>5

num_greater_than5 = list(filter(is_greater5,num))
print(num_greater_than5)

# Reduce  : Helps in better iteration in list.
from functools import reduce
lst = [1,2,3,4,5,6,7,8,9]
sums = reduce(lambda x,y:x+y,lst)
product = reduce(lambda x,y:x*y,lst)
print("Sum of the elements in the list ",sums)
print("Product of the elements in the list ",product)

"""
    Topics Learnt : 
        1. Map Function
        2. Filter Function
        3. Reduce Function
"""