#!/usr/bin/env python3
import IO
import functions as f
import sys


def comb(input_int):
    ''' Takes an integer, converts to binary, finds predicted bits based on a
    memory file, then updates a "memory" and "predict" file
    '''

    # create memory if one doesn't exist and load
    memory_list = IO.mem2set()

    predict_int = 0
    # finds all combinations of active bits in an integer
    for comb_list in f.powerset(f.convert(input_int)):
        comb_int = sum(comb_list)
        memory_list.add(comb_int)
        # if the combination is found in memory, predict the difference
        for mem_int in memory_list:
            if comb_int & mem_int == comb_int:
                predict_int |= (mem_int - comb_int)
                '''
                print("comb_int = ", bin(comb_int)[:1:-1])
                print("mem_int  = ", bin(mem_int)[:1:-1])
                print("mem-comb = ", bin(mem_int-comb_int)[:1:-1])
                print("out=       ", bin(predict_int)[:1:-1])
                '''
    # for difference:  predict_int -= (predict_int & input_int)
    '''
    print("inp=", bin(input_int)[2:])
    print("pred", bin(predict_int)[2:])
    '''

    # save the prediction and memory
    IO.set2file(memory_list, "memory")
    IO.int2text(predict_int, "predict")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        comb(IO.text2int(sys.argv[1]))
    else:
        comb(IO.text2int("input"))
