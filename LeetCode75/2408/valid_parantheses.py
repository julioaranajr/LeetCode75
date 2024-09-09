"""
Function to check if a string of parasyntheses is valid or not
"""

def is_valid(s: str) -> bool:
    """
    Function to check if a string of parasyntheses is valid or not
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)

    return not stack

# Time complexity: O(n)
# Space complexity: O(n)
# n = len(s)

# Test the function
TEST = "()[]{}"
print(is_valid(TEST))  # Output: True
