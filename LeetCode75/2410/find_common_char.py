"""Method to find the common characters among the words in a list."""

from typing import List
from collections import Counter


def common_chars(words: List[str]) -> List[str]:
    """A function to find the common characters among the words in a list.

    Args:
        words (List[str]): A list of strings.

    Returns:
        List[str]: A list of common characters.
    """
    common = Counter(words[0])
    for word in words[1:]:
        common &= Counter(word)
    return list(common.elements())
