#!/usr/bin/env python3
import pandas as pd
from src import IO
from src import functions as f
from src.main import comb

def exp_big_text():
    df = pd.DataFrame(columns=["inp","pre"])
    data = "Hello World"
    with open(self.testing_files["inp"], 'w') as of: of.write(data)
    converted_integer = f.basechanger(IO.textfile2int(self.testing_files["inp"]), 50)
    for i in f.concat(converted_integer, 4):
        self.worker.load(files=self.testing_files, from_text=True)
        self.worker.inp = i
        self.worker.run().save(files=self.testing_files, text=True)
        with open("results", 'a') as of: of.write(bin(self.worker.pre)[:2:-1] + "\n")
        df.loc[i] = [bin(self.worker.inp)[:2:-1], bin(self.worker.pre)[:2:-1]]
    df.to_csv("outdf.csv")


if __name__ == '__main__':
    exp_big_text()
