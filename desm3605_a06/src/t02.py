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
from functions import detect_prime
# Constants
number = int(input("Prime number: "))

prime = detect_prime(number)

print(f"\n{prime}")