#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorted_dic = sorted(a_dictionary)
    for i in sorted_dic:
        print("{}: {}".format(i,sorted_dic[i]))
