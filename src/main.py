#!/usr/bin/env python3
from src import IO
import src.functions as f
import os.path
import sys

class worker:
    def __init__(self):
        self.inp, self.mem, self.pre = 0, 0, 0

    def __repr__(self):
        return f"inp:{bin(self.inp)[:1:-1]}\nmem:{bin(self.mem)[:1:-1]}\npre:{bin(self.pre)[:1:-1]}"

    def io(self, files={}, mode='in'):
        self.files = dict()
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

        self.files = dict(files)
        if not self.files:
            self.files["inp"] = "data/input"
            self.files["mem"] = "data/memory"
            self.files["pre"] = "data/predict"
        self.inp = parse(obj=self.inp, mode=mode, filename=self.files["inp"])
        self.mem = parse(obj=self.mem, mode=mode, filename=self.files["mem"])
        self.pre = parse(obj=self.pre, mode=mode, filename=self.files["pre"])
        return self

    def predict(self):
        from math import sqrt
        from statistics import mean
        pre = []
        for i in f.convert(self.mem):
            pre.append(bin(len(bin(i)[2:]))[:1:-1])
        #print("combinations stored in memory \n", pre)
        j = 0
        final = []
        while True:
            j += 1
            filtered = []
            [filtered.append(x) for x in pre if len(x) >= j]
            if len(filtered) == 0:
                break
            final.append(mean([int(i[j-1]) for i in filtered]))
        self.pre = int("".join([str(round(i)) for i in final[::-1]]),2)

    def run(self):
        for com_lst in f.powerset(f.convert(self.inp)):
            com = sum(com_lst) - 1
            self.mem = self.mem | 2**com
        return self
