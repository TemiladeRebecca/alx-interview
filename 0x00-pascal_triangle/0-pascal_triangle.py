#!/usr/bin/python3
# Pascal's Triangle


def pascal_triangle(n):
    """
    A function that returns a list of lists of integers 
    representing the Pascal’s triangle of n
    """
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    for x in range(n):
        row = []
        for y in range(x+1):
            if y == 0 or y == x:
                row.append(1)
            else:
                row.append(triangle[x-1][y]+triangle[x-1][y-1])
        triangle.append(row)
    return triangle
