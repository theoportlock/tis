#!/usr/bin/env python
import re
def expand(int_number):
    binary = bin(int_number)[:1:-1]
    active_list = [pos for pos, char in enumerate(binary) if char == "1"]
    final = 0
    for i in range(2**len(active_list)):
        final += sum([2**i for i in active_list])

    return active_list

def contract(binary_number):
    return int(binary_number, 2)

if __name__ == "__main__":
    a = 6
    b = expand(a)
    #c = contract(b)
    print(b)
    #print(c)
