"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-10-25"
------------------------------------------------------------------------
"""

# Imports

# Constants

def draw_rectangle(height, width, char):
    """
    -------------------------------------------------------
    Prints a rectangle of height and width characters using
    the char character.
    Use: draw_rectangle(height, width, char)
    -------------------------------------------------------
    Parameters:
        height - number of characters high (int > 0)
        width - number of characters wide (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """

    for _ in range(height):
        print(char*width)
    return

#Task8
def draw_hollow_triangle(width, char):
    """
    -------------------------------------------------------
    Prints a hollow triangle of width characters using
    the char character.
    Use: draw_hollow_triangle(width, char)
    -------------------------------------------------------
    Parameters:
        width - number of characters wide (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    char_num = char * width
    
    print(f"{char}")
        
    i = 0
    space = " " * i
    
    if width == 2:
        print(f"{char}{space}{char}")
        
    
    for i in range(0,width-2):
        
        space = " " * i
        print(f"{char}{space}{char}")
        if i == (width-3):
            print(f"{char_num}")
            
    return
   
   

#Task 10
def treadmill(burnt_per_minute, start, end, inc):
    """
    -------------------------------------------------------
    Calculates and prints calories burnt on a treadmill over
    a given time range.
    Use: treadmill(burnt_per_minute, start, end, inc)
    -------------------------------------------------------
    Parameters:
        burnt_per_minute - calories burnt per minute (float > 0)
        start - start time in minutes (int > 0)
        end - end time in minutes (int >= start)
        inc - increment in minutes (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    minutes = start
    
    calories = burnt_per_minute * minutes
    
    if start == end:
        print(f"Calories burned after {minutes:d} minutes: {calories:.1f}")
    
    
    for _ in range(1,end,inc):
        calories = burnt_per_minute * minutes
        print(f"Calories burned after {minutes:d} minutes: {calories:.1f}")
        minutes += inc
    return


#Task 11`
def retirement(age, salary, increase):
    """
    -------------------------------------------------------
    Calculates a prints a table of how much a worker earns
    between age and retirement at 65.
    Use: retirement(age, salary, increase)
    -------------------------------------------------------
    Parameters:
        age - worker's current age (int > 0)
        salary - worker's current salary (float > 0)
        increase - percent increase in salary per year (float >= 0)
    Returns:
        None
    ------------------------------------------------------
    """
    print("Age         Salary")
    print("------------------")
    
    if age == 65:
        print(f"{age:2d}{salary:>16,.2f}")
    
    for _ in range(0,66-age):
        print(f"{age:2d}{salary:>16,.2f}")
        age += 1
        salary += salary*(increase/100)   
        
    return

#Task 15
def statistics(n):
    """
    -------------------------------------------------------
    Asks a user to enter n values, then calculates and returns
    the minimum, maximum, total, and average of those values.
    Use: minimum, maximum, total, average = statistics(n)
    -------------------------------------------------------
    Parameters:
        n - number of values to process (int > 0)
    Returns:
        minimum - smallest of n values (float)
        maximum - largest of n values (float)
        total - total of n values (float)
        average - average of n values (float)
    ------------------------------------------------------
    """
    
    value = float(input("First value: "))
    
    total = value
    
    minimum = value
    
    maximum = value
    
    for _ in range(1, n):
        compare = float(input("Next value: "))
        total += compare
        if compare < minimum: 
            minimum = compare
        if compare > maximum:
            maximum = compare
            
    average = total / n
    
    return (minimum, maximum, total, average)

            
            
        
    

