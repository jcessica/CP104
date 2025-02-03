"""
------------------------------------------------------------------------
Lab 2, Task 2
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-09-19"
------------------------------------------------------------------------
"""

# Imports

# Constants

#Freezing point of water
WATER_FREEZE = 32 

#Fahrenheit and Celsius ratio
FAHREN_CELSIUS = 5/9 

#Fahrenheit value request
fahrenheit_input = int(input("Temperature (F): "))

#Fahrenheit conversion to Celsius
celsius_output = int((fahrenheit_input-WATER_FREEZE)*FAHREN_CELSIUS)

print("Temperature (C):",celsius_output)





