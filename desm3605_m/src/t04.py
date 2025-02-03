"""
-------------------------------------------------------
Midterm B Task 4 Testing
-------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-10-29"
-------------------------------------------------------
"""
# Imports
# your imports here
from t04_functions import get_it

response = input("Enter Y/N: ")

classification = get_it(response)

print(f"{classification:s}")

# your code here
