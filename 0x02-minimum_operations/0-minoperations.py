#!/usr/bin/python3
"""Module: minimum operations"""


def minOperations(n):
    """ calculates the fewest number of operations needed
    to result in exactly (n * H)"""

    textFile = 'H'
    count = 0
    length = len(textFile)

    while n > length:

        if n % length == 0:
            count += 2
            copyFile = textFile
            textFile += textFile

        else:
            count += 1
            textFile += copyFile

        length = len(textFile)

    return count
