"""
------------------------------------------------------------------------
Assignment 7, Task 3
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-11-16"
------------------------------------------------------------------------
"""

# Imports
from functions import get_indexes,list_positives
# Constants

numbers = list_positives()


target = int(input("Target number:"))

index = get_indexes(numbers,target)

print(index)

