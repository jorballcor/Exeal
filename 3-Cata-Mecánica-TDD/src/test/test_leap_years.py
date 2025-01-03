from src.leap_year import is_leap_year
import pytest

@pytest.mark.parametrize("year, expected", [
    (2008, True),
    (2012, True),
    (2016, True)
])
def test_years_divisible_by_4_are_leap_years(year, expected):
    """Parametric test for checking leap years."""
    leap_year = is_leap_year(year)
    assert leap_year == expected  # noqa: E712


@pytest.mark.parametrize("year, expected", [
    (1700, False),
    (1800, False),
    (1900, False),
])
def test_years_divisible_by_100_are_NOT_leap_years(year, expected):
    """Parametric test for checking leap years."""
    leap_year = is_leap_year(year)
    assert leap_year == expected  # noqa: E712


@pytest.mark.parametrize("year, expected", [
    (2000, True),
    (2400, True),
    (2800, True),
])
def test_years_divisible_by_400_are_leap_years(year, expected):
    """Parametric test for checking leap years."""
    leap_year = is_leap_year(year)
    assert leap_year == expected  # noqa: E712

@pytest.mark.parametrize("year, expected", [
    (2017, False),
    (2018, False),
    (2019, False),
])
def test_years_not_divisible_by_4_are_NOT_leap_years(year, expected):
    """Parametric test for checking leap years."""
    leap_year = is_leap_year(year)
    assert leap_year == expected  # noqa: E712

 #Now we write a parametric test from the beginning
 #as we now how the exercice goes