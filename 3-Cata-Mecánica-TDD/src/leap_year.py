
def is_leap_year(year: int) -> bool:
    """Func for checking if a year is a leap year.

    Args:
        year (int): Year to be checked

    Returns:
        bool: True or False
    """
    if (year % 4) == 0:
        return True
    else:
        return False
    
 #Once we got 3 particular cases -> General rule (line 11)
 #not before than 3 particular cases  
 
 #Then see if test pass
 #If test pass, you can commit changes
 
 #Refactor conducted from GREEN to GREEN
 #We didnt broke anything
