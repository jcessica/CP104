"""
------------------------------------------------------------------------
Functions module
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-11-08"
------------------------------------------------------------------------
"""

# Imports
from random import randint

# Constants
WEEK = ['None','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']


#Task1
def get_weekday_name(d):
    """
    -------------------------------------------------------
    Returns the name of a day of the week given its number.
    Use: name = get_weekday_name(d)
    -------------------------------------------------------
    Parameters:
        d - day of week number (1 <= int <= 7)
    Returns:
        name - matching day of the week, 1 = "Sunday", 7 = "Saturday" (str)
    -------------------------------------------------------
    """
    name = WEEK[d]
    
    return name

def generate_integer_list(n, low, high):
    """
    -------------------------------------------------------
    Generates a list of random integers.
    Requires import: from random import randint
    Use: values = generate_integer_list(n, low, high)
    -------------------------------------------------------
    Parameters:
        n - number of values to generate (int, > 0)
        low - low value range (int)
        high - high value range (int, > low)
    Returns:
        values - a list of random integers (list of int)
    -------------------------------------------------------
    """
    values =[]
    
    for _ in range(1,n+1):
        values.append(randint(low,high))
        
    return values
        
    
    
    
    
    
    
#Task6
def list_stats(values):
    """
    -------------------------------------------------------
    Returns statistics about values in a list.
    values has at least one element.
    Use: smallest, largest, total, average = list_stats(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of float)
    Returns:
        smallest - the smallest number in values (float)
        largest - the largest number in values (float)
        total - total of numbers in list (float)
        average - the average numbers in values (float)
    -------------------------------------------------------
    """
    
    largest = values[0]
    
    smallest = values[0]
    
    total = 0
    
    for i in values:
        total += i
        compare = i
        if compare < smallest: 
            smallest = compare
        if compare > largest:
            largest = compare
            

    average = total/len(values)
    
    return (smallest,largest,total,average)
    
    
#Task7
def list_categorize(values):
    """
    -------------------------------------------------------
    Returns data about the categories of values in a list.
    Use: negatives, positives, zeroes, evens, odds = list_categorize(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of int)
    Returns:
        negatives - the number of negative values (int)
        positives - the number of positive values (int)
        zeroes - the number of zeroes (int)
        evens - the number of even values (int)
        odds - the number of odd values (int)
    -------------------------------------------------------
    """
    negatives = 0 
    
    odds = 0
    
    evens = 0
    
    for i in values:
        if i < 0:
            negatives +=1
            
        zeroes = values.count(0)
        positives = len(values) - negatives - zeroes
            
        if i % 2 == 1:
            odds += 1
        else:
            evens += 1
            
    return (negatives,positives,zeroes,evens,odds)
            
        
    

#Task11
def dot_product(source1, source2):
    """
    -------------------------------------------------------
    Calculates a dot product of two lists. Lists must be the
    same length.
    Use: product = dot_product(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - list of numbers (list of float)
        source2 - list of numbers (list of float)
    Returns:
        product - source1 • source2 (float)
    -------------------------------------------------------
    """
    product = 0 
    
    if len(source1) == len(source2):
        
        for i in range(0,len(source1)):
            product += source1[i] * source2[i]
    
    return product


#Task15
def symmetric_difference(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the symmetric difference of the contents
    of source1 and source2.
    Only elements that appear in one of source1 and source2, but not both,
    appear once and only once in target.
    Use: target = symmetric_difference(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of *)
        source2 - a list (list of *)
    Returns:
        target - the symmetric difference of source1 and source2 (list of *)
    -------------------------------------------------------
    """
    target = source1 + source2
    copy = target[:]
        
    for i in copy:
        repeat = i
        count = target.count(repeat)
            
        if count > 1:
            for _ in range(0,count):
                target.remove(repeat) 

    return target
                
                
        
        
    
    
    
    
    
    
    
    
    
    
    