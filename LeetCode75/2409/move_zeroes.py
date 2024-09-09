"""
Function to move all zeroes to the end of the list
"""


def move_zeroes(nums: list[int]) -> None:
    """
    Function to move all zeroes to the end of the list

    Parameters:
    - nums: List[int] - An array of integers
    """
    i = 0 # Index to keep track of the position of the next non-zero element
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return nums

# Time complexity: O(n)
# Space complexity: O(1)
# n = length of nums

# Test the function
print("Test 1")
TEST_NUMS = [0, 1, 0, 3, 12]
print(TEST_NUMS)
print("Result:")
print(move_zeroes(TEST_NUMS)) # Expected: [1, 3, 12, 0, 0]
