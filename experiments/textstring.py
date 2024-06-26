#!/usr/bin/env python3
'''
Should save this test for the last minute
'''
import pandas as pd
from src import IO
from src import functions as f
from src.main import worker

# same as test_abcd but with text
data = ["abc",
        "ab",
        "b",
        "bc",
        "ac",
        "abc",
        "b",
        "a"]
for i in data[1:]:
    with open(self.testing_files["inp"], 'w') as of:
        of.write(data[0])
    with open(self.testing_files["inp"], 'w') as of:
        of.write(i)
    self.worker.load(files=self.testing_files, text=True)
    self.worker.run().save(files=self.testing_files, text=True)
    self.assertTrue(os.path.isfile(self.testing_files["pre"]))
