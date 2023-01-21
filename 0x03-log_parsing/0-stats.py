#!/usr/bin/python3
"""Module: Log Parsing
eads stdin line by line and computes metrics"""
import sys


fileSize = 0
statusCodes = {}
for count, line in enumerate(sys.stdin, start = 1):
    try:
        words = line.split()
        fileSize += int(words[-1])
        value = statusCodes.setdefault(words[-2], 0)
        statusCodes[words[-2]] = value + 1

        if (count) % 10 == 0:
            print("File size: {}".format(fileSize))
            [print(f'{k}: {v}') for k, v in sorted(statusCodes.items())]

    except KeyboardInterrupt:
        print("File size: {}".format(fileSize))
        [print(f'{k}: {v}') for k, v in sorted(statusCodes.items())]

