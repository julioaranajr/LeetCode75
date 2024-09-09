"""
Function to check if two strings are anagrams of each other.
"""

from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    """
    Function to check if two strings are anagrams of each other.

    Parameters:
    - s: str - The first string
    - t: str - The second string

    Returns:
    - bool - True if the strings are anagrams, False otherwise
    """
    if len(s) != len(t):
        return False

    cnt_s = Counter(s)
    cnt_t = Counter(t)

    return cnt_s == cnt_t

# Time complexity: O(n)
# Space complexity: O(1)
# n = length of s and t

# Example:
print(is_anagram("anagram", "nagaram")) # True
print(is_anagram("rat", "car")) # False
print(is_anagram("listen", "silent")) # True
print(is_anagram("arepera", "arepera")) # True
