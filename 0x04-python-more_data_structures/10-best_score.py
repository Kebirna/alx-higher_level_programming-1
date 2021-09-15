#!/usr/bin/python3
# 10-best_score.py


def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    lst = list(a_dictionary.keys())[0]
    lg = a_dictionary[lst]
    for i, j in a_dictionary.items():
        if v > lg:
            lg = j
            lst = i
    return (lst)
