#!/usr/bin/env python
def a(input_array,memory_array):
    #memory_array["key"].astype("category")
    '''Takes an array of binary digits and returns an array of all combinations of that array'''
    qry = 0 
    for j in range(1,2**input_array.bit_length()):
        if j & input_array == j:
            ind = str("{:.10e}".format(j))
            memory_array[ind] = j, memory_array.get(ind, 1) + 1
    return memory_array

if __name__ == "__main__":
    import os.path
    import pickle
    import IO

    in_file = "input"
    out_file = "memout"

    if not os.path.isfile(out_file):
        arr = {}
        pickle.dump(arr, open(out_file,"wb"))

    pickle.dump(a(IO.file2arr(in_file),pickle.load(open(out_file,"rb"))),open(out_file,"wb"))
