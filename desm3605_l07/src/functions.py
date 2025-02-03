"""
------------------------------------------------------------------------
Functions module
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-11-01"
------------------------------------------------------------------------
"""

# Imports
from random import randint

# Constants
STOP = -999

def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """
    count = 1
    
    number = randint(1, high)
    
    guess = int(input("Guess: "))
    
    while guess != number:
        if guess < number: 
            count += 1
            print("Too low, try again.")
            guess = int(input("Guess: "))   
        elif guess > number:
            count += 1
            print("Too high, try again.")
            guess = int(input("Guess: "))
            
    print(f"Congratulations - good guess!\nYou made {count} guesses.")
             
    return count
    
def sum_squares(target):
    """
    -------------------------------------------------------
    Determines the sum of squares closest to, and greater than or
    equal to, a target value.
    Use: final = sum_squares(target)
    -------------------------------------------------------
    Parameters:
        target - target value (int >= 0)
    Returns:
        final - the final sum of squares >= target (int)
    -------------------------------------------------------
    """
    final = 0
    i = 0
    while final <= target:
            i += 1
            final += i**2
        
        
    return final
        
        
def num_categories():
    """
    -------------------------------------------------------
    Asks a user to enter a series of numbers, then counts and returns
    how may positives, negatives, and zeroes there are.
    Stop processing values when the user enters -999.
    Use: negatives, zeroes, positives = num_categories()
    -------------------------------------------------------
    Returns:
        negatives - number of negative values (int)
        zeroes - number of zero values (int)
        positives - number of positive values (int)
    ------------------------------------------------------
    """
    
    negatives = 0
    
    zeroes = 0
    
    positives = 0
    
    number = float(input("First value: "))
    
    while number != STOP:      
        if number < 0:
            negatives += 1
        elif number > 0:
            positives += 1
        else: 
            zeroes += 1
        number = float(input("Next value: "))
    
    return (negatives,zeroes,positives)

def meal_costs():
    """
    -------------------------------------------------------
    Asks a user the costs of breakfast, lunch, and supper for each
    day the user was away. Assumes there is at least one day, and
    after entering data for each day asks the user whether they want
    to enter data for another day. Calculates total costs for meals.
    Use: b_total, l_total, s_total, a_total = meal_costs()
    -------------------------------------------------------
    Returns:
        b_total - total breakfasts cost (float)
        l_total - total lunches cost (float)
        s_total - total suppers cost (float)
        a_total - all meals cost (float)
    ------------------------------------------------------
    """
    count = 0
    b_total = 0
    l_total = 0
    s_total = 0
    a_total = 0
    sum_total = 0
    away = ""
    breakfast = 0
    lunch = 0
    supper = 0
    
    
    
    while away != "N":

        count +=1
        print(f"For Day {count}\n")
        breakfast = float(input("How much was breakfast? $"))
        b_total += breakfast
        lunch = float(input("How much was lunch? $"))
        l_total += lunch
        supper = float(input("How much was supper? $"))
        s_total += supper
        sum_total = breakfast + lunch + supper
        a_total += sum_total
        
        print(f"Your total for the day was ${sum_total:.2f}\n\n")
        
        away = input("Were you away another day (Y/N)? ")
        print()
        
    return (b_total,l_total,s_total,a_total)
        
        
def get_int(low, high):
    """
    -------------------------------------------------------
    Asks a user for an integer value between low and high, and
    continues asking until an acceptable value is input.
    Use: value = get_int(low, high)
    -------------------------------------------------------
    Parameters:
        low - the lowest acceptable integer (inclusive) (int)
        high - the higest acceptable integer (inclusive) (int > low)
    Returns:
        value - a number between low and high (int)
    ------------------------------------------------------
    """
    value = int(input(f"Enter a value between {low} and {high}: "))
    
    while value < high or value > low:
        if value < low:
            print("Value entered is too low")
            value = int(input(f"Enter a value between {low} and {high}: "))
        elif value > high:
            print("Value entered is too high")
            value = int(input(f"Enter a value between {low} and {high}: "))
        else: 
            return value
    
    
        
   
    
    
            
            
