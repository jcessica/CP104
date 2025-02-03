"""
------------------------------------------------------------------------
Assignment 9, Task 5
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-11-29"
------------------------------------------------------------------------
"""

# Imports
from functions import student_stats
# Constants

file_handle = open("students.txt", "r+", encoding="utf-8")

print(student_stats(file_handle))

file_handle.close()