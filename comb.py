#!/usr/bin/env python
def a(input_array,memory_array):
    import numpy as np
    from itertools import combinations
    '''Takes an array of binary digits and returns an array of all combinations of that array'''
    converted_input = []
    for i in range(input_array.bit_length()):
        # conversion to see only the active bits in an array
        if 2**i & input_array == 2**i:
            converted_input.append(2**i)

<<<<<<< HEAD
    for j,k in enumerate(converted_input):
        # find the active combination and add one to the charge
        if j & input_array == j:
=======
    converted_input_np = np.array(converted_input)
    for j in np.combinations(converted_input_np):
        if np.sum(j) & input_array == j:
>>>>>>> 90eedb1dd2d5e4b92ca94d8f5925e2e50b86b0c3
            ind = "{:.50e}".format(j)
            memory_array[ind] = memory_array.get(ind, [j, 0.0])
            memory_array[ind][1] += 1
            memory_array[ind][0] = j
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
