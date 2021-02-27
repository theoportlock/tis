#!/usr/bin/env python3
'''
This test will be turing like
In order to affect sparceness, it is necessary to convert some of the active
bits to 0 from the input string.  This, I believe is done incorrectly by
traditional HTM architectures where that effect is mandated manually by
external preprocessing algorythms. Conversely, the reverse process of input compression is also necessary.
'''
import unittest
import os
from src import IO
from src import functions as f
from src.main import worker

df = pd.DataFrame(columns=["inp","pre"])
data = "Hello Jello"
with open(self.testing_files["inp"], 'w') as of: of.write(data)
for i in f.concat(f.basechanger(IO.textfile2int(self.testing_files["inp"]), 8), 4):
    self.worker.load(files=self.testing_files, from_text=True)
    self.worker.inp = i
    self.worker.run().save(files=self.testing_files, text=True)
    with open("results", 'a') as of: of.write(bin(self.worker.pre)[:2:-1] + "\n")
    df.loc[i] = [bin(self.worker.inp)[:2:-1], bin(self.worker.pre)[:2:-1]]
    df.to_csv("outdf.csv")
    df.plot()
