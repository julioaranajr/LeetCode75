"""
Function to find the median of two sorted arrays
"""

from typing import List


def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    """
    Function to find the median of two sorted arrays

    Parameters:
    - nums1: List[int] - A list of integers
    - nums2: List[int] - A list of integers

    Returns:
    float - The median of the two sorted arrays
    """
    def find_kth_element(i: int, j: int, k: int) -> int:
        """
        Function to find the kth element in the two sorted arrays

        Parameters:
        - i: int - An integer representing the index in the first array
        - j: int - An integer representing the index in the second array
        - k: int - An integer representing the kth element to find

        Returns:
        int - The kth element in the two sorted arrays
        """
        # If the first array is exhausted, return the kth element in the second array
        if i >= len(nums1):
            return nums2[j + k - 1]
        if j >= len(nums2):
            return nums1[i + k - 1]
        if k == 1:
            return min(nums1[i], nums2[j]) # Return the minimum of the two elements
        # Find the mid elements in the two arrays
        mid1 = nums1[i + k // 2 - 1] if i + k // 2 - 1 < len(nums1) else float('inf')
        mid2 = nums2[j + k // 2 - 1] if j + k // 2 - 1 < len(nums2) else float('inf')
        # Recursively find the kth element
        if mid1 < mid2:
            return find_kth_element(i + k // 2, j, k - k // 2) # Exclude the first half of the first array
        else:
            return find_kth_element(i, j + k // 2, k - k // 2) # Exclude the first half of the second array
    # Find the median of the two sorted arrays
    total_length = len(nums1) + len(nums2)# Find the total length of the two arrays
    median1 = find_kth_element(0, 0, (total_length + 1) // 2) # Find the first median
    median2 = find_kth_element(0, 0, (total_length + 2) // 2) # Find the second median

    return (median1 + median2) / 2 # Return the average of the two medians

# Time complexity: O(log(min(n, m)))
# Space complexity: O(1)
# n = number of elements in nums1
# m = number of elements in nums2

# Test the function
TEST_NUMS1 = [1, 3]
TEST_NUMS2 = [2]
print(f'The first sorted array is: {TEST_NUMS1}')
print(f'The second sorted array is: {TEST_NUMS2}')
print(f'The median of the two sorted arrays is: {find_median_sorted_arrays(TEST_NUMS1, TEST_NUMS2)}')
# Expected output: 2.0
