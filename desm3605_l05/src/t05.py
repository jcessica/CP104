"""
------------------------------------------------------------------------
Lab 5, Task 5
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-10-12"
------------------------------------------------------------------------
"""

# Imports
from functions import is_leap
# Constants

year_ent = int(input("Enter year: "))

year_valid = is_leap(year_ent)

print(f"Is this year a leap year: {year_valid}")