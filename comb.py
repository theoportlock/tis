#!/usr/bin/env python3
import IO

def a(input_int):
    '''Takes an array of binary digits and returns an array of all combinations of that array'''

    # Create memory if one doesn't exist and load
    memory_array = IO.mem2set()

    # Finds all combinations of active bits in an integer
    predict = 0
    for j in IO.powerset(IO.convert(input_int)):
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
    print("inp=", bin(input_int)[:1:-1])
    print("pred", bin(predict)[:1:-1])

    IO.set2file(memory_array, "memory")
    IO.int2file(predict, "predict")

if __name__ == "__main__":
    a(IO.file2int("input"))
