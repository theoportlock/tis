#!/usr/bin/env python3
from src import IO
from src import functions as f
import sys


class comb:
    def __init__(self):
        self.files = dict()
        self.inp = 0
        self.mem_set = {}
        self.pre = 0

    def load(self, files={}, from_text=True):
        # needs to be either more like save or completeley seperate
        self.files = dict(files)
        if self.files:
            self.mem_set = IO.mem2set(self.files["mem"])
            if from_text:
                self.inp = IO.textfile2int(self.files["inp"])
                self.pre = IO.textpre2int(self.files["pre"])
            else:
                self.inp = IO.intfile2int(self.files["inp"])
                self.pre = IO.intpre2int(self.files["pre"])
        else:
            self.files["inp"] = "data/input"
            self.files["mem"] = "data/memory"
            self.files["pre"] = "data/predict"
            if from_text:
                self.inp = IO.textfile2int(self.files["inp"])
                self.mem_set = IO.mem2set(self.files["mem"])
                self.pre = IO.pre2int(self.files["pre"])
            else:
                self.inp = IO.intfile2int(self.files["inp"])
                self.mem_set = IO.mem2set(self.files["mem"])
                self.pre = IO.pre2int(self.files["pre"])

        return self

    def run(self):
        """ Takes an integer, converts to binary, finds predicted bits based on
        a memory file, then updates a "memory" and "predict" file
        """
        # finds all combinations of active bits in an integer
        for com_lst in f.powerset(f.convert(self.inp)):
            com = sum(com_lst)
            self.mem_set.add(com)
            # if the combination is found in memory, predict the difference
            # <-- this needs speeding up
            for mem in self.mem_set:
                if com & mem == com:
                    self.pre |= mem - com
                    """
                    print("com = ", bin(com)[:1:-1])
                    print("mem = ", bin(mem)[:1:-1])
                    print("mem-com = ", bin(mem - com)[:1:-1])
                    print("out =     ", bin(pre)[:1:-1])
                    """
            # for difference:  pre -= (pre & inp)
        return self

    def save(self, files={}, to_text=True):
        if files:
            IO.set2intfile(self.mem_set, files["mem"])
            if to_text:
                IO.int2textfile(self.pre, files["pre"])
            else:
                IO.int2intfile(self.pre, files["pre"])
        else:
            IO.set2intfile(self.mem_set, self.files["mem"])
            if to_text:
                IO.int2textfile(self.pre, self.files["pre"])
            else:
                IO.int2intfile(self.pre, self.files["pre"])


if __name__ == "__main__":
    worker = comb()
    if len(sys.argv) == 2:
        worker.load(
            {"inp": sys.argv[1], "mem": "memory", "pre": "predict"}
        ).run().save()
    else:
        worker.load().run().save()
