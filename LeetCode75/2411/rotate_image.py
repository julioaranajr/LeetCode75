"""Method to rotate the matrix 90 degrees clockwise."""
from typing import List


def rotate(matrix: List[List[int]]) -> None:
    """
    Rotate the matrix 90 degrees clockwise in-place.
    """
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
