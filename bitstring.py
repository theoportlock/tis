#!/usr/bin/env python3
import pandas as pd
from src import IO
from src import functions as f
from src.main import worker

# Tests ability to recognise binary sequences from file
'''
bindata = ["10001000000011", # ABCD
           "10001000100001", # ABXD
           "10000000000000", # A
           "10001000000000", # AB
           "10001000100000", # ABX
           "10001000000010", # ABC
           "00000000100010"] # CX
'''

bindata = ["0000000000000000000000000000000000000001000000000010000",
           "0010000000000000000000000000000000000001000000000010000",
           "0011000000000000000000000000000000000001000000000010000",
           "0001100000000000000000000000000000000001000000000010000",
           "0000111000000000000000000000000000000001000000000010000",
           "0000011000000000000000000000000000000001000000000010000",
           "0000001100000000000000000000000000000001000000000010000",
           "0010000100000000000000000000000000000000000000000010000",
           "1000000000000000000000000000000000000000000000000010000"]

data = [int(i[::-1], 2) for i in bindata]

df = pd.DataFrame(zip(bindata, data), columns=["bininp", "inp"])
df["pre"] = 0
df["binpre"] = 0
df.index.name = "time"

steve = worker()
prediction = 0
for i in df.index:
    number = int(df["inp"][i])
    steve.inp = number
    steve.run()
    df["pre"][i] = steve.pre
    df["binpre"][i] = str(bin(steve.pre)[:1:-1])

print(steve.mem)
df[["bininp", "binpre"]].to_csv("results.csv")
