#!/usr/bin/env python3
import IO
import functions as f
import sys


class comb:
    def __init__(self):
        self.files = dict()
        self.inp_int = 0
        self.mem_lst = []
        self.pre_int = 0

    def load(self, files={}, default=True):
        self.files = files
        if default:
            self.files["inp"] = "input"
            self.files["mem"] = "memory"
            self.files["pre"] = "predict"
            self.inp_int = IO.textfile2int(self.files["inp"])
            self.mem_lst = IO.mem2set(self.files["mem"])
            self.pre_int = IO.pre2int(self.files["pre"])
        else:
            if type(files["inp"]) == str: self.files["inp"] = IO.textfile2int(files["inp"])
            else: self.files["inp"] = files["inp"]
            if type(files["mem"]) == str: self.files["mem"] = IO.mem2set(files["mem"])
            else: self.files["mem"] = files["mem"]
            if type(files["pre"]) == str: self.files["pre"] = IO.pre2int(files["pre"])
            else: self.files["pre"] = files["pre"]
        return self

    def run(self):
        ''' Takes an integer, converts to binary, finds predicted bits based on a
        memory file, then updates a "memory" and "predict" file
        '''
        if self.inp_int is None:
            print("No input")
            quit()
        if self.mem_lst is None:
            print("No memory")
            quit()
        if self.pre_int is None:
            print("No prediction")
            quit()

        # finds all combinations of active bits in an integer
        for com_lst in f.powerset(f.convert(self.inp_int)):
            com_int = sum(com_lst)
            self.mem_lst.add(com_int)
            # if the combination is found in memory, predict the difference
            # <-- this needs speeding up
            for mem_int in self.mem_lst:
                if com_int & mem_int == com_int:
                    self.pre_int |= (mem_int - com_int)
                    '''
                    print("com_int = ", bin(com_int)[:1:-1])
                    print("mem_int = ", bin(mem_int)[:1:-1])
                    print("mem-com = ", bin(mem_int - com_int)[:1:-1])
                    print("out =     ", bin(pre_int)[:1:-1])
                    '''
            # for difference:  pre_int -= (pre_int & inp_int)
        return self

    def save(self, files={}, default=True, to_text=True):
        if default:
            IO.set2intfile(self.mem_lst, self.files["mem"])
            if to_text:
                IO.int2textfile(self.pre_int, self.files["pre"])
            else:
                IO.int2intfile(self.pre_int, self.files["pre"])
        else:
            IO.set2intfile(self.mem_lst, files["mem"])
            if to_text:
                IO.int2textfile(self.pre_int, files["pre"])
            else:
                IO.int2intfile(self.pre_int, files["pre"])


if __name__ == "__main__":
    worker = comb()
    if len(sys.argv) == 2: worker.load({
        "inp": sys.argv[1],
        "mem": "memory",
        "pre": "predict"}).run().save()
    else: worker.load().run().save()
