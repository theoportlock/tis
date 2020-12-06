#!/usr/bin/env python
def expand(number):
    for i in bin(number)[:1:-1]:
        yield i


def contract(number):
    for i in bin(number):
        print(i)

if __name__ == "__main__":
    a = 24
    b = expand(a)
    print(list(b))
    """
    c = contract(b)
    """