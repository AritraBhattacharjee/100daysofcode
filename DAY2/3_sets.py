"""
    Author : ARITRA BHATTACHARJEE
    Date : 14-02-2022(DD-MM-YYYY)
"""

st = set()    # Initialising a empty set.
st = set([1,5,6,9,10])
print(st)
print(type(st))
st.add(11)
print(st)

st.remove(10)
print(st)

se = set([1,2,3,4,5,6,7,8,9,10])
s1 = se.union(st)   # To find the union of two sets
print(s1)

s2 = se.intersection(st) # To find the intersection of the two sets
print(s2)

print(se.isdisjoint(st))  # to find the disjoint of the two sets
print(se.issubset(st)) # to find the subset of the two sets
print(s1.issuperset(st)) # to find the superset of the two sets

# Sets in python are similar to set theory. All functions used in set theory are available to be used here.

print(s1.symmetric_difference(s2))  # Finding the symmetric difference 

# More Set Functions: https://www.w3schools.com/python/python_ref_set.asp

"""
    Topics Learnt: 
        1. Set 
        2. Set Functions
        
"""