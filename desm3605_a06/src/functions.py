"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-11-10"
------------------------------------------------------------------------
"""

# Imports

# Constants
TEN = 10

YEARPERC = 12*100

def total_wins():
    """
    -------------------------------------------------------
    Total_wins is a function that asks the user to provide 
    a string sequence representing the results 
    of a game that is looped; it does not require any parameters.
    The end of the series should be indicated by the user by 
    entering an empty string (just press "Enter" or "return').
    Following the entry of every string, the function yields two 
    values that indicate the frequency with which the 
    strings "purple" and "gold" occurred in the input.
    Use: total_wins
    -------------------------------------------------------
    Returns:
        purple - Times the purple team won (int >= 0)
        golden - Times the golden team won (int >= 0)
    ------------------------------------------------------
    """
    
    user_input = str(input("Enter the winning team: "))
    
    purple = 0
    
    golden = 0
    
    while user_input != "":
        if user_input == "purple":
            purple += 1
        elif  user_input == "gold":
            golden += 1
        user_input = str(input("Enter the winning team: "))
                
    return (purple,golden)
            
        
        
    
    
def detect_prime(number):
    """
    -------------------------------------------------------
    Determines if number is a prime number.
    Use: prime = detect_prime(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int > 1)
    Returns:
        prime - True if number is prime, False otherwise (bool)
    ------------------------------------------------------
    """
    count = 1
    
    checker = 0
    
    prime = True
    

    while count < TEN:
        count += 1
        if number % count == 0 and count != number:
            checker = 1
        if checker > 1 or checker == 1:
            prime = False
            
    return prime
              
    
    
def interest_table(principal_amount, interest_rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal_amount, interest_rate, payment)
    -------------------------------------------------------
    Parameters:
        principal_amount - original value of a loan (float > 0)
        interest_rate - yearly interest interest_rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    
    intpay = principal_amount*(interest_rate/YEARPERC)
    
    balance = principal_amount-(payment-intpay)
    
    payleft = (principal_amount - (principal_amount % payment))/payment
    
    keeper = 0
    intkeep = 0
    month = 1
    
    
    
    
    print(f"Principal: ${principal_amount:.2f}")
    
    print(f"Interest Rate: {interest_rate:.2f}%")
    
    print(f"Monthly Payment: ${payment:.2f}")
    
    print("----------------------------------")
    print("Month Interest   Payment   Balance")
    print("----------------------------------")

    while payleft > 0:
        print(f"{month:>4d}{intpay:>10.2f}{payment:>10.2f}{balance:>10.2f}")
        intpay = balance*(interest_rate/YEARPERC)
        intkeep = intpay # Keeps intpay's last value
        keeper = balance # Keeps balance's last value
        balance = balance-(payment-intpay)
        payleft -= 1
        month += 1
    pay = keeper + intkeep
    balance = keeper-(pay-intkeep)
    print(f"{month:>4d}{intkeep:>10.2f}{pay:>10.2f}{balance:>10.2f}")

    
    
    return 

def count_of_digits(number):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: digits = count_of_digits(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int)
    Returns:
        digits - the number of digits in number (int)
    ------------------------------------------------------
    """
    digits = 1
    check = number // 10
    
    while check != 0:

        digits +=1
        number = number // 10
        check = number // 10
        
    return digits
    
    
def factor_summation(number):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = factor_summation(number)
    -------------------------------------------------------
    Parameters:
        number - a positive integer (int >= 1)
    Returns:
        total - the total of number's factors (int)
    ------------------------------------------------------
    """
    count = 0
    
    total = 0
    
    while count < number:
        count += 1
        if number % count == 0 and count != number:
            total += count
    return total
    