#!/usr/bin/env python3
import argparse
import utils as f
import sys

def parse_args():
    parser = argparse.ArgumentParser(description="Merge two binary files with bit padding.")
    parser.add_argument("-a", "--input-a", required=True, help="First input file.")
    parser.add_argument("-b", "--input-b", required=True, help="Second input file.")
    parser.add_argument("-pa", "--pad-a", type=int, required=True, help="Bit length to pad first file to.")
    parser.add_argument("-pb", "--pad-b", type=int, required=True, help="Bit length to pad second file to.")
    parser.add_argument("-o", "--output", required=True, help="Output file path.")
    return parser.parse_args()

def pad_binary(bitstring, length):
    if len(bitstring) > length:
        sys.exit(f"Error: Bitstring too large for requested padding ({len(bitstring)} > {length}).")
    return bitstring.zfill(length)

def main():
    args = parse_args()

    # Load as integers then to binary
    a_int = f.load(args.input_a)
    b_int = f.load(args.input_b)

    a_bin = f.int2bin(a_int)
    b_bin = f.int2bin(b_int)

    # Pad to fixed bit lengths
    a_padded = pad_binary(a_bin, args.pad_a)
    b_padded = pad_binary(b_bin, args.pad_b)

    # Merge and save
    merged_bin = a_padded + b_padded
    merged_int = f.bin2int(merged_bin)
    f.save(merged_int, args.output)

if __name__ == "__main__":
    main()

