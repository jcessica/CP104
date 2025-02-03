"""
------------------------------------------------------------------------
Lab 10, Task 5
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-11-23"
------------------------------------------------------------------------
"""

# Imports
from functions import customer_append

fh = open("customers.txt", "a", encoding="utf-8")
# Constants

fields = ['\n\35612', 'David', 'Brown', 237.56, '2008-10-10']


customer_append(fh, fields)

fh.close()
