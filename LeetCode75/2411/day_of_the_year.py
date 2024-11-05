"""Method to return the day of the year."""

# l= leap year
# d= days in a month per year
def day_of_year(date: str) -> int:
    """A function to return the day of the year."""
    year, month, days = (int(s) for s in date.split("-"))
    l = 29 if year % 400 == 0 or (year % 4 == 0 and year % 100) else 28
    d = [31, l, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return sum(d[: month - 1]) + days
