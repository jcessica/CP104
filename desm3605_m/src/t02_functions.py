"""
-------------------------------------------------------
Midterm B Task 2 Function Definitions
-------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-10-31"
-------------------------------------------------------
"""
GRAND = 70
MASTER = 85
PRO = 100


def categorize(strokes):
    """
    -------------------------------------------------------
    Determines the golf skill rating given number of strokes to complete 18 holes.
        If strokes are 70 or less, the rating is "Grandmaster".
        If strokes are 85 or less, the rating is "Master".
        If strokes are 100 or less, the rating is "Professional".
        If strokes are greater than 100, the rating is "Amateur".
        If points is less than 0, return "Error"
    Must use a fallthrough algorithm.
    Use: rating = categorize(strokes)
    -------------------------------------------------------
    Parameters:
        strokes - strokes to complete 18 holes of golf (int >= 0)
    Returns‌​‌​​​​‌​​‌‌​​‌‌‌‌‌‌‌​​​​‌​‌:
        category - description of skill rating (str)
    -------------------------------------------------------
    """

    # your code here
    category = 0
    
    if strokes > PRO:
        category = "Amateur"
    elif strokes <= PRO and strokes > MASTER:
        category = "Professional"
    elif strokes <= MASTER and strokes > GRAND:
        category = "Master"
    elif strokes <= GRAND and strokes >= 0:
        category = "Grandmaster"
    else:
        category = "Error"
    

    return category
