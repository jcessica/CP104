"""
-------------------------------------------------------
Midterm B Task 3 Function Definitions
-------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-10-29"
-------------------------------------------------------
"""
# Constants

# your constants here
FURNACE_TUNE = 125
EXTRA = 25
DISCOUNT = 10 


def servicing():
    """
    -------------------------------------------------------
    Determines the cost of getting a home furnace tune up. The cost is made up of:
        base cost: $125.00
        cost per extra service: $25.00
        VIP discount 10% only if:
            more than 1 extra service purchased
            and purchaser is a VIP
    The function must ask the user for these inputs.
    Use: cost = servicing()
    -------------------------------------------------------
    Returns‌​‌​​​​‌​​‌‌​​‌‌‌‌‌‌‌​​​​‌​‌:
        cost - cost of getting a home furnace tune up based upon the base cost,
            the number of extra services purchased, and VIP discount
            if applicable (float)
    -------------------------------------------------------
    """

    # your code here
    cost = 0
    
    furnace = float(input("How many extra services are you purchasing? "))
    ques1 = input("Are you a VIP member (Y/N)? ")
    if ques1 == "Y":
        cost = (FURNACE_TUNE + furnace * EXTRA) * (1 - (DISCOUNT/100))
    else: 
        cost = FURNACE_TUNE + (furnace * EXTRA)

    return cost
