"""
------------------------------------------------------------------------
Assignment 9, Task 2
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-11-29"
------------------------------------------------------------------------
"""

# Imports
from functions import read_integers
# Constants

file_handle = open("numbers.txt", "r", encoding="utf-8")

print(read_integers(file_handle))

file_handle.close()

