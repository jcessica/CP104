"""
------------------------------------------------------------------------
Lab 08, Task 15
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-11-08"
------------------------------------------------------------------------
"""

# Imports
from functions import symmetric_difference
# Constants

source1 = [10, 3, 10, 3, 1,7,7,7,7]

source2 = [8, 2, 7, 3, 6, 10, 32, 99,1,1,1,1]

sym = symmetric_difference(source1, source2)

print(f"{source1}\n{source2}\n{sym}")