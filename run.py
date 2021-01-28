#!/usr/bin/env python3
from src.main import worker
import sys

if __name__ == "__main__":
    steve = worker()
    if len(sys.argv) == 2:
        steve.inp = int(sys.argv[1])
        steve.run().io(mode='out')
    else:
        steve.io(mode='in').run().io(mode='out')
