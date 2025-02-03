"""
------------------------------------------------------------------------
Lab 4, Task 9
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-09-30"
------------------------------------------------------------------------
"""

# Imports

# Constants

from functions import fraction_product

fraction1_num = int(input("Enter a numerator for fraction 1: "))

fraction1_den = int(input("Enter a denominator for fraction 1: "))

print()

fraction2_num = int(input("Enter a numerator for fraction 2: "))

fraction2_den = int(input("Enter a denominator for fraction 2: "))

numer_,_,_ = fraction_product(fraction1_num,fraction1_den,fraction2_num,fraction2_den)

_,denom_,_ = fraction_product(fraction1_num,fraction1_den,fraction2_num,fraction2_den)

_,_,decimal_ = fraction_product(fraction1_num,fraction1_den,fraction2_num,fraction2_den)

print()

print(f"Numerator of the fraction product: {numer_:d}")

print(f"Denominator of the fraction product: {denom_:d}")

print(f"Decimal form: {decimal_:.2f}")

