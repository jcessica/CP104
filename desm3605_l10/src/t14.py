"""
------------------------------------------------------------------------
Lab 10, Task 14
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-11-23"
------------------------------------------------------------------------
"""

# Imports
from functions import file_copy_n

fh_1 = open("words.txt", "r+", encoding="utf-8")
fh_2 = open("new_words.txt", "a+", encoding="utf-8")

file_copy_n(fh_1, fh_2, 5)

fh_1.close()
fh_2.close()





# Constants

