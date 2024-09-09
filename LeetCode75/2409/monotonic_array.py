"""
Function to check if an array is monotonic
"""
from typing import List

def is_monotonic(nums: List[int]) -> bool:
    """
    Function to check if an array is monotonic

    Parameters:
    - nums: List[int] - An array of integers

    Returns:
    bool - True if the array is monotonic, False otherwise
    """
    return all(nums[i] <= nums[i+1] for i in range(len(nums)-1)) or \
        all(nums[i] >= nums[i+1] for i in range(len(nums)-1))

# Time complexity: O(n)
# Space complexity: O(1)
# n = length of nums

# Test the function
TEST_NUMS = [1, 2, 2, 3]
print(is_monotonic(TEST_NUMS)) # Expected: True
print(is_monotonic([1, 3, 2])) # Expected: False
