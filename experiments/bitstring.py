#!/usr/bin/env python3
import pandas as pd
from src import IO
from src import functions as f
from src.main import worker

# Tests ability to recognise binary sequences from file
data = ["10000000001000000000000011",  # ABCD
        "10000000001000000001000001",  # ABXD
        "10000000000000000000000000",  # A
        "10000000001000000000000000",  # AB
        "10000000001000000001000000",  # ABX
        "10000000001000000000000010",  # ABC
        "00000000000000000001000010"]  # CX
df = pd.Dataframe(data,columns=["inp"])

steve = worker()
prediction = 0
for i in df.index:
    steve.inp = df["inp"][i]
    steve.run()
    df["pre"][i] = steve.pre
df.to_csv("experiment.csv")
