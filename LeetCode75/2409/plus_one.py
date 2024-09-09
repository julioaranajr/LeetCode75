"""
Funtion to add one to the number represented by the digits array.
"""

def plus_one(digits: list[int]) -> list[int]:
    """
    Function to add one to the number represented by the digits array.

    Parameters:
    - digits: List[int] - An array of integers representing a number

    Returns:
    - List[int] - An array of integers representing the number after adding one
    """
    n = len(digits)
    for i in range(n - 1, -1, -1):
        digits[i] += 1
        digits[i] %= 10
        if digits[i] != 0:
            return digits
    return [1] + digits

# Time complexity: O(n)
# Space complexity: O(1)
# n = length of digits
