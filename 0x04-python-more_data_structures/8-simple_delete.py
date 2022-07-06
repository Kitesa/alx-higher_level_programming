#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    for i in a_dictionary.keys():
        if i == key:
            a_dictionary.remove(a_dictionary[i])
    if key not in a_dictionary.keys():
        pass
    return a_dictionary
