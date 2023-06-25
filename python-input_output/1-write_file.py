#!/usr/bin/python3
""" Ex 1 """


def write_file(filename="", text=""):
    """ read file function """
    with open(filename, "r", encoding="utf-8") as ifile:
        txt = ifile.read()
        with open(text, "w") as ofile:
            return ofile.write(txt)
