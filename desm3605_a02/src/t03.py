"""
------------------------------------------------------------------------
Assignment 1, Task 3
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-10-05"
------------------------------------------------------------------------
"""

date = int(input("Enter a date in the format YYYYMMDD: "))

days = int(date % 100)

month = int(((date - days)/100) % 100)

year = int((((date - days)/100) - month)/100)

#In order to fill the MM space with two digts
    
print(f"The reformatted date: {year}/{month:02d}/{days:02d}")

