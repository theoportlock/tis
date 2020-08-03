#!/usr/bin/env python3
import IO
import functions as f
import sys

def comb(input_int):
    '''Takes an array of binary digits and returns an array of all combinations of that array'''

    # Create memory if one doesn't exist and load
    memory_array = IO.mem2set()

    # Finds all combinations of active bits in an integer
    predict = 0
    for j in f.powerset(f.convert(input_int)):
        k = sum(j)
        if k & input_int == k:
            memory_array.add(k)
            for l in memory_array:
                if k & l == k:
                    predict |= (l - k)
                    '''
                    print("k = ", bin(k)[:1:-1])
                    print("l = ", bin(l)[:1:-1])
                    print("l-k=", bin(l-k)[:1:-1])
                    print("out=", bin(predict)[:1:-1])
                    '''

    predict -= (predict & input_int)
    print("inp=", bin(input_int)[2:])
    print("pred", bin(predict)[2:])

    IO.set2file(memory_array, "memory")
    IO.int2text(predict, "predict")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        comb(IO.text2int(sys.argv[1]))
    else:
        comb(IO.text2int("input"))
