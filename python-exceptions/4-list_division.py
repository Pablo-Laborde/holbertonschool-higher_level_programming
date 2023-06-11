#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    ml = []
    for i in range(list_length):
        try:
            ml.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            print("wrong type")
            ml.append(0)
        except ZeroDivisionError:
            print("division by 0")
            ml.append(0)
        except IndexError:
            print("out of range")
            ml.append(0)
    return ml
