#!/usr/bin/env python3
'''
CONVEYOR
Tests the interaction between two workers
'''
from src.main import worker
from src import functions as f
from datetime import datetime
import random
import time
import math

# recruit the boys
alan = worker()
barry = worker()
charlie = worker()

# train them well
alan.inp = f.bin2int('110000'); alan.run()
barry.inp = f.bin2int('011000'); barry.run()
charlie.inp = f.bin2int('001100'); charlie.run()
alan.inp = f.bin2int('000110'); alan.run()
barry.inp = f.bin2int('000011'); barry.run()
charlie.inp = f.bin2int('100001'); charlie.run()

# show alan a challenge
alan.inp = f.bin2int('100000')

# let em work
while True:
    time.sleep(1)
    print(f.int2bin(alan.inp))
    alan.predict()
    barry.inp = int(alan.pre)
    time.sleep(1)
    print(f.int2bin(barry.inp))
    barry.predict()
    charlie.inp = int(barry.pre)
    time.sleep(1)
    print(f.int2bin(charlie.inp))
    charlie.predict()
    alan.inp = int(charlie.pre)
