"""
------------------------------------------------------------------------
Assignment 9, Task 3
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-11-29"
------------------------------------------------------------------------
"""

# Imports
from functions import file_statistics
# Constants

file_handle = open("addresses.txt", "r", encoding="utf-8")

print(file_statistics(file_handle))

file_handle.close()