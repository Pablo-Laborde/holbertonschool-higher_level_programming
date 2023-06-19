#!/usr/bin/python3
""" Module Ex 5 """


def text_indentation(text):
    """ text identation """
    if type(text) != str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if (text[i] == ' ') and (text[i - 1] in ['.', '?', ':']):
            pass
        else:
            print(text[i], end="")
            if text[i] in ['.', '?', ':']:
                    print("\n")
