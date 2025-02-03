"""
------------------------------------------------------------------------
Assignment 1, Task 5
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-09-25"
------------------------------------------------------------------------
"""
#Principal amount
p_principal_amt = float(input("Principal: $"))

#Annual rate of interest
interest = float(input("Interest (%): "))

#Annual rate of interest as a decimal
r_percent_int = interest/100

#Amount of money accumulated after t years
t_years = int(input("Number of years: "))

#Number of times the interest is compounded per year
n_compound = int(input("Number of times interest compounded per year: "))

#A = P(1+(r/n))^nt => compound interest calculation

calculation = (1+r_percent_int/n_compound)**(n_compound*t_years)

balance = p_principal_amt*calculation

print("Balance: $",balance)




