"""
------------------------------------------------------------------------
Lab 10, Task 3
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-11-23"
------------------------------------------------------------------------
"""

# Imports
from functions import customer_best

# Constants

fh = open("customers.txt", "r", encoding="utf-8")

print(customer_best(fh))

fh.close()