#!/usr/bin/env python3
from src.main import worker
import sys

if __name__ == "__main__":
    steve = worker()
    if len(sys.argv) == 2:
        steve.io(mode='in')
        steve.inp = int(sys.argv[1][::-1],2)
        steve.run()
        steve.predict()
        print(steve)
        steve.io(mode='out')
    else:
        steve.io(mode='in')
        steve.run()
        steve.predict()
        print(steve)
        steve.io(mode='out')
