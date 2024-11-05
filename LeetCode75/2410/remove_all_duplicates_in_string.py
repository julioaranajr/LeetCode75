"""Remove All Adjacent Duplicates in String"""


def remove_duplicates(s: str) -> str:
    """Remove all adjacent duplicates in a string.

    Args:
        s (str): The input string.

    Returns:
        str: The string with all adjacent duplicates removed.
    """
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return "".join(stack)
