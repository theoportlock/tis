#!/usr/bin/env python

def a(arr):
    '''Takes an array of binary digits and returns an array of all combinations of that array'''
    qry = 0 
    for j in range(1,2**arr.bit_length()):
        if j & arr == j:
            qry += 2**j
    return qry

if __name__ == "__main__":
    import IO
    in_file = "input.bin"
    out_file = "combinations.bin"
    IO.arr2file(a(IO.file2arr(in_file)),out_file)
