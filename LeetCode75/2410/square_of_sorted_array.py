"""Method to return the squares of the sorted numbers in the list."""

from typing import List


def sorted_squares(nums: List[int]) -> List[int]:
    """Return the squares of the sorted numbers in the list."""
    ans = []
    # for i in range(len(nums)):
    i, j = 0, len(nums) - 1  # Two pointers
    while i <= j:
        a = nums[i] * nums[i]  # Square of the number
        b = nums[j] * nums[j]  # Square of the number
        # Compare the square of two numbers
        if a > b:
            ans.append(a)  # Append the smaller one
            i += 1  # Move the pointer
        else:
            ans.append(b)  # Append the smaller one
            j -= 1
    # Reverse the list
    return ans[::-1]  # Return the list of squares of sorted numbers
