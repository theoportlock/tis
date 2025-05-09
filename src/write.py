#!/usr/bin/env python3
import argparse
import sys
import utils as f

def write(data, output):
    f.save(f.bin2int(data), output)

def parse_args(sysargs):
    parser = argparse.ArgumentParser(description='''
    write.py - a script that writes a binary string to a file
    ''')
    parser.add_argument('data',
    help='Data string to input', type=str)
    parser.add_argument('-o', '--output', default='data/input',
    help='Path of output file', type=str)
    return parser.parse_args(sysargs)

if __name__ == '__main__':
    sysargs = sys.argv[1:]
    args = parse_args(sysargs)
    write(args.data, args.output)
