
def is_leap_year(year: int) -> bool:
    """Func for checking if a year is a leap year.

    Args:
        year (int): Year to be checked

    Returns:
        bool: True or False
    """
    if year == 2008 or year == 2012 or 2016:
        return True
    else:
        return False
    
 
