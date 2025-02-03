"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-11-02"
------------------------------------------------------------------------
"""

# Imports

# Constants

def calc_factorial(number):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of number.
    Use: product = calc_factorial(number)
    -------------------------------------------------------
    Parameters:
        number - number to factorial (int > 0)
    Returns:
        product - number! (int)
    ------------------------------------------------------
    """
    fact = 0
    product = 1
    for _ in range(1,number+1):
        fact += 1
        product *= fact
    return product

def calories_treadmill(per_min, minutes):
    """
    -------------------------------------------------------
    Prints a table of the number of calories
    burned every five minutes given the number of calories 
    burned per minute (per_min) an the total number of minutes
    run (minutes). 
    Use: run = calories_treadmill(per_min, minutes)
    -------------------------------------------------------
    Parameters:
        per_min - calories burned per min (float => 0)
        minutes - total number of minutes run (int => 0)
    Returns:
    ------------------------------------------------------
    """
    increment = 0
    
    for i in range (5,minutes + 1,5):
        increment = i
        calories = per_min * increment
        print(f"{i:<2d}{calories:>5.1f}")
          
  
    return 

def arrow_up(rows):
    """
    -------------------------------------------------------
    Takes an integer parameter and prints a arrow
    of # characters pointing up.
    Use: arrow_up(rows)
    -------------------------------------------------------
    Parameters:
        rows - description (int > 0)
    Returns:
        None 
    ------------------------------------------------------
    """
    char = "#"      
    count = 1
      
    space = (" " * count)
  
    down = rows-1
    
    blank = " " * down
    
    print(f"{blank:s}#")
        
    for _ in range(1,rows):
        down -= 1
        blank = " " * down
        space = (" " * count)
        print(f"{blank:s}{char:s}{space}{char:s}")
        count += 2
    return 




def range_addition(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum values from start by increment.
    Use: total = range_addition(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """
    total = 0
    
    values = increment * count
    for i in range(start,values,increment):
        total += i
        
    return total
        
def multiplication_table(start_num, stop_num):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start_num to stop_num.
    Use: multiplication_table(start_num, stop_num)
    -------------------------------------------------------
    Parameters:
        start_num - the range start value (int)
        stop_num - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """
    
    space = " "
    
    # space2 = " " * 6
    
    print(f'{space:>6s}',end="")
    
    for i in range(start_num, stop_num + 1):
        
        print(f"{i:>4}", end="")
        
    difference = stop_num - start_num + 1
    
    space2 = "-"

    printer = "\n" + space2 * 7 + space2 * (6 * difference)
    
    print(printer)

    for i in range(start_num, stop_num + 1):
        print(f"{i:4} |", end="")
        for j in range(start_num, stop_num + 1):
            result = i * j
            print(f"{result:4}", end="")
        print("")
        
    return
    
    

