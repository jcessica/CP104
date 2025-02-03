"""
------------------------------------------------------------------------
Assignment 9, Task 1
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-11-29"
------------------------------------------------------------------------
"""

# Imports
from functions import file_top
# Constants

file_handle = open("students.txt", "r", encoding="utf-8")

file_top(file_handle, 5)

file_handle.close()