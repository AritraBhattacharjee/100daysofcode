"""
    Author : ARITRA BHATTACHARJEE
    Date : 14-02-2022(DD-MM-YYYY)
"""

dc = {}  # empty dictionary

dc = {"Name":"Aritra","City":"Durgapur","Food":"Biriyani"}
print(dc)
print(type(dc))

dc["Clothes"] = "Casuals"
print(dc)

del dc["Clothes"]
print(dc)

print(dc.get("Name"))
dc.update({"Education":"B.Tech CSE"})
print(dc)

dc2 = dc.copy()
print(dc2)

print(dc.items())
print(dc.keys())
print(dc.values())

# More Dicitonary Functions : https://www.w3schools.com/python/python_ref_dictionary.asp



"""
    Topics Learnt: 
        1. Dictionary 
        2. Dictionary Functions
        
"""