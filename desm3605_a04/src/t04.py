"""
------------------------------------------------------------------------
Assignment 4, Task 4
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-10-27"
------------------------------------------------------------------------
"""

# Imports
from functions import colour_combine
# Constants

rgb_colour1 = str(input('Enter "red" "green", or "blue": '))

rgb_colour2 = str(input('Enter "red" "green", or "blue": '))

mixture = colour_combine(rgb_colour1, rgb_colour2)

print(f"The resulting mix is {mixture}")



