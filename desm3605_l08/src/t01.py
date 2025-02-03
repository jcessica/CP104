"""
------------------------------------------------------------------------
Lab 08, Task 1
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-11-09"
------------------------------------------------------------------------
"""

# Imports
from functions import get_weekday_name

# Constants

day = int(input("Day: "))

name = get_weekday_name(day)

print(name)