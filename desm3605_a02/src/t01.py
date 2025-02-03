"""
------------------------------------------------------------------------
Assignment 1, Task 1
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-10-05"
------------------------------------------------------------------------
"""

proj_sales = float(input("Enter the total sales: "))

ANNUAL_TAX = float(18.50)

tax = proj_sales * (ANNUAL_TAX/100)

print("Projected Tax Report")

print("-"*25)

print(f"Total sales:  $ {proj_sales:.2f}")

print(f"Annual tax:   % {ANNUAL_TAX:.2f}")

print("-"*25)

print(f"Tax:          $ {tax:.2f}")




#18.5 percent of total billing 