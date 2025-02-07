#!/usr/bin/env python3
import numpy as np
import os.path
import random
import pandas as pd
import src.functions as f

'''
# for testing
from src.main import worker
self = worker()
self.inp = f.bin2int('1101')
self.run()
self.inp = f.bin2int('11')
'''

class worker:
    def __init__(self):
        self.inp, self.mem, self.pre, self.act = 0, 0, 0, 0
        self.votearray = []

    def __repr__(self):
        return f"inp:{bin(self.inp)[:1:-1]}\nmem:{bin(self.mem)[:1:-1]}\npre:{bin(self.pre)[:1:-1]}\nact:{bin(self.act)[:1:-1]}"

    def io(self, files={}, mode='in'):
        def parse(obj=0, mode='in', filename=''):
            if mode == "in":
                if not os.path.isfile(filename):
                    with open(filename, "wb") as of:
                        of.write(b'\0')
                with open(filename, "rb") as of:
                    return int.from_bytes(of.read(), byteorder="big")
            elif mode == "out":
                with open(filename, "wb") as of:
                    of.write(obj.to_bytes((obj.bit_length() + 7) // 8, 'big') or b'\0')
                return obj
        self.files = dict(files)
        self.inp = parse(obj=self.inp, mode=mode, filename=self.files.setdefault('inp', 'data/input'))
        self.mem = parse(obj=self.mem, mode=mode, filename=self.files.setdefault('mem', 'data/memory'))
        self.pre = parse(obj=self.pre, mode=mode, filename=self.files.setdefault('pre', 'data/predict'))
        return self

    def predict(self):
        # Filter the memory array by different resolutions of the input 
        # Search through the non-activated input nodes
        if self.mem == 0 or self.inp == 0:
            self.pre = 0
            return self

        # invert the input
        Ih = "".join('1' if x == '0' else '0' for x in f.int2bin(self.inp))

        # extend the inversion to match max bitlength of comb
        mmax = len(f.int2bin(f.uncomb(self.mem)[-1]))
        Ih += ('1'*(mmax - len(Ih)))
        Ih = f.bin2int(Ih)
        I = self.inp

        # find difference between the memory and the prediction
        matches = f.paircomb(Ih, I) & self.mem
        if not matches:
            self.pre = 0
            return self
        converted = f.uncomb(matches)
        converted_filtered = [f.int2bin(i - (self.inp & i)) for i in converted]
        converted_int = [[int(j) for j in list(i)] for i in converted_filtered]
        max_length = max((len(i) for i in converted_int))
        for i in converted_int:
            i.extend([0] * (max_length - len(i)))
        votearray = [sum(i) for i in list(zip(*converted_int))]
        norm_votearray = [float(i)/max(votearray) for i in votearray]
        self.votearray = votearray
        self.pre = f.bin2int("".join([str(round(i)) for i in norm_votearray]))

    def run(self):
        self.mem = self.mem | f.comb(self.inp)
        return self
    
    def action(self):
        self.act = random.getrandbits(4)
        return self

