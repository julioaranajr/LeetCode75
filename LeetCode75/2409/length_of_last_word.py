"""
Function to find the length of the last word in a string.
"""


def length_of_last_word(s: str) -> int:
    """
    Function to find the length of the last word in a string.

    Parameters:
    - s: str - A string containing words separated by spaces

    Returns:
    int - The length of the last word in the string
    """
    # Strip any trailing spaces and split the string by spaces
    words = s.strip().split()
    # Return the length of the last word
    return len(words[-1]) if words else 0


# Time complexity: O(n)
# Space complexity: O(n)
# n = number of characters in the string

# Test the function
TEST_STRING = "I love Python"
print(f'The string is: "{TEST_STRING}"')
print(f"The length of the last word is: {length_of_last_word(TEST_STRING)}")
# Expected output: 6
