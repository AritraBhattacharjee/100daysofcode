"""
    Author : ARITRA BHATTACHARJEE
    Date : 14-02-2022(DD-MM-YYYY)
"""
#   LIST

lst = []  # empty list
lst = [1,3,5,7,9,8,4,6,2,0]
print(type(lst))
print(lst[2])
print(lst[2:6])  # List slicing
print(lst[::2])
print(len(lst))  # Total elements in List
print(max(lst))  # Finding the maximum element in the list
print(min(lst))  # Finding the minimum element in the list
lst.append(10)   # Adding element to the end of the list
print(lst)

lst.insert(1,22) # Adding Element to a specific index of the list
print(lst)

lst.remove(10)   # Removing a specific element 
print(lst)

lst.pop()   # Removing the last element of the list
print(lst)

lst.sort()  # Sorting the list
print(lst)

lst.reverse() # Reversing the list
print(lst)

#  More List Functions are : https://www.datacamp.com/community/tutorials/python-list-function

#  TUPLES -> Non Mutable
tp = ()  # Empty Tuple
tp = (5,6,7,8)
print(tp)
print(type(tp))
print(len(tp))
print(max(tp))
print(min(tp))
print(sum(tp))

# No Functions which tend to mutate/change the tuple is not allowed like append,pop,insert,etc.

"""
    Topics Learnt: 
        1. Lists 
        2. List Functions
        3. Tuples
"""