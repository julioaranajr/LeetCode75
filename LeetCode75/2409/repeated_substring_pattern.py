"""
Function to check if a string is a repeated substring pattern
"""


def repeated_substring_pattern(s: str) -> bool:
    """
    Function to check if a string is a repeated substring pattern

    Parameters:
    - s: str - The string

    Returns:
    - bool - True if the string is a repeated substring pattern, False otherwise
    """
    # The string is a repeated substring pattern if it can be formed by repeating a substring
    return (s + s).index(s, 1) < len(s)


# Time complexity: O(n)
# Space complexity: O(n)
# n = length of s

# Example:
print(repeated_substring_pattern("abab"))  # True
print(repeated_substring_pattern("aba"))  # False
