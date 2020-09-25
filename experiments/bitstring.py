#!/usr/bin/env python3
import pandas as pd
from src import IO
from src import functions as f
from src.main import comb

def test_bin_abcd(self):
    # Tests ability to recognise binary sequences from file
    data = ["10000000001000000000000011",  # ABCD
            "10000000001000000001000001",  # ABXD
            "10000000000000000000000000",  # A
            "10000000001000000000000000",  # AB
            "10000000001000000001000000",  # ABX
            "10000000001000000000000010",  # ABC
            "00000000000000000001000010"]  # CX
    prediction = 0
    for i in data:
        self.worker.load(files=self.testing_files, text=False)
        with open(self.testing_files["inp"], 'w+') as of: of.write(i)
        self.worker.run()
        prediction = self.worker.pre
        self.worker.save(files=self.testing_files, text=False)


if __name__ == '__main__':
    exp_big_text()
