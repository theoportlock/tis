#!/usr/bin/env python3
import numpy as np
import os.path
import random
import pandas as pd
import utils as f

def memorize(inp, mem):
    mem = mem | f.comb(inp) # Save to memory
    return mem

inp, mem, pre, act = 0, 0, 0, 0
votearray = []

# Add 101 to memory
inp = f.bin2int('101')
f.int2bin(inp)
mem = memorize(inp, mem)
f.int2bin(mem)
f.uncomb(mem)
[f.int2bin(i) for i in f.uncomb(mem)]

# Add 11 to memory
inp = f.bin2int('1100')
f.int2bin(inp)
mem = memorize(inp, mem)
f.int2bin(mem)
f.uncomb(mem)
[f.int2bin(i) for i in f.uncomb(mem)]

'''
for each memory (uncomb mem









def predict(self):
    # invert the input
    Ih = "".join('1' if x == '0' else '0' for x in f.int2bin(inp))

    # extend the inversion to match max bitlength of comb
    mmax = len(f.int2bin(f.uncomb(mem)[-1]))
    Ih += ('1'*(mmax - len(Ih)))
    Ih = f.bin2int(Ih)
    I = inp

    # find difference between the memory and the prediction
    matches = f.paircomb(Ih, I) & mem
    if not matches:
        pre = 0
        return self
    converted = f.uncomb(matches)
    converted_filtered = [f.int2bin(i - (inp & i)) for i in converted]
    converted_int = [[int(j) for j in list(i)] for i in converted_filtered]
    max_length = max((len(i) for i in converted_int))
    for i in converted_int:
        i.extend([0] * (max_length - len(i)))
    votearray = [sum(i) for i in list(zip(*converted_int))]
    norm_votearray = [float(i)/max(votearray) for i in votearray]
    votearray = votearray
    pre = f.bin2int("".join([str(round(i)) for i in norm_votearray]))

def newpredict(self):
    # work on this
    if mem == 0 or inp == 0:
        pre = 0
        return self

    # inversion of input
    Ih = "".join('1' if x == '0' else '0' for x in f.int2bin(inp))

    # extend the inversion to match max bitlength of comb
    #import math / mmax = len(f.int2bin(math.floor(math.log(mem, 2))))
    mmax = len(f.int2bin(f.uncomb(mem)[-1]))
    Ih += ('1'*(mmax - len(Ih)))
    Ih = f.bin2int(Ih)
    I = inp

    # find difference between the memory and the prediction
    matches = f.paircomb(Ih, I) & mem
    if not matches:
        pre = 0
        return self
    converted = f.uncomb(matches)
    converted_filtered = [f.int2bin(i - (inp & i)) for i in converted]
    converted_int = [[int(j) for j in list(i)] for i in converted_filtered]
    max_length = max((len(i) for i in converted_int))
    for i in converted_int:
        i.extend([0] * (max_length - len(i)))
    votearray = [sum(i) for i in list(zip(*converted_int))]
    norm_votearray = [float(i)/max(votearray) for i in votearray]
    votearray = votearray
    pre = f.bin2int("".join([str(round(i)) for i in norm_votearray]))


def action(self):
    act = random.getrandbits(4)
    return self

out = []
maxim = 5
for i in range(20):
    test = 2**maxim  - 1 - i
    Ih = "".join('1' if x == '0' else '0' for x in f.int2bin(i))
    f.bin2int(Ih)
    out.append((i, f.bin2int(Ih), test))

outdf = pd.DataFrame(out)
sns.scatterplot(data=outdf, x=0, y=1)
