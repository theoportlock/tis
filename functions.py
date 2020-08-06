def powerset(items: list) -> list:
    # finds all combinations of list elements
    from itertools import compress, product
    yield list(set(compress(items, mask)) for mask in product(*[[0,1]]*len(items)))[1:]


def convert(arr: int) -> list:
    # conversion to see only the active bits
    converted_input = []
    for i in range(arr.bit_length()):
        if 2**i & arr == 2**i:
            converted_input.append(2**i)
    return converted_input


def basechanger(number: int, base: int) -> list:
    remainder_stack = []
    while number > 0:
        remainder = number % base
        remainder_stack.append(remainder)
        number = number // base
    new_digits = []
    while remainder_stack:
        new_digits.append(2**remainder_stack.pop())
    return new_digits


def concat(int_list: list, level: int) -> list:
    # need to be mindfull of duplicated bits
    new = []
    count = 0
    out = 0
    for j in int_list:
        count += 1 
        out += j
        if count == 3:
            new.append(out)
            count = 0
    if not count:
        new.append(out)
    return new
