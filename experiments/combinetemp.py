#!/usr/bin/env python3
import pandas as pd
import random
from src import IO
from src import functions as f
from src.main import worker

df = pd.DataFrame(columns=["inp","pre"])
inp = range(20)
bininp = [bin(i)[2:] for i in inp]
df = pd.DataFrame(zip(inp, bininp), columns=["inp", "bininp"])
df["mem"] = 0
df["binmem"] = 0
for i in df.index:
    steve = worker()
    steve.inp = int(df.inp[i])
    df.mem[i] = steve.run().mem
    df.binmem[i] = bin(df.mem[i])[2:]
print(df)
