#!/usr/bin/env python3
import argparse
import random
import utils as f  # assuming your utils module is named utils.py

def create_bitarray(length, sparsity, seed=None):
    """
    Create a random bitarray of given length,
    where `sparsity` is the fraction of zeros (e.g. 0.7 → 70% zeros, 30% ones).
    """
    if seed is not None:
        random.seed(seed)
    # Choose 0 with probability `sparsity`, else 1
    return ''.join(random.choices(['0', '1'], weights=[sparsity, 1 - sparsity], k=length))

def parse_args():
    parser = argparse.ArgumentParser(description="Generate a random bitarray with specified sparsity and save as integer.")
    parser.add_argument("-l", "--length", type=int, default=8, help="Length of the random bitarray.")
    parser.add_argument("-s", "--sparsity", type=float, default=0.5, help="Fraction of zeros (e.g. 0.8 → 80% zeros).")
    parser.add_argument("-o", "--output", required=True, help="Path to output file (saved as integer).")
    parser.add_argument("--seed", type=int, default=None, help="Optional random seed for reproducibility.")
    return parser.parse_args()

def main():
    args = parse_args()
    bitstring = create_bitarray(args.length, args.sparsity, args.seed)
    value = f.bin2int(bitstring)  # convert to int
    f.save(value, args.output)    # save as binary
    print(f"Wrote bitstring: {bitstring} (int={value}) → {args.output}")

if __name__ == "__main__":
    main()

