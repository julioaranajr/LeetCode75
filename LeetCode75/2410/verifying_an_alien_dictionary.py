def isAlienSorted(self, words: List[str], order: str) -> bool:
    """A function to check if the words are sorted in lexicographical order.

    Args:
        words (List[str]): A list of strings.
        order (str): A string of characters.

    Returns:
        bool: A boolean value.
    """
    m = {c: i for i, c in enumerate(order)}
    for i in range(20):
        prev = -1
        valid = True
        for x in words:
            curr = -1 if i >= len(x) else m[x[i]]
            if prev > curr:
                return False
            if prev == curr:
                valid = False
            prev = curr
        if valid:
            return True
    return True
