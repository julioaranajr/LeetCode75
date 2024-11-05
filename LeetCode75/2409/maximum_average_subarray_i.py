"""
Function to find the maximum average of a subarray of length k.
"""


def find_max_average(nums: list[int], k: int) -> float:
    """
    Function to find the maximum average of a subarray of length k.

    Parameters:
    - nums: List[int] - A list of integers
    - k: int - An integer representing the length of the subarray

    Returns:
    float - The maximum average of a subarray of length k
    """
    # Initialize the maximum average for the first k elements
    ans = s = sum(nums[:k])  # sum of the first k elements
    for i in range(k, len(nums)):  # iterate from k to the end of the list
        s += (
            nums[i] - nums[i - k]
        )  # add the current element and subtract the element k steps back
        ans = max(ans, s)  # update the maximum average
    return ans / k  # return the maximum average


# Time complexity: O(n)
# Space complexity: O(1)
# n = number of elements in the list

# Test the function
TEST_NUMS = [1, 12, -5, -6, 50, 3]
TEST_K = 4
print(f"The list of numbers is: {TEST_NUMS}")
print(
    f"The maximum average of a subarray of length {TEST_K} is: {find_max_average(TEST_NUMS, TEST_K)}"
)
# Expected output: 21.25
