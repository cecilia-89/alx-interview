#!/usr/bin/python3
""" Module: Making changes"""
import sys


def makeChange(coins, total):

    if (total == 0):
        return 0
    res = sys.maxsize

    for i in range(0, len(coins)):
        if (coins[i] <= total):
            sub_res = makeChange(coins, len(coins), total-coins[i])
            if (sub_res != sys.maxsize and sub_res + 1 < res):
                res = sub_res + 1

    return res
