#!/usr/bin/env python3
import argparse
import sys
import utils as f

def memorize(inp, mem):
    mem = mem | f.comb(inp)
    return mem

def parse_args(sysargs):
    parser = argparse.ArgumentParser(description='''
    memorize.py - a script that updates a memory file based on the contents of an input file
    ''')
    parser.add_argument('-i', '--input', default='../data/input',
    help='Path of input file', type=str)
    parser.add_argument('-m', '--memory', default='../data/memory',
    help='Path of memory file to read', type=str)
    parser.add_argument('-o', '--output', default='../data/memory',
    help='Path of memory file to update', type=str)
    return parser.parse_args(sysargs)

if __name__ == '__main__':
    sysargs = sys.argv[1:]
    args = parse_args(sysargs)
    mem = memorize(f.load(args.input), f.load(args.memory))
    f.save(mem, args.output)
