#!/usr/bin/env python3
from src.main import worker
import sys
import subprocess
# runs either from command line e.g. python run.py 10100010
# or without arguments from data/input
# Need a way to run in realtime

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
        '''
        steve.io(mode='in')
        steve.run()
        steve.predict()
        print(steve)
        steve.io(mode='out')
        '''
        while True:
            print(steve)
            steve.action()
            subprocess.call(['clear'])
