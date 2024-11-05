"""
Add Digits
Given a non-negative integer num, repeatedly add all its digits
until the result has only one digit.
"""


def add_digits(num):
    """
    Adds the digits of the given number until the result is a single digit.
    """

    while num >= 10:
        num = sum(int(digit) for digit in str(num))

    return num


# Time complexity: O(log(n))
# Space complexity: O(1)

# Test the function
print(add_digits(38))  # Output: 2
print(add_digits(0))  # Output: 0
print(add_digits(9))  # Output: 9
