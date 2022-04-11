"""
    Author : ARITRA BHATTACHARJEE
    Date : 21-02-2022(DD-MM-YYYY)
"""

#  Writing line to the file : Whatever previosly existed in the text file, gets replaced by the current input lines
fhand = open("Sample.txt","wt")
line = input("Enter a line to be entered : ")
a = fhand.write(line)  # a contains the total number of characters entered
print("Number of characters entered : ",a)
fhand.close()

#  Appending line to the file : Whatever previously existed in the text files, remains as it is, and the new line gets added at the last.

fhand = open("Sample.txt","at")
line = input("Enter a line to be entered : ")
fhand.write(line)
fhand.close()



"""
    Topics Learnt : 
        1. File Handling
"""