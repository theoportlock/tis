#!/usr/bin/env python3
'''
MATHS
Equation tree discovery test
This experiment should test the workers ability to perform basic mathematical operations without pre-exhisting memory for a calculation. The experiment should consist of a learning phase, a testing phase, and a result recording phase.
Need to move this into the docs
'''
import pandas as pd
import random
from src import IO
from src import functions as f
from src.main import worker

# creates and writes training data
df = pd.DataFrame(columns=["inp","pre"])
bindata = [
        "0100", # 1
        "1000", # +
        "0100", # 1
        "0010"] # 2
data = [int(i[::-1], 2) for i in bindata]
df = pd.DataFrame(zip(bindata, data), columns=["bininp", "inp"])
df["pre"] = 0
df["binpre"] = 0
print(df)
