"""
------------------------------------------------------------------------
Functions
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-10-01"
------------------------------------------------------------------------
"""

# Import

import math

# Constants

def circumference(radius):
    
    """
    -------------------------------------------------------
    Calculates and returns circumference of a circle.
    Use: circ = circumference(radius)
    -------------------------------------------------------
    Parameters:
        radius - radius of a circle (float >= 0)
    Returns:
        circ - circumference of a circle (float)
    ------------------------------------------------------
    """
    
    circ = float(2 * math.pi * radius)
    
    return circ




def right_triangle(adjacent,opposite):
    """
    -------------------------------------------------------
    Calculates and returns the hypotenuse, perimeter, and
    area of a right triangle given two non-hypotenuse sides.
    Use: hyp, per, area = right_triangle(adjacent, opposite)
    -------------------------------------------------------
    Parameters:
        adjacent - length of side right triangle (float > 0)
        opposite - length of side right triangle (float > 0)
    Returns:
        hyp - hypotenuse of the triangle (float)
        per - perimeter of the triangle (float)
        area - area of the triangle (float)
    ------------------------------------------------------
    """
    hyp = float(math.sqrt(adjacent**2 + opposite**2))
    
    per = float(hyp + adjacent + opposite)
    
    area = float((adjacent * opposite)/2)
    
    return hyp,per,area

def computer_costs(computer_cost, computers_bought, commission_percent):
    """
    -------------------------------------------------------
    Calculates purchase costs of computers
    Use: pre_commission_cost, total_cost = computer_costs(computer_cost,
        computers_bought, commission_percent)
    -------------------------------------------------------
    Parameters:
        computer_cost - per unit cost (float >= 0)
        computers_bought - units bought (int >= 0)
        commission_percent - wholesaler commission (float >= 0)
    Returns:
        pre_commission_cost - cost before commission (float)
        total_cost - cost after commission (float)
    -------------------------------------------------------
    """
    
    pre_commission_cost = computers_bought * computer_cost
    
    total_cost = round(pre_commission_cost * (1+(commission_percent/100)),2)
    
    return (pre_commission_cost,total_cost)

def fraction_product(num1, den1, num2, den2):
    """
    -------------------------------------------------------
    Calculates and returns fraction values.
    Use: num, den, product = fraction_product(num1, den1, num2, den2)
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
    num = int((num1/den1) * (num2/den2) * (den1 * den2))
    
    den = int(((num1/den1) * (num2/den2) * (1/(num1 * num2)))**-1)
    
    product = float(num/den)
    
    return (num,den,product)
    
def time_split(initial_seconds):
    """
    -------------------------------------------------------
    Converts total seconds into days, hours, minutes, and seconds.
    Use: days, hours, minutes, seconds = time_split(initial_seconds)
    -------------------------------------------------------
    Parameters:
        initial_seconds - time elapsed (int >= 0)
    Returns:
        days - number of days in initial_seconds (int)
        hours - remaining hours in initial_seconds (int)
        minutes - remaining minutes in initial_seconds (int)
        seconds - remaining seconds in initial_seconds (int)
    -------------------------------------------------------
    """
    DAYS_DIV = 86400
    
    HOURS_DIV = 3600
    
    MINS_DIV = 60
    
    days_remainder = initial_seconds % DAYS_DIV
    
    days = int((initial_seconds - days_remainder)/DAYS_DIV)
    
    hours_remainder = days_remainder % HOURS_DIV
    
    hours = int((days_remainder - hours_remainder)/HOURS_DIV)
    
    seconds = int(hours_remainder % MINS_DIV)
    
    minutes = int((hours_remainder - seconds)//MINS_DIV)
    
    return(days,hours,minutes,seconds)
        
    