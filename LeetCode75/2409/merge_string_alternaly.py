"""
Function to merge two strings alternatively
"""

def merge_alternately(word1: str, word2: str) -> str:
    """
    Function to merge two strings alternatively

    Parameters:
    - word1: str - A string
    - word2: str - A string

    Returns:
    str - The merged string
    """
    merged = ""
    i, j = 0, 0 #
    while i < len(word1) and j < len(word2):
        merged += word1[i] + word2[j]
        i += 1
        j += 1
    merged += word1[i:] + word2[j:]
    return merged

# Time complexity: O(n + m)
# Space complexity: O(n + m)
# n = length of word1
# m = length of word2

# Test the function
TEST_WORD1 = "abc"
TEST_WORD2 = "def"
print(merge_alternately(TEST_WORD1, TEST_WORD2)) # Expected: "adbecf"
