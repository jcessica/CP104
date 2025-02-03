"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-10-20"
------------------------------------------------------------------------
"""
# from math import sqrt
#Task 1 - Sqft to Acres
SQFT = 32560
ACRES_RATIO = 1/43560

#Task 5 - Falling distance
GRAVITY = 9.8
DIST_CONST = 2




def footage_to_acres(square_feet):
    """
    -------------------------------------------------------
    Converts square footage to acres.
    Use: acres = footage_to_acres(square_feet)
    -------------------------------------------------------
    Parameters:
        square_feet - area in square feet (float >= 0)
    Returns:
        acres - square_footage in acres (float)
    ------------------------------------------------------
    """
    acres = ACRES_RATIO * square_feet
    
    return acres

def lawn_mow_time(width, length, speed):
    """
    -------------------------------------------------------
    Determines how long it takes to mow a rectangular lawn.
    Use: time = lawn_mow_time(width, length, speed)
    -------------------------------------------------------
    Parameters:
        width - width of a lawn in metres (float > 0)
        length - length of a lawn in metres (float > 0)
        speed - square metres cut per minute (float > 0)
    Returns:
        time_minutes - time required to mow the lawn (float)
    ------------------------------------------------------
    """
    
    sq_meters = width * length
    
    time_minutes = sq_meters / speed

    return time_minutes

def extract_date(date_number):
    """
    -------------------------------------------------------
    Extracts the year, month, and day from a date number in the format YYYYMMDD.
    Use: year, month, day = extract_date(date_number)
    -------------------------------------------------------
    Parameters:
        date_number - a date number in the format YYYYMMDD (int)
    Returns:
        year - year portion of date_number (int)
        month - month portion of date_number (int)
        day - day portion of date_number (int)
    ------------------------------------------------------
    """
    
    day = date_number % 100 
    
    month = (date_number // 100) % 100
    
    year = date_number // 10000
    
    date = (year,month,day)
    
    return date

def multiply_fractions(num1, den1, num2, den2):
    """
    -------------------------------------------------------
    Calculates and returns fraction values.
    Use: num, den, product = multiply_fractions(num1, den1, num2, den2)
    -------------------------------------------------------
    Parameters:
        num1 - numerator of first fraction (int)
        den1 - denominator of first fraction (int != 0)
        num2 - numerator of second fraction (int)
        den2 - denominator of second fraction (int != 0)
    Returns:
        num - numerator of product (int)
        den - denominator of product (int)
        product - num / den (float)
    -------------------------------------------------------
    """
    
    frac1 = num1/den1
    
    frac2 = num2/den2
    
    fracprod = frac1 * frac2
    
    frac_prod_num = num1 * num2
    
    frac_prod_den = den1 * den2
    
    return (frac_prod_num, frac_prod_den, fracprod)

def falling_distance(falling_time):
    """
    -------------------------------------------------------
    Calculates distance an object has fallen due to gravity given
    the time it is fallen.
    Use: distance = falling_distance(falling_time)
    -------------------------------------------------------
    Parameters:
        falling_time - time object has fallen in seconds (int >= 0)
    Returns:
        distance - distance object has fallen in metres (float)
    -------------------------------------------------------
    """
    
    distance = ((falling_time**2)*GRAVITY)/DIST_CONST
    
    return distance

    
    
    




