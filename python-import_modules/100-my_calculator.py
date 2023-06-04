#!/usr/bin/python3

def add(a, b):
    return (a + b)


def sub(a, b):
    return (a - b)


def mul(a, b):
    return (a * b)


def div(a, b):
    return (a / b)


def func_op(a, b, op):
    if op == '+':
        return (add(a, b))
    elif op == '-':
        return (sub(a, b))
    elif op == '*':
        return (mul(a, b))
    elif op == '/':
        return (div(a, b))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        s_exit(1)


if __name__ == "__main__":
    from sys import argv as av, exit as s_exit
    ac = len(av)
    if ac != 4:
        s_exit(1)
    res = func_op(int(av[1]), int(av[3]), av[2])
    print("{} {} {} = {}".format(av[1], av[2], av[3], res))
