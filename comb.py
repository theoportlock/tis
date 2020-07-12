#!/usr/bin/env python3
def a(input_array,memory_array):
    import numpy as np
    import powerset
    '''Takes an array of binary digits and returns an array of all combinations of that array'''
    converted_input = []
    for i in range(input_array.bit_length()):
        # conversion to see only the active bits in an array
        if 2**i & input_array == 2**i:
            converted_input.append(2**i)

    converted_input_np = np.array(converted_input)
    for j in powerset.a(converted_input_np):
        k = sum(j)
        if k & input_array == k:
            ind = "{:.50e}".format(k)
            memory_array[ind] = memory_array.get(ind, [k, 0.0])
            memory_array[ind][1] += 1
            memory_array[ind][0] = k
    print(memory_array)
    return memory_array

'''
array[array1 & array2 = array1]
'''

if __name__ == "__main__":
    import os.path
    import pickle
    import IO

    in_file = "input"
    out_file = "memout"

    if not os.path.isfile(out_file):
        pickle.dump(dict(), open(out_file,"wb"))
    pickle.dump(a(IO.file2arr(in_file),pickle.load(open(out_file,"rb"))),open(out_file,"wb"))
