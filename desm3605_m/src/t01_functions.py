"""
-------------------------------------------------------
Midterm B Task 1 Function Definitions
-------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-10-29"
-------------------------------------------------------
"""
# Constants

# your constants here
DIME = 10
NICKEL = 5
QUARTERS = 25
LOONIES = 100




def minimal_change(cents):
    """
    -------------------------------------------------------
    Breaks down cents into a minimal number of coins.
    The change can be:
        loonies - coins worth 100 cents
        quarters - coins worth 25 cents
        dimes - coins worth 10 cents
        nickels - coins worth 5 cents
    Use: loonies, quarters, dimes, nickels = minimal_change(cents)
    -------------------------------------------------------
    Parameters:
        cents - number of cents (int >= 0)
    Returns‌​‌​​​​‌​​‌‌​​‌‌‌‌‌‌‌​​​​‌​‌:
        loonies - number of loonies ($1 coins) (int)
        quarters - number of quarters (25 cent coins) (int)
        dimes - number of dimes (10 cent coins) (int)
        nickels - number of nickels (5 cent coins) (int)
    -------------------------------------------------------
    """

    # your code here
    loonies_ = cents // LOONIES
    
    loon_remain = cents - (loonies_ * LOONIES)
    
    quarters_ = loon_remain // QUARTERS 
    
    quarter_remain = loon_remain - (quarters_*QUARTERS)
    
    dimes_ = quarter_remain // DIME
    
    dimes_remain = quarter_remain - (dimes_* DIME)
    
    nickel_ = (dimes_remain - (dimes_remain % 5)) // NICKEL

    return (loonies_,quarters_,dimes_,nickel_)
