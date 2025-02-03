"""
------------------------------------------------------------------------
Lab 3, Task 9
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-09-25"
------------------------------------------------------------------------
"""

sweatband_cost = float(input("Enter sweatband cost: $"))

pants_cost = float(input("Enter pants cost: $"))

jacket_cost = float(input("Enter jacket cost: $"))

total = sweatband_cost+pants_cost+jacket_cost

print()
print()

print("Clothes    Cost")
print(f"Sweatband  ${sweatband_cost:7.2f}")
print(f"Pants      ${pants_cost:7.2f}")
print(f"Jacket     ${jacket_cost:7.2f}")
print(f"Total      ${total:7.2f}")
