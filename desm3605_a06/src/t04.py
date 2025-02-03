"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-11-10"
------------------------------------------------------------------------
"""

# Imports
from functions import count_of_digits
# Constants

number = int(input("Number: "))

digits_c = count_of_digits(number)

print(f"\n{digits_c}")