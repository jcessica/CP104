"""
------------------------------------------------------------------------
Lab 5, Task 7
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-10-12"
------------------------------------------------------------------------
"""

# Imports
from functions import get_pay
# Constants

wage_hourly = float(input("Enter hourly wage: "))

hours = float(input("Enter hours worked: "))

net_pay = get_pay(wage_hourly,hours)

print(f"Your net payment after tax deductions is {net_pay:.2f} ")

