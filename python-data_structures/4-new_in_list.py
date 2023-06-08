#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    nl = my_list.copy()
    length = len(nl)
    if idx > 0:
        if idx <= length:
            nl[idx] = element
        else:
            nl.append(element)
    return nl
