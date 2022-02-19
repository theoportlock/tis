#!/usr/bin/env python3
import pandas as pd
import random
from src import IO
from src import functions as f
from src.main import worker

df = pd.DataFrame(columns=["inp","pre"])
inp = range(5)
bininp = [bin(i)[2:] for i in inp]
df = pd.DataFrame(zip(inp, bininp), columns=["inp", "bininp"])
df["mem1"] = 0
df["binmem1"] = 0
df["mem2"] = 0
df["binmem2"] = 0
for i in df.index:
    steve = worker()
    steve.inp = int(df.inp[i])
    df.mem1[i] = steve.run().mem
    df.binmem1[i] = bin(df.mem1[i])[2:]
    steve.inp = steve.mem
    steve.mem = 0
    df.mem2[i] = steve.run().mem
    df.binmem2[i] = bin(df.mem2[i])[2:]
print(df)
