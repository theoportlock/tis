#!/usr/bin/env python3
def comb(input_array, memory_array):
    '''Takes an array of binary digits and returns an array of all combinations of that array'''
    from itertools import compress, product
    def powerset(items):
        # finds all combinations of list elements
        return(set(compress(items, mask)) for mask in product(*[[0,1]]*len(items)))

    def convert(arr):
        # conversion to see only the active bits
        converted_input = []
        for i in range(input_array.bit_length()):
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
                if k & l == k:
                    out |= (l - k)
                    print("k = ", bin(k))
                    print("l = ", bin(l))
                    print("l-k=", bin(l-k))
                    print("out=", bin(out))

    print("out=", bin(out))
    print("inp=", bin(input_array))
    out -= (out & input_array)
    print("pred", bin(out))
    return memory_array, out

if __name__ == "__main__":
    import os.path
    import IO

    in_file = "input"
    memory_file = "memout"
    prediction_file = "prediction_file"

    # Create memout if one doesn't exist
    if not os.path.isfile(memory_file):
        IO.set2file(set(), memory_file)

    # Run and save
    output = comb(IO.file2arr(in_file), IO.file2set(memory_file))
    IO.set2file(output[0], memory_file)
    IO.arr2file(output[1], prediction_file)
