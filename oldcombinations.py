#!/usr/bin/env python

def a(arr):
    '''Takes a numpy array of binary digits and returns a numpy array of all combinations of that array'''
    import numpy as np
    #qry = np.zeros(2**arr.bit_length(),dtype=np.uint8)
    qry = np.array([])
    for j in range(1,2**arr.bit_length()-1):
        print(bin(j),bin(arr))
        if j & arr == j:
            print("true")
            np.append(j)
    return qry.dot(2**np.arange(qry.size))

if __name__ == "__main__":
    import IO
    in_file = "input.bin"
    out_file =  "combinations.bin"
    IO.arr2file(a(IO.file2arr(in_file)),out_file)
