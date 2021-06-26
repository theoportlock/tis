#!/usr/bin/env python3
'''
PARROT
Simple script that runs random input of defined density and records output        
'''
from src.main import worker
from datetime import datetime
import random
import time

steve = worker()

print("time, inp, bininp, pre, binpre")
percent=7
length=10
while True:
    testcase = [1]*percent + [0]*(100-percent)
    bininp = "".join(str(random.choice(testcase)) for i in range(length))
    inp = int(bininp[::-1], 2)


    steve.inp = inp
    steve.run()
    steve.predict()

    pre = steve.pre
    binpre = bin(steve.pre)[:1:-1]
    time_now = datetime.now().strftime("%H:%M:%S")
    print(f"{time_now}, {inp}, {bininp}, {pre}, {binpre}")
