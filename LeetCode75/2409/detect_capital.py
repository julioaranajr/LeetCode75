"""Methods to detect capital in a word."""


def detect_capital_use(word: str) -> bool:
    """Method to detect capital in a word."""
    if word.isupper():
        return True
    if word.islower():
        return True
    if word[0].isupper() and word[1:].islower():
        return True
    return False


def detect_capital(word: str) -> bool:
    """Method to detect capital in a word."""
    cnt = sum(c.isupper() for c in word)
    return cnt == 0 or cnt == len(word) or (cnt == 1 and word[0].isupper())
