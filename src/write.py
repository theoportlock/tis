#!/usr/bin/env python3
import argparse
import utils as f

def parse_args():
    parser = argparse.ArgumentParser(description="Write a binary string to a file.")
    parser.add_argument('-i', "--input", help="Binary string to write.")
    parser.add_argument("-o", "--output", default="data/input", help="Output file path.")
    return parser.parse_args()

def write(data, output):
    f.save(f.bin2int(data), output)

def main():
    args = parse_args()
    write(args.input, args.output)

if __name__ == "__main__":
    main()

