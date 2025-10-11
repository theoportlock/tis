#!/usr/bin/env python3
import argparse
import utils as f

def memorize(inp, mem):
    """Combine input and memory values using bitwise OR on their combinations."""
    return mem | f.comb(inp)

def parse_args():
    parser = argparse.ArgumentParser(description="Update a memory file based on an input file.")
    parser.add_argument("-i", "--input", required=True, help="Path to input file.")
    parser.add_argument("-m", "--memory", required=True, help="Path to existing memory file.")
    parser.add_argument("-o", "--output", required=True, help="Path to updated memory file.")
    return parser.parse_args()

def main():
    args = parse_args()
    mem = memorize(f.load(args.input), f.load(args.memory))
    f.save(mem, args.output)

if __name__ == "__main__":
    main()

