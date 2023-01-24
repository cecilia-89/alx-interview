#!/usr/bin/python3
"""utf-8 validation"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8"""
 
    for item in data:
        if item > 255:
            return False
    return True
