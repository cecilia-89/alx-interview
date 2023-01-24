#!/usr/bin/python3
"""utf-8 validation"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8"""
    if len(data) == 0:
        return False
    for item in data:
        if item > 255 or item < 0:
            return False
    return True
