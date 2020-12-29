#!/usr/bin/env python3
'''
ADDITION
Should succeed after abcd-abxd
Equation tree discovery test
This experiment should test the workers ability to perform basic mathematical operations without pre-exhisting memory for a calculation. The experiment should consist of a learning phase, a testing phase, and a result recording phase.
Need to move this into the docs
Should learn like:
    1 when you see equals sign, produce a number
        
'''
import pandas as pd
import random
from src import IO
from src import functions as f
from src.main import worker

# creates and writes training data
df = pd.DataFrame(columns=["inp","pre"])
bindata = [
        "0100", #t1-1  1
        "1000", #t1-2  +
        "0100", #t1-3  1
        "0010"] #t1-4  2
        "0100", #t2-1  1
        "1000", #t2-2  +
        "0100", #t2-3  2
        "0001"] #t2-4  3
data = [int(i[::-1], 2) for i in bindata]
df = pd.DataFrame(zip(bindata, data), columns=["bininp", "inp"])
df["pre"] = 0
df["binpre"] = 0
print(df)
