#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor
execute only two operations in the file: Copy ALL  and Paste.
Given a number n write a method that calculates the fewest
of operations needed to result in exactly n H characters
in the file
"""


def minOperations(n):
    """
    function that calculates the fewest number of operations
    """
    if n <= 1:
        return 0
    # this checks if n is less than or equal 1. if it is the
    # function returns 0 since no operation is needed when n
    # n is 0 or 1

    operations = 0
    # keeps track of the total num of operations performed

    factor = 2
    """
    finds factor of the number n and we start from 2 since
    1 divided by any number returns that same number
    """

    while n > 1:
        while n % factor == 0:
            operations += factor
            # this line increments operations by the value of factor
            # each time this line is executed,it simulates the process
            # of Copy all followed by paste operations
            n //= factor  # using floor division to return an int
        factor += 1
        # increments factor by 1, used to check the next possible
        # factor of n

    return operations
