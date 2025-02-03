"""
------------------------------------------------------------------------
Lab 2, Task 12
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-09-19"
------------------------------------------------------------------------
"""

# Imports

# Constants
MAX = 60
#Registers the number of seconds as an integer
seconds_input = int(input("Number of seconds: "))

#Finds out how many days find into "seconds_input",saves it as the closest whole number
days = round(seconds_input//86400)

#Keeps track of number of seconds left to calculate
days_remainder = (seconds_input/86400)-days

#Finds out how many hours fit into remaining seconds
hours = round((days_remainder*86400)//3600)

#Keeps track of number of seconds left to calculate
hours_remainder = (((days_remainder*86400)/3600)-hours)

#Finds out how many minutes fit into remaining seconds
minutes = round((hours_remainder*3600)//60)

#Keeps track of number of seconds left to calculate
minutes_remainder = ((hours_remainder*3600)/60)-minutes


seconds = round(minutes_remainder*60)

print("Days:",days,"Hours:",hours,"Minutes:",minutes,"Seconds:",seconds)










