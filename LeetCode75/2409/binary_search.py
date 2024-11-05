""" Methods to perform binary search on a sorted list. """

from typing import List


def binary_search(nums: List[int], target: int) -> int:
    """
    Perform a binary search to find the index of the target in a sorted list.

    Args:
        nums (List[int]): A list of integers sorted in ascending order.
        target (int): The integer to search for.

    Returns:
        int: The index of the target if found, otherwise -1.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def search(nums: List[int], target: int) -> int:
    """Perform a binary search to find the index of the target in a sorted list."""

    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) >> 1
        if nums[mid] >= target:
            r = mid
        else:
            l = mid + 1
    return l if nums[l] == target else -1
