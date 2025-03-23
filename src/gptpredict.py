#!/usr/bin/env python3
import argparse
import utils as f

def parse_args():
    """
    Parses command-line arguments.

    Returns:
        Namespace: The parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description='predict.py - Predict output based on a memory file.'
    )
    parser.add_argument('-i', '--input', default='../data/input',
                        help='Path to input file', type=str)
    parser.add_argument('-m', '--memory', default='../data/memory',
                        help='Path to memory file', type=str)
    return parser.parse_args()

def predict(input_val, memory_val):
    """
    Predicts an output based on the input and memory.

    Parameters:
        input_val (int): Input integer.
        memory_val (int): Memory integer.

    Returns:
        int: Predicted output.
    """
    if input_val == 0 or memory_val == 0:
        return 0

    # Determine the bit-length to work with (using memory's bit-length)
    bit_length = memory_val.bit_length()
    mask = (1 << bit_length) - 1

    # Invert input, limited to bit_length bits
    inverted = (~input_val) & mask

    # Majority vote across input, inverted, and memory
    result = 0
    for i in range(bit_length):
        bit_mask = 1 << i
        count = ((input_val & bit_mask) > 0) + ((inverted & bit_mask) > 0) + ((memory_val & bit_mask) > 0)
        if count >= 2:
            result |= bit_mask

    return result

if __name__ == '__main__':
    # Parse command-line arguments
    args = parse_args()
    
    # Load input and memory
    input_val = f.load(args.input)
    memory_val = f.load(args.memory)
    
    # Compute prediction
    prediction = predict(input_val, memory_val)
    print(prediction)
    
    # Save the memory (if needed)
    f.save(memory_val, args.memory)
