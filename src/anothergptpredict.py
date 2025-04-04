#!/usr/bin/env python3
import argparse
import sys
import utils as f

def predict(inp, mem):
    """
    Generate a predicted bitarray based on the input and memory.
    If either the memory or input is 0, returns 0.
    """
    if mem == 0 or inp == 0:
        return 0

    # Invert the input bitarray: for each bit in the reversed binary representation,
    # change 0 -> 1 and 1 -> 0.
    inv_str = "".join('1' if bit == '0' else '0' for bit in f.int2bin(inp))
    
    # Determine the maximum bit position from memory (using 1-indexing from uncomb)
    uncomb_mem = f.uncomb(mem)
    max_pos = uncomb_mem[-1] if uncomb_mem else len(inv_str)
    
    # Extend the inversion string to match the maximum bit-length if needed.
    if len(inv_str) < max_pos:
        inv_str += '1' * (max_pos - len(inv_str))
    inv_int = f.bin2int(inv_str)
    
    I = inp
    # Compute the combined pair from the inverted input and actual input,
    # and intersect with memory.
    matches = f.paircomb(inv_int, I) & mem
    if not matches:
        return 0

    # Break the matching integer into its combinatorial components.
    converted = f.uncomb(matches)
    
    # For each component, subtract overlapping bits from the input and convert to a binary string.
    converted_filtered = [f.int2bin(i - (inp & i)) for i in converted]
    # Convert each binary string to a list of integers.
    converted_int = [[int(bit) for bit in s] for s in converted_filtered]
    
    # Normalize lengths: pad each list with zeros so they all have the same length.
    max_length = max(len(bits) for bits in converted_int)
    for bits in converted_int:
        bits.extend([0] * (max_length - len(bits)))
    
    # Column-wise vote: sum bits for each position.
    votearray = [sum(col) for col in zip(*converted_int)]
    # Normalize votes by dividing each sum by the maximum vote count.
    norm_votearray = [v / max(votearray) for v in votearray]
    # Create predicted bitarray: round each normalized value to 0 or 1 and form a binary string.
    pred_str = "".join(str(round(v)) for v in norm_votearray)
    pre = f.bin2int(pred_str)
    return pre

def parse_args(sysargs):
    parser = argparse.ArgumentParser(
        description='predict.py - a script that predicts the input/output based on a memory file'
    )
    parser.add_argument('-i', '--input', default='../data/input',
                        help='Path of input file', type=str)
    parser.add_argument('-m', '--memory', default='../data/memory',
                        help='Path of memory file to read', type=str)
    parser.add_argument('-o', '--output', default='../data/prediction',
                        help='Path of output prediction file', type=str)
    return parser.parse_args(sysargs)

if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    inp = f.load(args.input)
    mem = f.load(args.memory)
    prediction = predict(inp, mem)
    f.save(prediction, args.output)

