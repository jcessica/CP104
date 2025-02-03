"""
------------------------------------------------------------------------
Assignment 3, Task 3
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-10-20"
------------------------------------------------------------------------
"""

# Imports
from functions import extract_date
# Constants

date = int(input("Enter date (YYYYMMDD): "))

extracted = extract_date(date)

year1, _, _ = extracted

_, month1, _ = extracted

_, _, day1 = extracted


print(f"The extracted date is: ({year1:d}, {month1:02d}, {day1:02d})")