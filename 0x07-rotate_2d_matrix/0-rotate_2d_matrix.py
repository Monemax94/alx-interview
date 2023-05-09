#!/usr/bin/env python3
"""Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """Transpose the matrix
    """
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row of the transposed matrix
    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]
