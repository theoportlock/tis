def powerset(items):
    # finds all combinations of list elements
    from itertools import compress, product
    return list(set(compress(items, mask)) for mask in product(*[[0,1]]*len(items)))[1:]

def convert(arr):
    # conversion to see only the active bits
    converted_input = []
    for i in range(arr.bit_length()):
        if 2**i & arr == 2**i:
            converted_input.append(2**i)
    return converted_input
