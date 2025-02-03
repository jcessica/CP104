"""
------------------------------------------------------------------------
Lab 2, Task 6
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-09-19"
------------------------------------------------------------------------
"""

# Imports

# Constants

principal_amt_p = float(input("Enter the principal amount of your mortgage: "))

#Registers life of mortgage in years
life_mortgage = int(input("Enter the life of your mortgage (in years): "))

#Registers user's yearly mortgage interest rate
yearly_int = float(input("Enter your yearly interest rate: "))


#Number of monthly payments
monthly_int_i = yearly_int/100/12

#User's number of monthly payments over the course of mortgage
numb_monthly_pay_n = life_mortgage*12


numerator = monthly_int_i *(1+monthly_int_i) ** numb_monthly_pay_n

denominator = (1+monthly_int_i) ** numb_monthly_pay_n-1

#Calculates users monthly payment
monthly_pay_m = (numerator/denominator)*principal_amt_p


print("The monthly payments are: $",monthly_pay_m)







