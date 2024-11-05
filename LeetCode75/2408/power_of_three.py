"""
Function to solve problem: Power of Three
"""


def is_power_of_three(n: int) -> bool:
    """
    Function to check if a number is a power of three.
    """
    if n <= 0:
        return False

    while n % 3 == 0:
        n //= 3

    return n == 1


# Test the function
print(is_power_of_three(27))  # Output: True
