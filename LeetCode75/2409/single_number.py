"""
Function that takes a list of integers where every integer appears twice except for one.
The function returns the integer that appears only once.
"""


def single_number(nums):
    """
    Function that takes a list of integers where every integer appears twice except for one.
    The function returns the integer that appears only once.

    Parameters:
    - nums: List[int] - The list of integers

    Returns:
    - int - The integer that appears only once
    """
    result = 0
    for num in nums:
        result ^= num
    return result


# Time complexity: O(n)
# Space complexity: O(1)
# n = length of nums

# Example:
print(single_number([2, 2, 1]))  # 1
print(single_number([4, 1, 2, 1, 2]))  # 4
