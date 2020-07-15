#!/usr/bin/env python3
def a(input_array,memory_array):
    '''Takes an array of binary digits and returns an array of all combinations of that array'''
    from itertools import compress, product
    def powerset(items):
        return( set(compress(items,mask)) for mask in product(*[[0,1]]*len(items)))

    def convert(arr):
        converted_input = []
        for i in range(input_array.bit_length()):
            # conversion to see only the active bits in an array
            if 2**i & input_array == 2**i:
                converted_input.append(2**i)
        return converted_input

    converted_input = convert(input_array)

    out = 0
    for j in powerset(converted_input):
        k = sum(j)
        if k & input_array == k:
            memory_array.add(k)
            for l in memory_array:
                if k & l == k and k != l and k != 0 and l != 0:
                    out = out | (l-k)
    print(bin(out))
    IO.arr2file(out,"input")
    return memory_array

if __name__ == "__main__":
    import os.path
    import pickle
    import IO

    in_file = "input"
    out_file = "memout"

    # Create memout if one doesn't exist
    if not os.path.isfile(out_file):
        pickle.dump(set(), open(out_file,"wb"))

    # Run and save
    pickle.dump(
            a(IO.file2arr(in_file), pickle.load(open(out_file,"rb"))),
            open(out_file,"wb"))
