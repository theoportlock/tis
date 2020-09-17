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
class comb:
    def __init__(self):
        self.files = dict()
        self.inp = 0
        self.mem_set = {}
        self.pre = 0

    def load(self, files={}, text=True):
        # needs to be either more like save or completeley seperate
        self.files = dict(files)
        if not self.files:
            self.files["inp"] = "data/input"
            self.files["mem"] = "data/memory"
            self.files["pre"] = "data/predict"

        self.mem_set = IO.setfile(filename=self.files["mem"])
        if text:
            self.inp = IO.txtfile(filename=self.files["inp"])
            self.pre = IO.txtfile(filename=self.files["pre"])
        else:
            self.inp = IO.intfile(filename=self.files["inp"])
            self.pre = IO.intfile(filename=self.files["pre"])
        return self

    def run(self):
        """
        Takes an integer, converts to binary, finds predicted bits based on
        a memory file, then updates a "memory" and "predict" file
        """
        # finds all combinations of active bits in an integer
        for com_lst in f.powerset(f.convert(self.inp)):
            com = sum(com_lst)
            self.mem_set.add(com)
            """
            # if the combination is found in memory, predict the difference
            # <-- this needs speeding up, maybe with red-black binary trees?
            # maybe use set intersect here
            #for mem in self.mem_set:
                #if com & mem == com:
                    #self.pre |= mem - com
                    print("com = ", bin(com)[:1:-1])
                    print("mem = ", bin(mem)[:1:-1])
                    print("mem-com = ", bin(mem - com)[:1:-1])
                    print("out =     ", bin(pre)[:1:-1])
                    """
            # for difference: pre -= (pre & inp)
        return self

    def save(self, files={}, text=True):
        # needs to be either more like save or completeley seperate
        self.files = dict(files)
        if not self.files:
            self.files["inp"] = "data/input"
            self.files["mem"] = "data/memory"
            self.files["pre"] = "data/predict"
        
        IO.setfile(obj=self.mem_set, mode="out", filename=self.files["mem"])
        if text:
            IO.txtfile(obj=self.pre, mode="out", filename=self.files["pre"])
        else:
            IO.intfile(obj=self.pre, mode="out", filename=self.files["pre"])
        return self
    
if __name__ == "__main__":
    worker = comb()
    if len(sys.argv) == 2:
        worker.load(
            {"inp": sys.argv[1], "mem": "memory", "pre": "predict"}
        ).run().save()
    else:
        worker.load().run().save()
