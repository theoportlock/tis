#!/usr/bin/env python3
import IO
import functions as f
import sys

def comb(inp_int: int):
    ''' Takes an integer, converts to binary, finds predicted bits based on a
    memory file, then updates a "memory" and "predict" file
    '''
    # create memory if one doesn't exist and load
    mem_lst = IO.mem2set()

    # finds all combinations of active bits in an integer
    pre_int = 0
    for com_lst in f.powerset(f.convert(inp_int)):
        com_int = sum(com_lst)
        mem_lst.add(com_int)
        # if the combination is found in memory, predict the difference
        for mem_int in mem_lst:
            if com_int & mem_int == com_int:
                pre_int |= (mem_int - com_int)
                '''
                print("com_int = ", bin(com_int)[:1:-1])
                print("mem_int = ", bin(mem_int)[:1:-1])
                print("mem-com = ", bin(mem_int - com_int)[:1:-1])
                print("out =     ", bin(pre_int)[:1:-1])
                '''
    # for difference:  pre_int -= (pre_int & inp_int)
    print("inp_int = ", bin(inp_int)[2:])
    print("pre_int = ", bin(pre_int)[2:])
    # save the prediction and memory
    IO.set2file(mem_lst, "memory")
    IO.int2text(pre_int, "predict")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        comb(IO.text2int(sys.argv[1]))
    else:
        comb(IO.text2int("input"))
