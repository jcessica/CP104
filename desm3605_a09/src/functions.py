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

# Constants

def file_top(file_handle, count): #Task 1
    """
    -------------------------------------------------------
    Prints first count lines of file_handle. Line numbering starts at 0.
    If length of file is shorter than count, stops printing after
    last line of file.
    Use: file_top(file_handle, count)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
        count - number of lines to print (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    
    lines = file_handle.readlines()
    length = len(lines)
    incr = 0

    
    if length < count:
        while length > 0:
            print(lines[incr].strip())
            length -= 1
            incr += 1       
    else: 
        while count > 0:
            print(lines[incr].strip())
            count -= 1
            incr += 1
    return
            
    
        
    
        
    
def read_integers(file_handle): #Task 2
    """
    -------------------------------------------------------
    Extracts positive integers from a file into a list of integers.
    Numbers are comma-delimited. Non-numeric tokens are ignored.
    Use: number_list = read_integers(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        number_list - a list of integers from file_handle (list of int)
    -------------------------------------------------------
    """
    
    number_list = []
    
    file_handle.seek(0)
    
    for line in file_handle.readlines():
        substring = line.strip().split(',')
        
        for sub in substring:
            if sub.isdigit() == True:
                number_list.append(int(sub))
    return number_list
        

def file_statistics(file_handle): #Task 3
    """
    -------------------------------------------------------
    Evaluates the contents of a file by counting upper-case letters,
    lower-case letters, digits, white-spaces (including end-of-line
    characters), and remaining characters.
    Use: ucount, lcount, dcount, wcount, rcount = file_statistics(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        ucount - The number of upper-case letters in the file (int)
        lcount - The number of lower-case letters in the file (int)
        dcount - The number of digits in the file (int)
        wcount - The number of white-space characters in the file (int)
        rcount - The number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    ucount = 0 
    lcount = 0
    dcount = 0
    wcount = 0
    rcount = 0
    
    for line in file_handle.readlines(): 
        for char in  line:
            if char.isupper() == True:
                ucount += 1
            elif char.islower() == True:
                lcount += 1 
            elif char.isdigit() == True:
                dcount += 1  
            elif char.isspace() == True:
                wcount += 1 
            else:
                rcount += 1             

    return ucount, lcount, dcount, wcount, rcount
    
def line_numbering(fh_read, fh_write): #Task 4
    """
    -------------------------------------------------------
    Adds line numbers to a file. Contents of fh_write contain contents
    of fh_read where every line has line numbers added to the beginning
    of the line in the format [number]. Line numbering starts at 0.
    Put a single space after the line number.
    Use: line_numbering(fh_read, fh_write)
    -------------------------------------------------------
    Parameters:
        fh_read - file to read (file - open for reading)
        fh_write - file to write (file - open for writing)
    Returns:
        None
    -------------------------------------------------------
    """
    fh_read.seek(0)
    
    lines = fh_read.readlines()
    for elem in lines:
        fh_write.write(f'[{lines.index(elem)}] {elem}')
        
    return
    
def student_stats(file_handle): #Task 5
    """
    -------------------------------------------------------
    Get information from a file of file_handle and grades.
    Use: l_id, h_id, avg = student_stats(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - student information file in the format
            surname,forename,id,mark (file - open for reading)
    Returns:
        l_id - the id of the student with the lowest mark (str)
        h_id - the id of the student with the highest mark (str)
        avg - the average mark (float)
    -------------------------------------------------------
    """
    grades = []
    gen = []
    iden = []
    
    filelist = file_handle.readlines()
    
    for line in filelist:
        gen= line.strip().split(',')
        grades.append(int(gen[-1]))
        iden.append(int(gen[-2]))
        
        l_id = str(iden[grades.index(min(grades))])
        
        h_id = str(iden[grades.index(max(grades))])
        
        avg = (float(min(grades))+float(max(grades)))/2
    
    return l_id,h_id,avg

    
        
            
        
        
        
        
    
        

