"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-11-02"
------------------------------------------------------------------------
"""

# Imports
from functions import range_addition
# Constants

start = int(input("Start:"))

increment = int(input("Increment:"))
                
count = int(input("Count: "))
            
counting = range_addition(start, increment, count)

print(counting)