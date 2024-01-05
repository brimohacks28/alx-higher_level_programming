#!/usr/bin/python3
# 0-print_list_integer.py
# Brian Maema Kyalo codes


def print_list_integer(my_list=[]):
    """Print all integers of a list."""
    for p in range(len(my_list)):
        print("{:d}".format(my_list[p]))
