#!/usr/bin/python3
# Pascal's Triangle


def pascal_triangle(n):
    """
    A function that returns a list of lists of integers 
    representing the Pascal’s triangle of n
    """
    if n <= 0 or not isinstance(n, int):
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        if i >= 2:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
