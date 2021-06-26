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
        import math
        # inversion of input
        Ih = "".join('1' if x == '0' else '0' for x in f.int2bin(steve.inp))

        # extend the inversion to match max bitlength of comb
        mmax = len(f.int2bin(math.floor(math.log(steve.mem, 2))))
        Ih+=('1'*(mmax - len(Ih)))
        Ih=f.bin2int(Ih)

        # find difference between the memory and the prediction
        matches = steve.mem - (steve.mem & (f.comb(Ih) + f.comb(steve.inp)))

        converted = [int(math.log(i,2)+1) for i in f.convert(matches)]

        converted_int = [[int(j) for j in list(f.int2bin(i))] for i in converted]
        votearray = [sum(i) for i in list(zip(*converted_int))]
        norm_votearray = [float(i)/max(votearray) for i in votearray]
        self.pre = f.bin2int("".join([str(round(i)) for i in norm_votearray]))

    def run(self):
        self.mem = self.mem | f.comb(self.inp)
        return self
