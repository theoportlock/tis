#!/usr/bin/env python3
'''
PARROT
Simple script that runs random input of defined density and records output        
'''
import pandas as pd
from random import random
from src import functions as f
from src.main import worker

# creates and writes training data
df = pd.DataFrame(columns=["inp","pre"])
arrlen = 10
bitlen = 10
bindata = []
for i in range(arrlen):
    teststring = []
    bindata.append([
            "".join([
                teststring.append(str(round(random()**2))) for i in range(bitlen)])
            ])

print(bindata)
'''
bindata = [
    "0100", #t1-1  1
    "1000", #t1-2  +
    "0100", #t1-3  1
    "0010", #t1-4  2
    "0100", #t2-1  1
    "1000", #t2-2  +
    "0100", #t2-3  2
    "0001"] #t2-4  3
data = [int(i[::-1], 2) for i in bindata]
df = pd.DataFrame(zip(bindata, data), columns=["bininp", "inp"])
df["pre"] = 0
df["binpre"] = 0
print(df)
'''
