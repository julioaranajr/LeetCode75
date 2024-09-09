"""
Function to find the greatest common divisor of two strings
"""
from math import gcd


def gcd_of_strings(str1: str, str2: str) -> str:
    """
    Function to find the greatest common divisor of two strings
    """
    if str1 + str2 != str2 + str1:
        return 'None'
    n = gcd(len(str1), len(str2))
    return str1[:n]

# Time complexity: O(n)
# Space complexity: O(1)
# n = len(str1) + len(str2)

# Test the function
TEST_STR1 = "ABCABCDEF"
TEST_STR2 = "ABC"
print(f'The 1st string is: {TEST_STR1}')
print(f'The 2nd string is: {TEST_STR2}')
print(f'The greatest common divisor is: {gcd_of_strings(TEST_STR1, TEST_STR2)}')  # Output: "ABC"

TEST_STR1 = "ABABAB"
TEST_STR2 = "ABAB"
print(f'The 1st string is: {TEST_STR1}')
print(f'The 2nd string is: {TEST_STR2}')
print(f'The greatest common divisor is: {gcd_of_strings(TEST_STR1, TEST_STR2)}')  # Output: "AB"
