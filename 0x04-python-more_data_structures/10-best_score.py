#!/usr/bin/python3

def best_score(a_dictionary):
    values = a_dictionary.values()
    for i in a_dictionary.keys():
        if a_dictionary[i] == max(values):
            return i
    if not a_dictionary.values():
        return None
