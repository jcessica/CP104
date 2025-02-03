"""
------------------------------------------------------------------------
Assignment 9, Task 4
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-11-29"
------------------------------------------------------------------------
"""

# Imports
from functions import line_numbering
# Constants

fh_read = open("wilde.txt", "r+", encoding="utf-8")
fh_write = open("oscar.txt", "a+", encoding="utf-8")

line_numbering(fh_read, fh_write)

fh_read.close()
fh_write.close()
