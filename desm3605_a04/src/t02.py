"""
------------------------------------------------------------------------
Assignment 4, Task 2
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-10-27"
------------------------------------------------------------------------
"""

# Imports
from functions import pollution_ranking

# Constants

air_quality_index = int(input("Enter air quality index (AQ1): "))

pollution = pollution_ranking(air_quality_index)

print(pollution)