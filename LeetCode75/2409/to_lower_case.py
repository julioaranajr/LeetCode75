"""
Function to convert a string to lowercase
"""


def to_lowercase(s: str) -> str:
    """
    Function to convert a string to lowercase

    Parameters:
    - s: str - The string

    Returns:
    - str - The lowercase string
    """
    return s.lower()


# Time complexity: O(n)
# Space complexity: O(1)
# n = length of s

# Example:
print(to_lowercase("Hello"))  # hello
print(to_lowercase("WORLD"))  # hello
