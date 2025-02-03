"""
------------------------------------------------------------------------
Functions Module
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-10-27"
------------------------------------------------------------------------
"""

# Imports
HAZARD = 300
V_UNHEALTHY = 201
UNHEALTHY = 151
SENSITIVE = 101
MODERATE = 51

# Constants

def day_name(day_num):
    """
    -------------------------------------------------------
    Returns the name of a day of the week given an integer day number.
    Day 1 is "Sunday", day 7 is "Saturday".
    Returns "Error" if the number is not valid.
    Use: day = day_name(day_num)
    -------------------------------------------------------
    Parameters:
        day_num - day number (1 <= int <= 7)
    Returns:
        day - name of a day of the week (str)
    ------------------------------------------------------
    """
    
    
    if type(day_num) == int:
        if day_num <= 7 or day_num >= 1:
            day = ""
            if day_num == 1:
                day = "Sunday"
            elif day_num == 2:
                day = "Monday"
            elif day_num == 3:
                day = "Tuesday"
            elif day_num ==4:
                day = "Wednesday"
            elif day_num == 5:
                day = "Thursday"
            elif day_num == 6:
                day = "Friday"
            else:
                day = "Saturday"
        else:
            day = "Error"
    else:
        day = "Error"
    return day
            
        
    
        
    
def pollution_ranking(air_quality_index):
    """
    -------------------------------------------------------
    Returns the pollution level given an AQI (Air Quality Index):
        "Good" - 0 to 50 AQI
        "Moderate" - 51 - 100 AQI
        "Unhealthy for Sensitive Groups" - 101 - 150 AQI
        "Unhealthy" - 151 - 200 AQI
        "Very Unhealthy" - 201 - 300 AQI
        "Hazardous" - 300+ AQI
    Returns "Error" if air_quality_index is negative.
    Use: pollution = pollution_ranking(air_quality_index)
    -------------------------------------------------------
    Parameters:
        air_quality_index - Air Quality Index (int)
    Returns:
        pollution - name of pollution level (str)
    ------------------------------------------------------
    """
    if type(air_quality_index) == int: 
        if air_quality_index >= 0:
            if air_quality_index >= HAZARD:
                pollution = "Hazardous"
            elif air_quality_index >= V_UNHEALTHY:
                pollution = "Very Unhealthy"
            elif air_quality_index >= UNHEALTHY:
                pollution = "Unhealthy"
            elif air_quality_index >= SENSITIVE:
                pollution = "Unhealthy for Sensitive Groups"
            elif air_quality_index >= MODERATE:
                pollution = "Moderate"
            else:
                pollution = "Good"
        else:
            pollution = "Error"
    else:
        pollution = "Error"
    return pollution    
    
    
def largest_average(val1, val2, val3):
    """
    -------------------------------------------------------
    Returns the average of the two largest values of
    val1, val2, and val3.
    Use: average = largest_average(val1, val2, val3)
    -------------------------------------------------------
    Parameters:
        val1 - a number (float)
        val2 - a number (float)
        val3 - a number (float)
    Returns:
        average - the average of the two largest values of
            val1, val2, and val3 (float)
    ------------------------------------------------------
    """
    two_large = 0
    
    one_large = 0
    
    if val1 >= val2:
        one_large = val1
    else:
        one_large = val2
    
    if val2 >= val3:
        two_large = val2
    else:
        two_large = val3
    
    average = (one_large + two_large) / 2
    
    return average
        
    
    
def colour_combine(rgb_colour1, rgb_colour2):
    """
    -------------------------------------------------------
    Determines the secondary rgb_colour from mixing two primary
    RGB (Red, Green, Blue) colours. The order of the colours
    is *not* significant.
    Returns "Error" if any of the rgb_colour parameter(s) are invalid.
        "red" + "blue": "fuchsia"
        "red" + "green": "yellow"
        "green" + "blue": "aqua"
        "red" + "red": "red"
        "blue" + "blue": "blue"
        "green" + "green": "green"
    Use: rgb_colour = colour_combine(rgb_colour1, rgb_colour2)
    -------------------------------------------------------
    Parameters:
        rgb_colour1 - a primary RGB rgb_colour (str)
        rgb_colour2 - a primary RGB rgb_colour (str)
    Returns:
        rgb_colour - a secondary RGB rgb_colour (str)
    -------------------------------------------------------
    """
    col1 = rgb_colour1
    col2 = rgb_colour2 
    
    rgb_colour = None
    
    if type(col1 and col2) == str: #Checking for valid input
        if col1 == "red" or col1 == "green" or col1 == "blue" and col2 == "red" or col2 == "green" or col2 == "blue":
            if col1 == "red" and col2 == "blue" or col1 == "blue" and col2 == "red": #Checking if colours make fuchsia
                rgb_colour = "fuchsia"
            elif col1 == "red" and col2 == "green" or col1 == "green" and col2 == "red": #Checking if colours make yellow 
                rgb_colour = "yellow" 
            elif col1 == "blue" and col2 == "green" or col1 == "green" and col2 == "blue": #Checking if colours make aqua
                rgb_colour = "aqua"
            elif col1 == "red" and col2 == "red": #Checking if colours make red
                rgb_colour = "red"  
            elif col1 == "blue" and col2 == "blue": #Checking if colours make blue
                rgb_colour = "blue"                 
            else:  #Checking if colours make green
                rgb_colour = "green"   
        else:
            rgb_colour = "Error"
    else: 
        rgb_colour = "Error"
        
    return rgb_colour
        
def hoo_rah(number):
    """
    -------------------------------------------------------
   Takes an integer parameter and returns one of the following strings
    "Hoo" if number is evenly divisible by 2
    "Rah" if number is evenly divisible by 7
    "Hoo Rah" if number is evenly divisible by both 2 and 7
    "Zip" if number is none of the above
    Use: hoo_rah = hoo_rah(number)
    -------------------------------------------------------
    Parameters:
        number - an integer parameter (int)
    Returns:
        string 
    -------------------------------------------------------
    """
    string = "Zip"
    if number % 14 == 0:
        string = "Hoo Rah"
    elif number % 2 == 0:
        string = "Hoo"
    elif number % 7 == 0:
        string = "Rah"
        
    return string
    
    
                

    

    
