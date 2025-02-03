"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-10-12"
------------------------------------------------------------------------
"""


# Imports

# Constants

#def gym_cost
DIS1 = 0.05
DIS2= 0.10
DIS3 = 0.15

#def get_pay
RAISE = 1.5
TAX_RATE = 3.625   
OVERTIME = 40
    
#def_pay_raise
PAY5 = 0.05 #Raise applied to calculation    
PAY15 = 0.015  
PAY3 = 0.03    
PAY1 = 0.01   
PAY2 = 0.02

YEARS10 = 10
YEARS4 = 4

#def fast_food
BURGER = 6.00
WINGS = 8.00
FRIES = 1.50
SALAD = 2.00


def gym_cost(cost, friends):
    """
    -------------------------------------------------------
    Calculates total cost of a gym membership. A member gets a
    discount according to the number of friends they sign up.
        0 friends: 0% discount
        1 friend: 5% discount
        2 friends: 10% discount
        3 or more friends: 15% discount
    Use: final_cost = gym_cost(cost, friends)
    -------------------------------------------------------
    Parameters:
        cost - a gym membership base cost (float > 0)
        friends - number of friends signed up (int >= 0)
    Returns:
        final_cost - cost of membership after discount (float)
    ------------------------------------------------------
    """
        
    if friends == 1:
        final_cost = cost - (cost * DIS1)
        
    elif friends == 2:
        final_cost = cost - (cost * DIS2)
    elif friends >= 3:
        final_cost = cost - (cost * DIS3)
    else: 
        final_cost = cost
    
    return final_cost
    

def is_leap(year):
    """
    -------------------------------------------------------
    Determines if a year is a leap year. Every year that is
    exactly divisible by four is a leap year, except for years
    that are exactly divisible by 100, but these centurial years
    are leap years if they are exactly divisible by 400. For
    example, the years 1700, 1800, and 1900 are not leap years,
    but the years 1600 and 2000 are.
    Use: result = is_leap(year)
    -------------------------------------------------------
    Parameters:
        year - a year (int > 0)
    Returns:
        result - True if year is a leap year,
            False otherwise (boolean)
    ------------------------------------------------------
    """
    result = True
    
    if year % 4 == 0:#Leap year
    
        if year % 400 == 0:#Centurial leap year
            result = True 
            
        elif year % 100 == 0:#Centurial year
            result = False
            
    else: 
        result = False
    
    return result
    


def get_pay(hourly_rate, hours_worked):
    """
    -------------------------------------------------------
    Calculates an employee's net wage given hours and pay.
    Each employee is paid 1.5 times their regular hourly rate for
    all hours over 40. A tax amount of 3.625 percent of gross salary
    is deducted.
    Use: net_payment = get_pay(hourly_rate, hours_worked)
    -------------------------------------------------------
    Parameters:
        hourly_rate - hourly rate of pay (float)
        hours_worked - total hours worked (float)
    Returns:
        net_payment - description (float)
    ------------------------------------------------------
    """ 
    hours_raise = 0
    
    hours = 0
    
    if hours_worked > OVERTIME:
    
        hours_raise = ((hours_worked % OVERTIME) * RAISE) - (hours_worked % OVERTIME)
        
        hours = (hours_worked + hours_raise) * hourly_rate
        
        net_payment = hours - (hours * TAX_RATE/100)
        
    else:
        
        net_payment = (hours_worked * hourly_rate) - ((TAX_RATE/100) * hours_worked * hourly_rate)
        
    return net_payment
        

def pay_raise(status, years, salary):
    """
    -------------------------------------------------------
    Calculates pay raises for employees. Pay raises are based on:
    status: Full Time ('F)' or Part Time ('P')
    and years of service
    Raises are:
        5% for full time greater than or equal to 10 years service
        1.5% for full time less than 4 years service
        3% for part time greater than 10 years service
        1% for part time less than 4 years service
        2% for all others
    Use: new_salary = pay_raise(status, years, salary)
    -------------------------------------------------------
    Parameters:
        status - employment type (str - 'F' or 'P')
        years - number of years employed (int > 0)
        salary - current salary (float > 0)
    Returns:
        new_salary - employee's new salary (float).
    -------------------------------------------------------
    """
    
    new_salary = 0 # Salary Calculation
    
    if status == 'F':
            
        if years >= YEARS10:
            
            new_salary = salary + (salary * PAY5)
            
        elif years < YEARS4:
            
            new_salary = salary + (salary * PAY15)
            
        else: new_salary = salary + (salary * PAY2)
            
    elif status == 'P':
            
        if years > YEARS10:
            
            new_salary = salary + (salary * PAY3)
            
        elif years < YEARS4:
                
            new_salary = salary + (salary * PAY1)
                
    else: 
            new_salary = salary + (salary * PAY2)
            
    return new_salary#Rounding to two decimal places
                
               
def fast_food():
    """
    -------------------------------------------------------
    Food order function.
    Asks user for their order and if they want a combo, and if
    necessary, what is the side order for the combo:
    Prices:
        Burger: $6.00
        Wings: $8.00
        Fries combo: add $1.50
        Salad combo: add $2.00
    Use: price = fast_food()
    -------------------------------------------------------
    Returns:
        price - the price of one meal (float)
    -------------------------------------------------------
    """
    
    order = input("Order B - burger or W - wings: ")
    
    if order == 'B':
        order = BURGER
    else:
        order = WINGS
    
    
    combo = input("Make it a combo? (Y/N): ") 
    
    price = 0
            
    if combo == "Y":
        
            side = input("Add F - fries or S - salad: ")
            
            if side == "F":
                side = FRIES
                
                price = order + FRIES
            
            else:
                side = SALAD
                price = order + SALAD
            
        
    else:
        price = order
    
    return price
         
    

                
            
     
            
            
            
        
        
    

    
    

    
        

 
        


    
    
    
    
    
    
    
        
    
    
    
    