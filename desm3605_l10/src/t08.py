"""
------------------------------------------------------------------------
Lab 10, Task 8
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-11-23"
------------------------------------------------------------------------
"""

# Imports
from functions import append_increment

fh = open("numbers.txt", "a+", encoding="utf-8")

# Constants

number = append_increment(fh)

fh.close()



