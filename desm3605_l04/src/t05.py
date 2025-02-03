"""
------------------------------------------------------------------------
Lab 4, Task 5
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-09-30"
------------------------------------------------------------------------
"""

# Imports

# Constants

from functions import right_triangle

adjacent_1 = float(input("Adjacent length of triangle: "))

opposite_1 = float(input("Opposite length of triangle: "))

hypotenuse, _, _ = right_triangle(adjacent_1,opposite_1) 

_,perimeter, _ = right_triangle(adjacent_1,opposite_1) 

_, _,area = right_triangle(adjacent_1,opposite_1) 

print(f"Hypotenuse:{hypotenuse:.1f}")

print(f"Perimeter:{perimeter:.1f}")

print(f"Area:{area:.1f}")

