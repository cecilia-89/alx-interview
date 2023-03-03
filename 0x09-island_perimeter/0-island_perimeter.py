#!/usr/bin/python3
""" Module: Island Perimeter"""


def island_perimeter(grid):
    """calculates the perimeter of an island"""
    perimeter = 0
    for count, array in enumerate(grid):
        for i, item in enumerate(array):
            if item == 1:
                if array[i+1] == 0 and array[i-1] == 0:
                    perimeter += 2

                if array[i+1] == 1 and array[i-1] == 0 or \
                        array[i+1] == 0 and array[i-1] == 1:
                    perimeter += 1

                if grid[count - 1][i] == 0 and \
                        grid[count + 1][i] == 0:
                    perimeter += 2

                if grid[count - 1][i] == 1 and \
                        grid[count + 1][i] == 0 or \
                        grid[count - 1][i] == 0 and \
                        grid[count + 1][i] == 1:
                    perimeter += 1

    return perimeter
