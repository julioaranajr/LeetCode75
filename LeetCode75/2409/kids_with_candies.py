"""
Function to find the kids with the greatest number of candies
"""

def kids_with_candies(candies: list[int], extra_candies: int) -> list[bool]:
    """
    Function to find the kids with the greatest number of candies

    Parameters:
    - candies: List[int] - A list of integers representing the number of
      candies each kid has

    - extraCandies: int - An integer representing the extra candies that
      can be given to each kid

    Returns:
    List[bool] - A list of booleans indicating whether each kid can have
    the greatest number of candies
    """
    mx = max(candies)
    return [candy >= mx - extra_candies for candy in candies]

# Time complexity: O(n)
# Space complexity: O(1)
# n = number of kids

# Test the function
TEST_CANDIES = [2, 3, 5, 1, 3]
TEST_EXTRA_CANDIES = 3
print(f'The candies are: {TEST_CANDIES}')
print(f'The extra candies are: {TEST_EXTRA_CANDIES}')
print('The kids with the greatest number of candies are:')
print(kids_with_candies(TEST_CANDIES, TEST_EXTRA_CANDIES))
# Expected output: [True, True, True, False, True]
