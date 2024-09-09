"""
Function to check if a string is a subsequence of another string
"""

def is_subsequence(s: str, t: str) -> bool:
    """
    Function to check if a string is a subsequence of another string
    """
    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)

# Time complexity: O(n)
# Space complexity: O(1)
# n = len(t)

# Test the function
TEST_S = "abc"
TEST_T = "ahbgdc"
print(f'The 1st str is: {TEST_S}')
print(f'The 2nd str is: {TEST_T}')
print(f'Is 1st str a subsequence of the 2nd str? {is_subsequence(TEST_S, TEST_T)}')
