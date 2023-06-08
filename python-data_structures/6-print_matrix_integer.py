#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if len(matrix) > 0:
        for i in matrix:
            if len(j) > 0:
                for j in i:
                    if j != i[-1]:
                        print("{:d}".format(j), end=" ")
                    else:
                        print("{:d}".format(j))
            else:
                print()
    else:
        print()
