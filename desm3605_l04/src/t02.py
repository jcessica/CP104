"""
------------------------------------------------------------------------
Lab 4, Task 2
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-09-30"
------------------------------------------------------------------------
"""

# Imports

from functions import circumference


radius_calc = float(input("Radius: "))

circ_calc = circumference(radius_calc)

print(f"Circumference: {circ_calc:.2f}")