# Longest Palindrome
# Given a string s which consists of lowercase or uppercase letters,
# return the length of the longest palindrome that can be built with those letters.

def longestPalindrome(s):
    """
    Calculates the length of the longest palindrome that can be formed using the characters in the given string.
    Args:
        s (str): The input string.
    Returns:
        int: The length of the longest palindrome.
    Example:
        >>> longestPalindrome("abccccdd")
        7
    """
    
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    length = 0
    odd_count = False
    for count in char_count.values():
        if count % 2 == 0:
            length += count
        else:
            length += count - 1
            odd_count = True

    if odd_count:
        length += 1

    return length

# Test the function
LETTERS = "aABbcCcccDdd"
print(longestPalindrome(LETTERS))  # Output: 7

LETTERS = "a"
print(longestPalindrome(LETTERS))  # Output: 1
