from src.leap_year import is_leap_year
# from src import main.is_leap_year

def test_2008_is_leap_year_bc_is_divisible_by_4():
    year = 2008
    leap_year = is_leap_year(year)
    assert leap_year == True  # noqa: E712
    
    