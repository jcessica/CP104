"""
------------------------------------------------------------------------
Lab 6, Task 5
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-10-23"
------------------------------------------------------------------------
"""

# Imports

# Constants

from functions import draw_rectangle

height = int(input("Height: "))

width = int(input("Width: "))

char = str(input("Character: "))

print()
draw_rectangle(height, width, char)