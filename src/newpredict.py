#!/usr/bin/env python3
import argparse
import utils as f

def parse_args():
    parser = argparse.ArgumentParser(
        description='predict.py - Predict output based on a memory file.'
    )
    parser.add_argument('-i', '--input', default='data/input',
                        help='Path to input file - CS0', type=str)
    parser.add_argument('-m', '--memory', default='data/memory',
                        help='Path to memory file - CS1', type=str)
    parser.add_argument('-o', '--output', default='data/input',
                        help='Path to input file -CS0', type=str)
    return parser.parse_args()

def predict(input_val, memory_val):
    """
    Predicts an output (CS0) based on the input (CS0) and memory (CS1).

    Parameters:
        input_val (int): Input integer.
        memory_val (int): Memory integer.

    Returns:
        int: Predicted output.
    """

    return result

if __name__ == '__main__':
    args = parse_args()
    
    input_val = f.load(args.input)
    memory_val = f.load(args.memory)
    
    prediction = predict(input_val, memory_val)
    print(f.int2bin(prediction))
    
    f.save(prediction, args.output)
