#!/usr/bin/env python3
import argparse
import pandas as pd
import sys
import utils as f

def predict(inp, mem):
'''
inp, mem = f.load(args.input), f.load(args.memory)
'''
    # work on this
    if mem == 0 or inp == 0:
        pre = 0
        return self

    # inversion of input
    Ih = "".join('1' if x == '0' else '0' for x in f.int2bin(inp))

    # extend the inversion to match max bitlength of comb
    mmax = len(f.int2bin(f.uncomb(mem)[-1]))
    Ih += ('1'*(mmax - len(Ih)))
    Ih = f.bin2int(Ih)
    I = inp

    # find difference between the memory and the prediction
    # pinch all worlds that match an input world (at any timepoint)
    matches = f.paircomb(Ih, I) & mem
    if not matches:
        pre = 0
        return self
    converted = f.uncomb(matches)
    converted_filtered = [f.int2bin(i - (inp & i)) for i in converted]
    converted_int = [[int(j) for j in list(i)] for i in converted_filtered]
    max_length = max((len(i) for i in converted_int))
    for i in converted_int:
        i.extend([0] * (max_length - len(i)))
    votearray = [sum(i) for i in list(zip(*converted_int))]
    norm_votearray = [float(i)/max(votearray) for i in votearray]
    votearray = votearray
    pre = f.bin2int("".join([str(round(i)) for i in norm_votearray]))
    return sense

def parse_args(sysargs):
    parser = argparse.ArgumentParser(description='''
    predict.py - a script that precits the input/output based on a memory file 
    ''')
    parser.add_argument('-i', '--input', default='../data/input',
    help='Path of input file', type=str)
    parser.add_argument('-m', '--memory', default='../data/memory',
    help='Path of memory file to update', type=str)
    return parser.parse_args(sysargs)

if __name__ == '__main__':
    sysargs = sys.argv[1:]
    args = parse_args(sysargs)
    inp, mem = f.load(args.input), f.load(args.memory)
    inp = predict(inp, mem)
    f.save(mem, args.memory)
