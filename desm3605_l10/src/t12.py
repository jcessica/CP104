"""
------------------------------------------------------------------------
Lab 10, Task 12
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-11-23"
------------------------------------------------------------------------
"""

# Imports
from functions import find_shortest

fh = open("words.txt", "r", encoding="utf-8")

short = find_shortest(fh)

print(short)

fh.close()

# Constants

