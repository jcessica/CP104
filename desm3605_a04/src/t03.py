"""
------------------------------------------------------------------------
Assignment 4, Task 3
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-10-27"
------------------------------------------------------------------------
"""

# Imports
from functions import largest_average
# Constants

val1 = float(input("Enter value: "))

val2 = float(input("Enter value: "))

val3 = float(input("Enter value: "))

average = largest_average(val1, val2, val3)

print(average)