#!/usr/bin/python3
""" Module Ex 5 """


def text_indentation(text):
    """ text identation """
    if type(text) != str:
        raise TypeError("text must be a string")
    x = text
    x = x.replace(". ", ".")
    x = x.replace(".", ".\n\n")
    x = x.replace("? ", "?")
    x = x.replace("?", "?\n\n")
    x = x.replace(": ", ":")
    x = x.replace(":", ":\n\n")
    print(x, end="")
