#!/usr/bin/env python3
import IO
import functions as f
import sys

class comb:
    def __init__(self):
        self.files = dict()
    
    def load(self, files={}, default=True):
        if default:
            self.files["inp"] = "input"
            self.files["mem"] = "memory"
            self.files["pre"] = "predict"
            self.inp_int = IO.text2int(self.files["inp"])
            self.mem_lst = IO.mem2set(self.files["mem"])
            self.pre_int = IO.text2int(self.files["pre"])
        else:
            if type(files["inp"]) == str:
                self.files[inp_int] = IO.text2int(files["inp"])
            else:
                self.files["inp"] = files["inp"]
            if type(files["mem"]) == str:
                self.files[inp_int] = IO.mem2set(files["mem"])
            else:
                self.files["mem"] = files["mem"]
            if type(files["pre"]) == str:
                self.files[inp_int] = IO.text2set(files["mem"])
            else:
                self.files["pre"] = files["pre"]
        return self

    def run(self):
        ''' Takes an integer, converts to binary, finds predicted bits based on a
        memory file, then updates a "memory" and "predict" file
        '''
        if self.inp_int == None:
            print("No input")
            quit()
        if self.mem_lst == None:
            print("No memory")
            quit()
        if self.pre_int == None:
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

    def save(self, files={}, default=True):
        if default:
            IO.set2file(self.files["mem"], self.mem)
            IO.int2text(self.files["pre"], self.pre)
        else:
            IO.set2file(files["mem"], self.mem)
            IO.int2text(files["pre"], self.pre)


if __name__ == "__main__":
    worker = comb()
    if len(sys.argv) == 2:
        worker.load({"inp":sys.argv[1], "mem":"memory", "pre":"predict"}).run()
    else:
        worker.load().run()
