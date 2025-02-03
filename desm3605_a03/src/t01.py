"""
------------------------------------------------------------------------
Assignment 3, Task 1
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-10-20"
------------------------------------------------------------------------
"""

# Imports
from functions import footage_to_acres
# Constants

sqft_num = float(input("Sqft. to acres: "))

acres_num = footage_to_acres(sqft_num)

print(f"{sqft_num} sqft. in acres is {acres_num}")




