#!/usr/bin/env python3
'''
PARROT
Simple script that runs random input of defined density and records output        
'''
import pandas as pd
import numpy as np
from random import random
from src import functions as f
from src.main import worker

# creates and writes training data
df = pd.DataFrame(columns=["inp","pre"])
bindata = []
for i in range(6):
    bindata.append("".join(np.random.binomial(1, 0.3, size=15).astype('U')))

data = [int(i[::-1], 2) for i in bindata]
df = pd.DataFrame(zip(bindata, data), columns=["bininp", "inp"])
df["binpre"] = 0
df["pre"] = 0


def conv(x):
    return bin(x)[:1:-1]

def work(integer):
    steve = worker()
    steve.inp = integer
    steve.run()
    steve.predict()
    return steve.pre

df.pre = df.inp.apply(work)
df.binpre = df.pre.apply(conv)
print(df)
