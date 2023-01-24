#!/usr/bin/python3
"""utf-8 validation"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8"""
    if len(data) == 0:
        return False
    for item in data:
        if item > 255:
            return False
    return True


data = []
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))