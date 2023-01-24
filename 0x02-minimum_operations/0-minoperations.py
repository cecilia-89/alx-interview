#!/usr/bin/python3
"""Module: minimum operations"""


def minOperations(n):
    """ calculates the fewest number of operations needed
    to result in exactly (n * H)"""

    textFile, count = 'H', 0
    length = len(textFile)

    while n > length:

        if n % length == 0:
            count += 2
            copyFile = textFile
            textFile = "".join([textFile, textFile])

        else:
            count += 1
            textFile = "".join([textFile, copyFile])

        length = len(textFile)

    return count



n = 2147483640
print("Min number of operations to reach {} char: {}".format(n, minOperations(n)))