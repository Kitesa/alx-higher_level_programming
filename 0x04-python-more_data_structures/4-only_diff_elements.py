#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    only_diff_elements = [i for i in set_1 or i in set_2 if not (i in set_2 and i in_set_2)]
    return only_diff_elements
