"""
------------------------------------------------------------------------
Assignment 1, Task 2
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-10-05"
------------------------------------------------------------------------
"""

positive_dig = int(input("Enter a positive two-digit integer: "))

second_dig= positive_dig % 10

first_dig = (positive_dig - second_dig) / 10

difference = first_dig - second_dig

print()
print()

print(f"The difference of the digits of {positive_dig} is {difference:.0f}")

