#!/usr/bin/env python3
import argparse
import sys
import utils as f

def read(filename):
    print(f.int2bin(f.load(filename)))

def parse_args(sysargs):
    parser = argparse.ArgumentParser(description='''
    read.py - a script that prints the binary of a file
    ''')
    parser.add_argument('-f','--filename',
    help='File to input', default='data/input', type=str)
    return parser.parse_args(sysargs)

if __name__ == '__main__':
    sysargs = sys.argv[1:]
    args = parse_args(sysargs)
    read(args.filename)
