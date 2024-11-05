"""
Function to calculate the perimeter of an island
"""


def island_perimeter(grid):
    """
    Function to calculate the perimeter of an island

    Parameters:
    grid: List[List[int]] - A 2D grid representing the island

    Returns:
    int - The perimeter of the island
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter


# Time complexity: O(n*m)
# Space complexity: O(1)
# n = number of rows in the grid
# m = number of columns in the grid

# Test the function
TEST_GRID = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
print(f"The grid is: {TEST_GRID}")
print(f"The perimeter of the island is: {island_perimeter(TEST_GRID)}")
# Expected output: 16
