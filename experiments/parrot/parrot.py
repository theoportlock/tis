#!/usr/bin/env python3
'''
PARROT
Simple script that runs random input of defined density and records output        
'''
from src.main import worker
from src import functions as f
from datetime import datetime
import random
import time
import math

steve = worker()

print("time\t inp\t pre\t bininp\t binpre\t lstinp\t lstpre\t votepre")
percent=5
length=10
while True:
    testcase = [1]*percent + [0]*(100-percent)
    bininp = "".join(str(random.choice(testcase)) for i in range(length))
    inp = int(bininp[::-1], 2)

    steve.inp = inp
    steve.predict()
    steve.run()

    pre = steve.pre
    lstinp = f.uncomb(inp)
    lstpre = f.uncomb(pre)
    binpre = bin(steve.pre)[:1:-1]
    votepre = steve.votearray
    time_now = datetime.now().strftime("%H:%M:%S")
    print(f"{time_now}\t {inp}\t {pre}\t {bininp}\t {binpre}\t {lstinp}\t {lstpre}\t {votepre}")
