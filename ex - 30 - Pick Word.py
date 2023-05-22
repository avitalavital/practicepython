#!/usr/bin/python3

"""
 open the file with the words
 tern it into a list
 pick a random word from the list
 print the word
"""

import random

words = open("SOWPODS_dictionary").read().split()
# print(words)
print(random.choice(words))
