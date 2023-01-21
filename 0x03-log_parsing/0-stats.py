#!/usr/bin/python3
"""Log Parsing: reads stdin line by line and computes metrics"""
import sys


fileSize = 0
statusCodes = {'200': 0, '301': 0, '400': 0, '401': 0,
               '403': 0, '404': 0, '405': 0, '500': 0}
try:
    for count, line in enumerate(sys.stdin, start=1):
        words = line.split()
        fileSize += int(words[-1])

        value = statusCodes.get(words[-2])
        if words[-2].isdigit() and value is not None:
            statusCodes[words[-2]] = value + 1

        if (count) % 10 == 0:
            print("File size: {}".format(fileSize))
            [print('{}: {}'.format(k, v)) for k, v in statusCodes.items()
             if v != 0]

except KeyboardInterrupt:
    print("File size: {}".format(fileSize))
    [print('{}: {}'.format(k, v))
     for k, v in statusCodes.items()]
