#!/usr/bin/env python

import tester.main as t

def a(arr):
    pos = 0
    counter = -1
    conv = [0]*(2**len(arr)-1)
    for e in arr:
        if e:
            counter = counter + 2**pos
        pos += 1
    for f in range(len(conv)):
        conv[f] = 0
    if counter > -1:
        conv[counter] = 1
    return conv

if __name__ == "__main__":
    run = t.run(a)
    run.excecute()
