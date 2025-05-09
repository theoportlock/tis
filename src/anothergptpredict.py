#!/usr/bin/env python3
import argparse
import sys
import utils as f

def predict(inp, mem):
    # If either the input or memory is 0, early exit.
    if mem == 0 or inp == 0:
        return 0

    # Determine the bit-width needed.
    width = max(inp.bit_length(), mem.bit_length())

    # Invert the input within the fixed width using two’s complement arithmetic.
    inverted = (~inp) & ((1 << width) - 1)

    # Use the inverted input directly.
    # For instance, if your f.paircomb operates on integers, pass `inverted` instead of
    # converting it to a string, then intersect with mem.
    matches = f.paircomb(inverted, inp) & mem
    if not matches:
        return 0

    # Process further with your existing combinatorial operations.
    converted = f.uncomb(matches)
    
    # For each component, subtract overlapping bits from the input.
    # Convert the result to binary lists if needed for vote counting.
    converted_int = [
        [int(bit) for bit in f.int2bin(i - (inp & i), width)]
        for i in converted
    ]
    
    # Normalize lengths by ensuring all lists are the same size (here, they should already be of length `width`).
    max_length = width  # or recalc if needed
    for bits in converted_int:
        bits.extend([0] * (max_length - len(bits)))
    
    # Column-wise vote: sum bits for each position.
    votearray = [sum(col) for col in zip(*converted_int)]
    # Normalize votes and determine the predicted bits.
    norm_votearray = [v / max(votearray) for v in votearray]
    pred_str = "".join(str(round(v)) for v in norm_votearray)
    pre = f.bin2int(pred_str)
    return pre


def parse_args(sysargs):
    parser = argparse.ArgumentParser(
        description='predict.py - a script that predicts the input/output based on a memory file'
    )
    parser.add_argument('-i', '--input', default='data/input',
                        help='Path of input file', type=str)
    parser.add_argument('-m', '--memory', default='data/memory',
                        help='Path of memory file to read', type=str)
    parser.add_argument('-o', '--output', default='data/prediction',
                        help='Path of output prediction file', type=str)
    return parser.parse_args(sysargs)

if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    inp = f.load(args.input)
    mem = f.load(args.memory)
    prediction = predict(inp, mem)
    f.save(prediction, args.output)

