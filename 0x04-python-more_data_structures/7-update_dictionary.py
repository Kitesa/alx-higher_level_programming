#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    for each_key in a_dictionary.keys():
        if each_key == key:
            a_dictionary[key] = value
    if key not in a_dictionary.keys():
        a_dictionary[key] = value
    return a_dictionary
