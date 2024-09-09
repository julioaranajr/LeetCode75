"""
Function to reverse the vowels in a string
"""

def reverse_vowels(s: str) -> str:
    """
    Function to reverse the vowels in a string

    Parameters:
    - s: str - The input string

    Returns:
    - str - The string with vowels reversed
    """
    s = list(s)

    left, right = 0, len(s) - 1
    while left < right:
        while left < right and s[left] not in "aäeioöuüAÄEIOÖUÜ":
            left += 1
        while right > 0 and s[right] not in "aäeioöuüAÄEIOÖUÜ":
            right -= 1

        if left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    return "".join(s)

# Time complexity: O(n)
# Space complexity: O(n)
# n = length of s

# Example:
print(reverse_vowels("hello")) # "holle"
print(reverse_vowels("world")) # "world"
