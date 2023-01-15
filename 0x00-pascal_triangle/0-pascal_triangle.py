#!/usr/bin/python3
"""Pascal Triangle implementation using python"""


def pascal_triangle(n):
    """Pasacal triangle using recursion"""
    if n < 1:
        return []

    if n == 1:
        return [[n]]

    new_lst = pascal_triangle(n-1)

    lst = new_lst[-1]
    my_lst = []
    if len(lst) == 1:
        my_lst.extend([1] * 2)
        new_lst.append(my_lst)

        return new_lst

    for count, item in enumerate(lst):
        num = count + 1
        if num >= len(lst):
            break
        my_lst.append(item + lst[num])

    my_lst.insert(0, 1)
    my_lst.append(1)
    new_lst.append(my_lst)
    return new_lst

print(pascal_triangle(54))