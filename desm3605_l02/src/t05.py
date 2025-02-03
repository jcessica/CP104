"""
------------------------------------------------------------------------
Lab 2, Task 5
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-09-19"
------------------------------------------------------------------------
"""

# Imports

# Constants

#Records user's hourly pay as a float, Ex: 14.96$/hr
hourly_pay = float(input("Hourly rate of pay: "))

#Records user's worked hours as a float, Ex: 30.5
worked_hours = float(input("Hours worked in the week: "))

#Calculates user's exact pay for the last week
weekly_pay = hourly_pay*worked_hours

#Rounds user's pay down to two decimal points
output_weekly = round(weekly_pay, 2)


#Prints user's weekly pay
print("Total pay for the week: ","$",output_weekly)
