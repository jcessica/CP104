"""
------------------------------------------------------------------------
Functions Module
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-11-23"
------------------------------------------------------------------------
"""

# Imports
# Constants

def customer_best(fh):
    """
    -------------------------------------------------------
    Find the customer with the largest balance.
    Assumes file is not empty.
    Use: result = customer_best(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        result - the record with the greatest balance (list)
    -------------------------------------------------------
    """
    highest = 0
    result = []
    line = fh.readline()
    
    while line !=  "":
        data = line.strip().split(",")
        if float(data[3])> highest:
            highest = float(data[3])
            result = data
        line = fh.readline()
    return result

def customer_append(fh, fields):
    """
    -------------------------------------------------------
    Appends a customer record to a comma-delimited sequential file.
    Use: customer_append(fh, fields)
    -------------------------------------------------------
    Parameters:
        fh - file to add to (file handle - already open for appending)
        fields - a list of the field data to append to the file (list)
    Returns:
       None
    -------------------------------------------------------
    """ 
    record = str(fields[0])
    for field in fields[1:]:
        record += ',' + str(field)
    

    
    fh.write(record)

    return 
    
def append_increment(fh):
    """
    -------------------------------------------------------
    Appends a number to the end of the fh. The number appended
    is the last number in the file plus 1.
    Assumes file is not empty.
    Use: num = append_increment(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading/writing)
    Returns:
        num - the number appended to the file (int)
    ------------------------------------------------------
    """
    line = fh.readline().strip()
    num = int(line)
    
    while line != "":
        num = int(line)
        line = fh.readline().strip()
    num += 1
        
    append = '\n' + str(num)
    
    fh.write(append)
    
    return num

def find_shortest(fh):
    """
    -------------------------------------------------------
    Finds the first word with shortest length in fh.
    Assumes file is not empty.
    Use: word = find_shortest(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        word - the first word with the shortest length in fh (str)
    ------------------------------------------------------
    """
    
    lines = fh.readlines()
    word = lines[0].strip()
    longer_word = lines[0].strip()
    
    for i in range(1,len(lines)):
        longer_word = lines[i].strip()
        if len(longer_word) < len(word):
            word = longer_word
            
    return word

def file_copy_n(fh_1, fh_2, n):
    """
    -------------------------------------------------------
    Copies n record from fh_1 (starting from the beginning of the file) to fh2
    Use: file_copy_n(fh_1, fh_2, n)
    -------------------------------------------------------
    Parameters:
        fh_1 - file to search (file handle - already open for reading)
        fh_2 - file to search (file handle - already open for appending)
        n - number of lines to copy from fh_1 to fh_2
    Returns:
        None
    ------------------------------------------------------
    """
    
    reading = [fh_1.readline() for _ in range(n)]
    
    fh_2.writelines(reading)
    
    return
    
        
        





        
        
   

    
    

