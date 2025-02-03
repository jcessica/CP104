"""
------------------------------------------------------------------------
Lab 5, Task 12
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-10-12"
------------------------------------------------------------------------
"""

# Imports
from functions import pay_raise
# Constants

status = str(input("Enter status F or P: "))

years = int(input("Enter years: "))

salary = float(input("Enter salary: " ))


newsal = pay_raise(status, years, salary)

print(newsal)