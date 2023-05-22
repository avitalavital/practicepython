#!/usr/bin/python3

print("boo")

"""
open the file
check every name in the file
create an empty dictionary for all of the names as keys
if the name exist in the dictionary add 1 to the value
if the name doesn't exist create a key for it  and add 1 to the value
print the 
"""

file = open("names_list")

names_counter = {}
print(names_counter)

for x in file:
    if x in names_counter:
        names_counter[x] += 1
    else:
        names_counter[x] = 1

print(names_counter)

file.close()
