"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-11-24"
------------------------------------------------------------------------
"""

# Imports

from functions import valid_isbn

# Constants

isbn = '978-3-16-14--10-0'

is_valid = valid_isbn(isbn)

print(f"isbn: {isbn}\n")
print(f"Valid: {is_valid}")


