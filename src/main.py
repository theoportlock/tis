#!/usr/bin/env python3
from src import IO
import os.path
import sys

class worker:
    def __init__(self):
        self.files = dict()
        self.inp, self.mem, self.pre = 0, 0, 0

    def IOparse(obj=0, mode='in', filename=''):
        if mode == "in":
            if not os.path.isfile(filename):
                with open(filename, "wb") as of:
                    of.write(b'\0')
            with open(filename, "rb") as of:
                return int.from_bytes(of.read(), byteorder="big")
        elif mode == "out":
            with open(filename, "wb") as of:
                of.write(obj.to_bytes((obj.bit_length() + 7) // 8, 'big') or b'\0')

    def io(self, files={}, mode='in'):
        self.files = dict(files)
        if not self.files:
            self.files["inp"] = "data/input"
            self.files["mem"] = "data/memory"
            self.files["pre"] = "data/predict"
        self.inp = self.IOparse(obj=self.inp, mode=mode, filename=self.files["inp"])
        self.mem = self.IOparse(obj=self.mem, mode=mode, filename=self.files["mem"])
        self.pre = self.IOparse(obj=self.pre, mode=mode, filename=self.files["pre"])
        return self


    def run(self):
        com = sum(com_lst) - 1
        self.mem = self.mem | 2**com
        print(self.mem)
        return self
