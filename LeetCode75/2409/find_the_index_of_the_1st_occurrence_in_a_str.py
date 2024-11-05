"""
Function to find the index of the first occurrence of a substring in a string.
"""


def find_index_of_substring(haystack: str, needle: str) -> int:
    """
    Function to find the index of the first occurrence of a substring in a string.
    """
    if not needle:
        return 0
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i : i + len(needle)] == needle:
            return i
    return -1


# Time complexity: O(n * m)
# Space complexity: O(1)
# n = len(haystack), m = len(needle)

# Test the function
TEST_HAYSTACK = "hello"
print(f"The original string is: {TEST_HAYSTACK}")
TEST_NEEDLE = "ll"
print(f"The substring to find is: {TEST_NEEDLE}")
print(
    f"The 1st. Index is: {find_index_of_substring(TEST_HAYSTACK,TEST_NEEDLE)}"
)  # Output: 2
