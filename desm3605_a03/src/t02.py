"""
------------------------------------------------------------------------
Assignment 3, Task 2
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-10-20"
------------------------------------------------------------------------
"""

# Imports
from functions import lawn_mow_time
# Constants

width1 = float(input("Enter lawn width: "))

length1 = float(input("Enter lawn length: "))

speed1 = float(input("Enter sqft. mowed per minute: "))

lawn_mow = lawn_mow_time(width1, length1, speed1)

print(f"It will take about {lawn_mow} minutes to mow the lawn")