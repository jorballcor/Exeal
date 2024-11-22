
def is_leap_year(year: int) -> bool:
    """Func for checking if a year is a leap year.

    Args:
        year (int): Year to be checked

    Returns:
        bool: True or False
    """
    if (year % 100) == 0:
        return False
    if (year % 4) == 0:
        return True
    else:
        return False
    
