"""
Module Can Make Arithmetic Progression From Sequence
"""

from typing import List
from itertools import tee

def can_make_arithmetic_progression(arr: List[int]) -> bool:
    """
    Function to check if the given list can form an arithmetic progression
    """
    arr.sort()
    d = arr[1] - arr[0]

    def pairwise(iterable):
        a, b = tee(iterable)
        next(b, None)
        return zip(a, b)

    return all(b - a == d for a, b in pairwise(arr))

# Test the function
TEST = [3, 5, 1]
print(can_make_arithmetic_progression(TEST))  # Output: True
