#!/usr/bin/env python3
'''
PARROT
Simple script that runs random input of defined density and records output        
'''
import pandas as pd
import numpy as np
from src.main import worker
import time
import sys

df = pd.DataFrame(columns=["inp","pre"])
bindata = []
for i in range(40):
    bindata.append("".join(np.random.binomial(1, 0.3, size=17).astype('U')))

data = [int(i[::-1], 2) for i in bindata]
df = pd.DataFrame(zip(bindata, data), columns=["bininp", "inp"])
df["binpre"] = 0
df["pre"] = 0

steve = worker()

def conv(x):
    return bin(x)[:1:-1]

def work(integer):
    prev = time.time()
    steve.inp = integer
    steve.run()
    steve.predict()
    now = time.time()
    print(now-prev)
    return steve.pre

df.pre = df.inp.apply(work)
df.binpre = df.pre.apply(conv)
print(df)
