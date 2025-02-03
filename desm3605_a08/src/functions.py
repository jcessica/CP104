"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-11-24"
------------------------------------------------------------------------
"""
# Imports

# Constants

def add_spaces(sentence):
    """
    -------------------------------------------------------
    Create a new sentence with added space between words. Words start
    with upper-case characters.
    Use: spaced = add_spaces(sentence)
    -------------------------------------------------------
    Parameters:
        sentence - sentence that represents a sentence in which all the
            words are run together (no spaces), but the first character
            of each word is uppercase. sentence has at least one
            character (str)
    Returns:
        spaced - new sentence in which the words are separated
            by spaces and only the first word starts with
            an uppercase character (str)
    -------------------------------------------------------
    """
    
    letter = ""
    word = ""
    
    space = sentence[0:1]
    for word in sentence[1:len(sentence)]:
        letter = word
        if letter.isalnum() == True:
            if letter != letter.upper():
                letter = letter.lower()
            elif letter == letter.upper():
                letter = " " + letter.lower()
        else:
                letter = letter.strip()
        space += letter
        
    return space
            
            
    

def pluralize(string):
    """
    -------------------------------------------------------
    Pluralizes a string according to the rules:
        - if string ends with 's', 'sh', or 'ch', add 'es'
        - if string ends with 'y' but not 'ay' or 'oy', replace
            the 'y' with 'ies'
        - otherwise add 's'
    Use: pluralized = pluralize(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        pluralized - a pluralized_string version of string (str)
    -------------------------------------------------------
    """
    if string.endswith('s') or string.endswith('sh') or string.endswith('ch'):
        pluralized = string + 'es'
    elif string.endswith('y') and not string.endswith('oy') and not string.endswith('ay'):
        pluralized = string.replace(string[-1],'ies')
    else:
        pluralized = string + 's'
    
    return pluralized
    
    
    
    
def common_end(str1, str2):
    """
    -------------------------------------------------------
    Returns the longest common ending of two strings.
    Use: suffix = common_end(str1, str2)
    -------------------------------------------------------
    Parameters:
        str1 - first string for ending comparison (str)
        str2 - second string for ending comparison (str)
    Returns:
        suffix - the longest common ending of str1 and str2 (str)
    -------------------------------------------------------
    """ 
    string1 = str1[::-1]
    string2 = str2[::-1]
    length = len(string1)
    suffix = ""
    substring = ""
    i = 0
    if string1[0] == string2[0]:
    
        while i <= length:
            if string1[0:i] == string2[0:i]:
                substring = string1[0:i]
                suffix = substring[::-1]
            i += 1
    
    return suffix



def valid_isbn(isbn):
    """
    -------------------------------------------------------
    Determines if an ISBN string is valid. An ISBN string is valid if:
        - it consists of only digits and dashes ('-')
        - it contains 5 groups of digits separated by dashes
        - its first group of digits is either '978' or '979'
        - its final group of digits is a single digit
        - its entire length is 17 characters
    Use: is_valid = valid_isbn(isbn)
    -------------------------------------------------------
    Parameters:
        isbn - a string (str)
    Returns:
        is_valid - True if isbn is valid, False otherwise (boolean)
    -------------------------------------------------------
    """
    is_valid =  False
    n = 4
    
    if len(isbn) == 17:
        if isbn[0:3] == '978' or isbn[0:3] == '979':
            if isbn.count('-') == 4 and isbn[isbn.find("-")]:
                if isbn.find("--") == -1:
                    while isbn[n:n+1].isdigit() == True or isbn[n:n+1] == "-" and (n+1) < len(isbn):
                        n += 1
                    if isbn[int(len(isbn)-2)] == "-" and isbn[len(isbn)-1:len(isbn)].isdigit() == True : 
                            is_valid = True
                        
    return is_valid
    
            
def has_word_chain(words):
    """
    -------------------------------------------------------
    Determines if a list of strings is a word chain. A word chain
    is a list of words in which the last character of a word in
    the list is the same as the first character of the next word
    in the list.
    Use: word_chain = has_word_chain(words)
    -------------------------------------------------------
    Parameters:
        words - a of strings (list of str, len > 1)
    Returns:
        word_chain - True if words is a word chain,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    word_chain = False
    first = words[0]
    second = words[1]
    rev_first = first[::-1]
    index = 1
    
    while rev_first[0:1] == second[0:1] and index < len(words) - 1:
        first = words[index]
        second = words[index + 1]
        rev_first = first[::-1]
        index += 1
    if index == len(words)-1 and rev_first[0:1] == second[0:1]:
        word_chain = True
            
    return word_chain

        
        


        

    
    

        
            
            
        
    
        
    
    
    
    
    
    
    