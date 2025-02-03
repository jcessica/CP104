"""
------------------------------------------------------------------------
Lab 4, Task 15
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-09-30"
------------------------------------------------------------------------
"""

# Imports
from functions import time_split
# Constants

seconds_input = int(input("Enter an amount in seconds: "))

total_time = time_split(seconds_input)


print("In days, hours, minutes, and seconds")
print(total_time)

