#!/usr/bin/python3

def uniq_add(my_list=[]):
    my_set = set(my_list)
    sum_of_unique = 0
    for i in my_set:
        sum_of_unique += i
    return sum_of_unique
