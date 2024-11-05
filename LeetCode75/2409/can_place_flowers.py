"""
Function to check if we can place n flowers in the flowerbed
"""


def can_place_flowers(flowerbed: list[int], n: int) -> bool:
    """
    Function to check if we can place n flowers in the flowerbed
    """
    count = 0
    length = len(flowerbed)

    for i in range(length):
        if flowerbed[i] == 0:
            prev_empty = (i == 0) or (flowerbed[i - 1] == 0)
            next_empty = (i == length - 1) or (flowerbed[i + 1] == 0)

            if prev_empty and next_empty:
                flowerbed[i] = 1
                count += 1

                if count >= n:
                    return True

    return count >= n


# Time complexity: O(n)
# Space complexity: O(1)
# n = len(flowerbed)

# Test the function
TEST_FLOWERBED = [1, 0, 0, 0, 1]
TEST_N = 1
print(can_place_flowers(TEST_FLOWERBED, TEST_N))  # Output: True
