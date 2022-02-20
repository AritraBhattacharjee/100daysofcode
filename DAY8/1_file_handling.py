"""
    Author : ARITRA BHATTACHARJEE
    Date : 20-02-2022(DD-MM-YYYY)
"""
# Opening file with open() function
fhand = open("Sample.txt") # returns a file handle, what points to the file
content = fhand.read()
print(content)
print(fhand.readline())  # reads line by line
print(fhand.readline())  
print(fhand.readlines())  # Returns the list of lines in the file


fhand.close()  # closing the opened file handle. This disallocates the memory.

"""
Various Modes to open a file : 
    1. "r" : Read Mode
    2. "w" : Write Mode
    3. "a" : Append Mode
    4. "x" : Exclusive Mode
    5. "b" : Binary Mode
    6. "+" : Read + Write
    7. "t" : Text Mode
"""

# For iterating the file line by line
handle = open("sample2.txt")
for line in handle:
    print(line)
handle.close()

# Opening  file with with-block : we no need to explicitly close the opened file handle

with open('Sample.txt') as f:
    lines = f.read()
    print(f.tell())  # It returns the position of the file pointer
    print(lines)

f.seek(10)  # Reset the file pointer to the given integer-th position


"""
    Topics Learnt : 
        1. File Handling
"""