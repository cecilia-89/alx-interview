#!/usr/bin/python3
"""Log Parsing: reads stdin line by line and computes metrics"""
import sys


fileSize = 0
statusCodes = {}
try:
    for count, line in enumerate(sys.stdin, start=1):
        words = line.split()
        fileSize += int(words[-1])
        value = statusCodes.setdefault(words[-2], 0)
        statusCodes[words[-2]] = value + 1

        if (count) % 10 == 0:
            print("File size: {}".format(fileSize))
            [print('{}: {}'.format(k, v))
             for k, v in sorted(statusCodes.items())]

except KeyboardInterrupt:
    print("File size: {}".format(fileSize))
    [print('{}: {}'.format(k, v))
     for k, v in sorted(statusCodes.items())]
