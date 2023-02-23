#!/usr/bin/python3
""" Module: Making changes"""
import sys
def makeChange(coins, total):

    table = [0 for i in range(total + 1)]

    for i in range(1, total + 1):
        table[i] = sys.maxsize

    for i in range(1, total + 1):

        for j in range(len(coins)):
            if (coins[j] <= i):
                sub_res = table[i - coins[j]]
                if (sub_res != sys.maxsize and
                    sub_res + 1 < table[i]):
                    table[i] = sub_res + 1

    if table[total] == sys.maxsize:
        return -1

    return table[total]
