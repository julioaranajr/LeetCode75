"""
Function to convert a Roman numeral to an integer.
"""


def roman_to_int(s: str) -> int:
    """
    Function to convert a Roman numeral to an integer.

    Parameters:
    - s: str - The Roman numeral

    Returns:
    - int - The integer representation of the Roman numeral
    """
    d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    prev_value = 0

    for char in reversed(s):
        current_value = d[char]

        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value

        prev_value = current_value

    return total


# Time complexity: O(n)
# Space complexity: O(1)
# n = length of s

# Example:
print(roman_to_int("MMXXIV"))  # 2024
print(roman_to_int("CCII"))  # 202
print(roman_to_int("XX"))  # 20
print(roman_to_int("IV"))  # 4
