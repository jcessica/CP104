"""
------------------------------------------------------------------------
Functions module
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-11-29"
------------------------------------------------------------------------
"""

# Imports

import random

# Constants

def generate_matrix_char(rows, cols):
    """
    -------------------------------------------------------
    Generates a 2D list of random lower case letter ('a' - 'z') values
    Use: matrix = generate_matrix_char(rows, cols)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the generated matrix (int > 0)
        cols - number of columns in the generated matrix (int > 0)
    Returns:
        matrix - a 2D list of random characters (2D list of str)
    -------------------------------------------------------
    """
    matrix = []

    for _ in range(rows):
        elem = []  # Create a new list for each row
        for _ in range(cols):
            alpha = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
            elem.append(alpha)
        matrix.append(elem)


        
    return matrix
    
def print_matrix_char(matrix):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list of strings in a formatted table.
    Prints row and column headings.
    Use: print_matrix_char(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of strings (2D list)
    Returns:
        None.
    -------------------------------------------------------
    """

    rows, cols = len(matrix), len(matrix[0])

    # Print column indices
    print(f'{"": >2}', end="\t")
    for j in range(cols):
        print(f'{j: >4}', end="")
    print()

    # Print matrix
    for i in range(rows):
        print(f'{i: >2}', end="\t")
        for j in range(cols):
            print(f'   {matrix[i][j]}', end="")
        print()
        
    return

    
def words_to_matrix(word_list):
    """
    -------------------------------------------------------
    Generates a 2D list of character values from the given
    list of words. All words must be the same length.
    Use: matrix = words_to_matrix(word_list)
    -------------------------------------------------------
    Parameters:
        word_list - a list containing the words to be placed in
            the matrix (list of string)
    Returns:
        matrix - a 2D list of characters of the given words
         in word_list (2D list of string).
    -------------------------------------------------------
    """
    

    matrix = []
    rows = []
    for i in word_list:
        for letter in i:
            rows.append(letter)
        matrix.append(rows)
        rows = []
    return matrix
        
        
def find_word_horizontal(matrix, word):
    """
    -------------------------------------------------------
    Look for word in each row of the given matrix of characters.
    Returns a list of indexes of all rows that are equal to word.
    Returns an empty list if no row is equal to word.
    Use: rows = find_word_horizontal(matrix, word)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix of characters (2D list of str)
        word - the word to search for (str)
    Returns:
        rows - a list of row indexes (list of int)
    ------------------------------------------------------
    """
    rows = []

    for row_index, row in enumerate(matrix):
        # Convert the row list to a string for comparison
        row_str = ''.join(row)
        
        if row_str == word:
            rows.append(row_index)

    return rows

        

        
    
    
    
    