#!/usr/bin/env python
import sys
import os

def parse(obj=0, mode='in', filename=''):
    if mode == "in":
        if not os.path.isfile(filename):
            with open(filename, "wb") as of:
                of.write(b'\0')
        with open(filename, "rb") as of:
            return int.from_bytes(of.read(), byteorder="big")
    elif mode == "out":
        with open(filename, "wb") as of:
            of.write(obj.to_bytes((obj.bit_length() + 7) // 8, 'big') or b'\0')

'''
if sys.argv[1] == "d":
    with open(sys.argv[2], 'rb') as inf:
        with open(sys.argv[2]+".d", 'w') as of:
            print(int(inf.read()))
            of.write(inf.read().decode('utf-8'))
elif sys.argv[1] == "e":
    with open(sys.argv[2], "r") as inf:
        with open(sys.argv[2]+".e", 'wb') as of:
            of.write(inf.read().encode('utf-8'))
'''
if sys.argv[1] == "e":
    with open(sys.argv[2], 'r') as inf:
        value = int(inf.read())
    parse(obj=value, filename=sys.argv[2]+".d", mode='out')
elif sys.argv[1] == "d":
    value = parse(filename=sys.argv[2], mode='in')
    with open(sys.argv[2]+".e", 'w') as inf:
        inf.write(str(value))
