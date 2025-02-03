"""
------------------------------------------------------------------------
Functions module
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-11-14"
------------------------------------------------------------------------
"""

# Imports

# Constants
STRONG = 8


def password_strength(password):
    """
    -------------------------------------------------------
    Checks the strength of a given password. A password is
    strong if it contains at least eight characters, has a
    combination of upper-case and lower-case letters, and
    includes digits. Prints one or more of:
        not long enough - if password less than 8 characters
        no digits - if password has no digits
        no upper case - if password has no upper case letters
        no lower case - if password has no lower case letters
    Use: password_strength(password)
    -------------------------------------------------------
    Parameters:
        password - the password to be checked (str)
    Returns:
        None
    ------------------------------------------------------
    """
    length = len(password)
    upper = 0
    lower = 0
    digit = 0
    
    if len(password) < STRONG:
        print("not long enough") 
        
    for c in range(length):
        if password[c].isdigit() == True:
            digit +=1   
        if password[c].isupper() == True:
            upper +=1
        if password[c].islower() == True:
            lower +=1  
    
    if digit == 0:
        print("no digits")
    if upper == 0:
        print("no upper case")      
    if lower == 0:
        print("no lower case")
        
    return
        
        
def vowel_count(s):
    """
    -------------------------------------------------------
    Counts the number of vowels in a string. Does not include 'y'.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        count - the number of vowels in s (int)
    -------------------------------------------------------
    """
        
    vowels = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']

    count = 0
    
    length = len(vowels)
    
    for i in range(0,length):
        count += s.count(vowels[i])
        
    return count
        
    
def count_special_chars(s):
    """
    -------------------------------------------------------
    Counts the number of special characters in s.
    The special characters are: "#", "@", "$", "%", "&", "!".
    Use: count = count_special_chars(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        count - number of special characters in s (int)
    ------------------------------------------------------
    """
    
    special  = ['#','@','$','%','&','!']
    
    count = 0
    
    length = len(special)
    
    for i in range(0,length):
        count += s.count(special[i])
        
    return count

def comma_period_replace(string):
    """
    -------------------------------------------------------
    Replaces all the commas with a period in s.
    Use: out = comma_period_replace(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        out - string with all commas replaced by a period (str)
    ------------------------------------------------------
    """
    
    period = '.'
    
    comma = ','
    
    out = string.replace(comma,period)
    
    return out

def total_digits(string):
    """
    -------------------------------------------------------
    Extracts and calculates the total of all digits in string.
    Use: total = total_digits(string)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        total - total of all the digits in string (int)
    ------------------------------------------------------
    """
    total = 0
    
    for c in range(0,len(string)):
    
        if string[c].isdigit() == True:
            total += int(string[c])   
            
    return total
    
    

        
        
            
    
        
    
    
    