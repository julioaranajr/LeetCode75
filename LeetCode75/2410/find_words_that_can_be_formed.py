from typing import List
from collections import Counter


def countCharacters(words: List[str], chars: str) -> int:
    """A function to find the sum of lengths of all good strings in a list.

    Args:
        words (List[str]): A list of strings.
        chars (str): A string of characters.

    Returns:
        int: The sum of lengths of all good strings.
    """
    cnt = Counter(chars)
    ans = 0
    for w in words:
        wc = Counter(w)
        if all(cnt[c] >= v for c, v in wc.items()):
            ans += len(w)
    return ans
