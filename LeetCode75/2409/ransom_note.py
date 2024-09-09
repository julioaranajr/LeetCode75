"""
Function to check if a ransom note can be constructed from a magazine.
"""
from collections import Counter

def can_construct(ransom_note: str, magazine: str) -> bool:
    """
    Function to check if a ransom note can be constructed from a magazine.

    Parameters:
    - ransomNote: str - The ransom note
    - magazine: str - The magazine

    Returns:
    - bool - True if the ransom note can be constructed, False otherwise
    """
    cnt = Counter(magazine)
    for c in ransom_note:
        cnt[c] -= 1
        if cnt[c] < 0:
            return False
    return True

# Time complexity: O(n)
# Space complexity: O(1)
# n = length of ransomNote

# Example:
print(can_construct("a", "b")) # False
print(can_construct("aa", "ab")) # False
print(can_construct("aa", "aab")) # True
