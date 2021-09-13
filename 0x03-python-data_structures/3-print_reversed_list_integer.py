#!/usr/bin/python3
# 3-print_reversed_list_integer.py


def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in reverse order."""
    i = len(my_list) 
    while i >= 1:
        print("{:d}\n".format(my_list[i - 1]))
