"""
------------------------------------------------------------------------
Assignment 3, Task 4
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-10-20"
------------------------------------------------------------------------
"""

# Imports
from functions import multiply_fractions
# Constants

num_1 = int(input("Numerator of first fraction: "))

den_1 = int(input("Denominator of first fraction: "))

num_2 = int(input("Numerator of second fraction: "))

den_2 = int(input("Denominator of second fraction: "))

fraction = multiply_fractions(num_1, den_1, num_2, den_2)

print(f"Fraction numerator,denominator and decimal: {fraction}")