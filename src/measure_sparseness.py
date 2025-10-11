#!/usr/bin/env python3
import argparse
import utils as f

def parse_args():
    parser = argparse.ArgumentParser(description="Measure sparseness (ratio of zeros) in a binary file.")
    parser.add_argument("-i", "--input", required=True, help="Input file path.")
    parser.add_argument("--bits", action="store_true",
                        help="Print raw counts instead of ratios (zeros and ones).")
    return parser.parse_args()

def main():
        args = parse_args()

        value = f.load(args.input)
        bitstring = f.int2bin(value)

        zeros = bitstring.count('0')
        ones = bitstring.count('1')
        total = len(bitstring)

        if total == 0:
            print("Empty bitstring (sparseness undefined)")
            return

        if args.bits:
            print(f"zeros={zeros} ones={ones} total={total}")
        else:
            sparseness = zeros / total
            density = ones / total
            print(f"{sparseness:.5f}")

if __name__ == "__main__":
    main()

