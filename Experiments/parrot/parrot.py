#!/usr/bin/env python3
'''
PARROT
Simple script that runs random input of defined density and records output        
'''
from src.main import worker
from datetime import datetime
import random
import time
import sys

steve = worker()
start_time = str(datetime.now().strftime("%H:%M:%S"))

with open(f"Experiments/parrot/{start_time}.csv", mode="w+") as csv_file:
    csv_file.writelines("time, inp, bininp, pre, binpre\n")

while True:
    time_now = datetime.now().strftime("%H:%M:%S")
    d1 = [0]*12 + [1]*3
    random.shuffle(d1)
    bininp = "".join(str(i) for i in d1)
    inp = int(bininp[::-1], 2)

    steve.inp = inp
    steve.run()
    steve.predict()
    pre = steve.pre
    binpre = bin(steve.pre)[:1:-1]

    with open(f"Experiments/parrot/{start_time}.csv", mode="a") as csv_file:
        time_now = datetime.now().strftime("%H:%M:%S")
        out = f"{time_now}, {inp}, {bininp}, {pre}, {binpre}\n"
        print(out)
        csv_file.writelines(out)
