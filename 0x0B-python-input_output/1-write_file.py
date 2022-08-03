#!/usr/bin/python3
"""
function to write string to a text file(UTF8) and return number of char written
"""


def write_file(filename="", text=""):
    """ module write_file
    """
    with open(filename, 'w') as f:
        return f.write(text)
