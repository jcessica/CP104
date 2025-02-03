"""
------------------------------------------------------------------------
Assignment 1, Task 4
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-10-05"
------------------------------------------------------------------------
"""

flyers = int(input("Number of flyers: "))

delivery_p = int(input("Number of delivery people: "))

flyers_left = int(flyers % delivery_p)

flyers_pers = int((flyers - flyers_left)/delivery_p)



print()
print()

print(f"Flyers per delivery person: {flyers_pers:d}")
print(f"FLyers left over: {flyers_left:d}")

