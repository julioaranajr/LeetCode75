"""
Add Digits
Given a non-negative integer num, repeatedly add all its digits 
until the result has only one digit.
Example:
    Input: 38
    Output: 2
Returns:
    int: The single digit result.
    
The solution is to keep adding the digits of the number until the result 
is a single digit.
The sum of the digits of a number is always less than the number itself, 
so the result will be a single digit.

The time complexity is O(log(n)), where n is the input number.
"""


def addDigits(num):
    """
    Adds the digits of the given number until the result is a single digit.
    Args:
        num (int): The input number.
    Returns:
        int: The single digit result.
    Example:
        >>> addDigits(38)
        2
    """

    while num >= 10:
        num = sum(int(digit) for digit in str(num))

    return num

# Test the function
print(addDigits(38))  # Output: 2
print(addDigits(0))  # Output: 0
print(addDigits(11))  # Output: 2
print(addDigits(103))  # Output: 4