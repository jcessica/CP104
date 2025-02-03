"""
------------------------------------------------------------------------
Assignment 3, Task 5
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-10-20"
------------------------------------------------------------------------
"""

# Imports
from functions import falling_distance
# Constants

falltime = int(input("Enter falling time of object: "))

dist = falling_distance(falltime)

print(f"Object has fallen a distance of {dist:.2f} meters")

