#!/usr/bin/env python
def a(input_array,memory_array):
    '''Takes an array of binary digits and returns an array of all combinations of that array'''
    converted_input = []
    for i in range(input_array.bit_length()):
        if 2**i & input_array == 2**i:
            converted_input.append(2**i)

    for j in converted_input:
        print(j)
        print(input_array)
        if j & input_array == j:
            print("true")
            ind = "{:.10e}".format(j)
            memory_array[ind] = memory_array.get(ind, [j, 0.0])
            memory_array[ind][1] += 1
            memory_array[ind][0] = j
    print(memory_array)
    return memory_array

if __name__ == "__main__":
    import os.path
    import pickle
    import IO

    in_file = "input"
    out_file = "memout"

    if not os.path.isfile(out_file):
        pickle.dump(dict(), open(out_file,"wb"))
    pickle.dump(a(IO.file2arr(in_file),pickle.load(open(out_file,"rb"))),open(out_file,"wb"))
