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

# Rm multiplicity of test: add parametric test instead