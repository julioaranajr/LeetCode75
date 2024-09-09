"""
Function to check if there are any duplicates in the list of numbers within k distance
"""

def contains_nearby_duplicate(nums, k):
    """
    Function to check if there are any duplicates in the list of numbers within k distance
    """
    d = {}
    for i, num in enumerate(nums):
        if num in d and abs(i - d[num]) <= k:
            return True
        d[num] = i
    return False

# Time complexity: O(n)
# Space complexity: O(n)
# n = len(nums)

# Test the function
TEST_NUMS = [1, 2, 3, 1]
TEST_K = 3
print(contains_nearby_duplicate(TEST_NUMS, TEST_K))  # Output: True
