"""
------------------------------------------------------------------------
Functions Module
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-11-16"
------------------------------------------------------------------------
"""

# Imports

# Constants

def list_factors(number):
    """
    -------------------------------------------------------
    description : Takes a number a returns its factor
    Use: list_factors(number)
    -------------------------------------------------------
    Parameters:
        number - (int > 0)
    Returns:
        factors - (int >0)
    ------------------------------------------------------
    """
    factors = []
    
    calc = 0
    track = 0
    #a.insert(position,value)
    
    for i in range(0,(number//2)+1):
        if number % (track+1) == 0:
            calc = track+1
            factors.insert(i,calc)
        track += 1
            
            
            
    return factors

def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: number_list = list_positives()
    -------------------------------------------------------
    Returns:
        number_list - A list of positive integers (list of int)
    ------------------------------------------------------
    """
    count = 0
    
    number_list = []
    
    number = int(input("Enter a positive number: "))
    
    while number != 0:
        if number > 0:
            number_list.insert(count,number)
        count +=1
        number = int(input("Enter a positive number: "))
        
    return number_list


def get_indexes(numbers, target_number):
    """
    -------------------------------------------------------
    Finds the indexes of target_number in numbers.
    Use: index_list = get_indexes(numbers, target_number)
    -------------------------------------------------------
    Parameters:
        numbers - list of values (list)
        target_number - value to look for in num_list (*)
    Returns:
        index_list - list of indexes of target_number (list of int)
    -------------------------------------------------------
    """
    
    index_list = []
    
    count = 0
    
    for i in range(0,len(numbers)):
        if numbers[i] == target_number:
            index_list.insert(i,count)
        count +=1
        
    return index_list
    
    
def list_subtract(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
    Use: list_subtract(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """
    
    target = subtrahend[0]
    
    modlist = []
    count = 0

    for i in range(0, len(minuend)):
        if minuend[i] != target:
            modlist.insert(count, minuend[i])
        count += 1
    
    minuend[:] = modlist

    return 

def verify_sorted(numbers):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = verify_sorted(numbers)
    -------------------------------------------------------
    Parameters:
        numbers - a list of numbers (list)
    Returns:
        in_order - True if numbers is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """
    
    in_order = True
    index = -1
    for i in range(0,len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            in_order = False
            index = -1
    
            
    return in_order,index



    
    


def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
        name - description (type)
    ------------------------------------------------------
    """