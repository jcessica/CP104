"""
------------------------------------------------------------------------
Lab 4, Task 8
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-09-30"
------------------------------------------------------------------------
"""

# Imports

# Constants
from functions import computer_costs

comp_cost = float(input("Enter cost of one computer: "))

comp_bought = int(input("Enter number of computers bought: "))

commiss_perc = float(input("Enter commission percentage: "))

before_commiss, _ = computer_costs(comp_cost,comp_bought,commiss_perc)

_, after_commiss = computer_costs(comp_cost,comp_bought,commiss_perc)

print(f"Cost of computers before commission: {before_commiss:.2f}")

print(f"Cost of computers before commission: {after_commiss:.2f}")

