#!/usr/bin/env python
# chopps of left hand 0's
import sys
import struct
import os

if sys.argv[1] == "e":
    with open(sys.argv[2], 'r') as inf:
        value = int(inf.read(), 2)
    with open(sys.argv[2] +'.e', 'wb') as of:
        of.write(value.to_bytes(50, byteorder='little'))
elif sys.argv[1] == "d":
    with open(sys.argv[2], 'rb') as inf:
        value = int.from_bytes(inf.read(), byteorder="big")
    with open(sys.argv[2]+'.d', 'w') as inf:
        inf.write(str(bin(value)[:1:-1]))
