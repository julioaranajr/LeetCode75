"""
Function to get the square of a number.
"""


def square(x):
    """
    Function to get the square of a number.
    """
    if not isinstance(x, (int, float)):
        raise TypeError(f'Error: "{x}" must be numeric, not {type(x)}')
    return x**2


# Time complexity: O(1)
# Space complexity: O(1)

# Test the function
print(square(5))  # Output: 25
print(square(0))  # Output: 0
print(square(-4))  # Output: 16
try:
    print(square("a"))
except TypeError as e:
    print(e)
