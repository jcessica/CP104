"""
------------------------------------------------------------------------
Lab 08, Task 11
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-11-08"
------------------------------------------------------------------------
"""

# Imports
from functions import dot_product,generate_integer_list
# Constants

num = int(input("Enter n: "))#number of iterations

low = int(input("Enter low: "))#start of range

high = int(input("Enter high: "))#end of range

source1 = generate_integer_list(num, low, high)

source2 = generate_integer_list(num, low, high)

dotted = dot_product(source1, source2)

print(f"{source1}\n{source2}\n\n{dotted}")
