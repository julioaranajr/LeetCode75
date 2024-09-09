"""
Function to find the difference between two strings
"""
from collections import Counter

def find_the_difference(s: str, t: str) -> str:
    """
    Function to find the difference between two strings
    """
    cnt = Counter(s)
    for c in t:
        cnt[c] -= 1
        if cnt[c] < 0:
            return c
    return ""

# Time complexity: O(n)
# Space complexity: O(1)
# n = len(s) + len(t)

# Test the function
TEST_S = "abcd"
print(f'The original string is: {TEST_S}')
TEST_T = "abcde"
print(f'The modified string is: {TEST_T}')
print(f'The difference is: {find_the_difference(TEST_S, TEST_T)}')  # Output: e
