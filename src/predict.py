#!/usr/bin/env python3
import argparse
import pandas as pd
import sys
import utils as f

def predict(mem):
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

def parse_args():
    parser = argparse.ArgumentParser(description='''
    memorize.py - a script that updates a memory file based on the contents of an input file
    ''')
    parser.add_argument('subject')
    parser.add_argument('-i', '--input', default='../data/input',
    help='Path of input file', type=str)
    parser.add_argument('-m', '--memory', default='../data/memory',
    help='Path of memory file to update', type=str)
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args(sys.argv)
    mem = memorize(f.load(args.input), f.load(args.memory))
    f.save(mem)

