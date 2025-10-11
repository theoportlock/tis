#!/usr/bin/env python3
import argparse
import utils as f

def read(filename):
    """Print the binary representation of the contents of a file."""
    print(f.int2bin(f.load(filename)))

def parse_args():
    parser = argparse.ArgumentParser(description="Print the binary representation of a file.")
    parser.add_argument(
        "-i", "--input",
        default="work/input",
        help="Path to input file."
    )
    return parser.parse_args()

def main():
    args = parse_args()
    read(args.input)

if __name__ == "__main__":
    main()

