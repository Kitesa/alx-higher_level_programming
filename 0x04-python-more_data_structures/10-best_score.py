#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return
    values = a_dictionary.values()
    for i in a_dictionary.keys():
        if a_dictionary[i] == max(values):
            return i
