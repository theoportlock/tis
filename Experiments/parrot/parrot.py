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
    time_now = datetime.now().strftime("%H:%M:%S")

    print(f"{time_now}, {inp}, {bininp}, {pre}, {binpre}\n")
