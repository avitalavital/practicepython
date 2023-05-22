#!/usr/bin/python3

"""
open file one
 open file other
 find overlap:
 1)tern the content of the files to lists
 2)go throw every number in list 1 and check if its in list 2
 3)create an empty list and add the overlapping values into it
 """


one_list = open("one").read().split()
# print(one_list)
other_list = open("other").read().split()
# print(other_list)

overlap_list = []

for number in one_list:
    if number in other_list:
        overlap_list.append(number)
print(overlap_list)

one_list.close()
other_list.close()
