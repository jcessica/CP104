"""
------------------------------------------------------------------------
Lab 08, Task 7
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-11-08"
------------------------------------------------------------------------
"""

# Imports
from functions import list_categorize,generate_integer_list
# Constants
num = int(input("Enter n: "))#number of iterations

low = int(input("Enter low: "))#start of range

high = int(input("Enter high: "))#end of range

values = generate_integer_list(num, low, high)

category = list_categorize(values)

print(f"{values}\n\n{category}")
