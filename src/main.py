#!/usr/bin/env python3
from src import IO
from src import functions as f
import sys
'''
maybe this?
import collections
memory = collections.Counter()
need to move to super combinations for sparcity
dont forget about OR combinatorics
'''

class worker:
    def __init__(self):
        self.files = dict()
        self.inp = 0
        self.mem = 0
        self.pre = 0

    def load(self, files={}, text=False):
        self.files = dict(files)
        if not self.files:
            self.files["inp"] = "data/input"
            self.files["mem"] = "data/memory"
            self.files["pre"] = "data/predict"
        self.mem = IO.intfile(filename=self.files["mem"])
        if text:
            self.inp = IO.txtfile(filename=self.files["inp"])
        else:
            self.inp = IO.intfile(filename=self.files["inp"])
        return self

    def save(self, files={}, text=False):
        self.files = dict(files)
        if not self.files:
            self.files["inp"] = "data/input"
            self.files["mem"] = "data/memory"
            self.files["pre"] = "data/predict"
        IO.intfile(obj=self.mem, mode="out", filename=self.files["mem"])
        if text:
            IO.txtfile(obj=self.pre, mode="out", filename=self.files["pre"])
        else:
            IO.intfile(obj=self.pre, mode="out", filename=self.files["pre"])
        return self

    def run(self):
        for com_lst in f.powerset(f.convert(self.inp)):
            com = sum(com_lst) - 1
            self.mem = self.mem | 2**com
        return self


if __name__ == "__main__":
    steve = worker()
    if len(sys.argv) == 2:
        steve.load({"inp": sys.argv[1], "mem": "memory", "pre": "predict"}).run().save()
    else:
        steve.load().run().save()
