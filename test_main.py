import unittest
import os
import IO
import main

class TestMain(unittest.TestCase):
    def test_abcd(self):
        # Tests ability to recognise binary sequences
        f = "memory"
        if os.path.isfile(f):
            os.remove(f)
        data = ["10001000011", #ABCD
                "10001010001", #ABXD
                "10000000000", #A
                "10001000000", #AB
                "10001010000", #ABX
                "10001000010", #ABC
                "00000010010"] #CX
        for i in data:
            with open("input", 'w') as of:
                of.write(i)
            main.comb(IO.file2int("input"))

    def test_text(self):
        # same as test_abcd but with text
        f = "memory"
        if os.path.isfile(f):
            os.remove(f)
        data = ["abc",
                "ab",
                "b",
                "bc",
                "ac",
                "abc",
                "b",
                "a"]
        for i in data[1:]:
            # cleanup prediction and memory
            if os.path.isfile("predict"):
                os.remove("predict")
            if os.path.isfile("memory"):
                os.remove("memory")

            # remember abc
            with open("input", 'w') as of:
                of.write(data[0])
            main.comb(IO.text2int("input"))

            # run prediction
            with open("input", 'w') as of:
                of.write(i)
            main.comb(IO.text2int("input"))
            with open("predict", "r") as of:
                print(i, " predicts ", of.read())














0000000100000000100000100001
0000000100000000000000000000 = -3
0000000100000000100000000000 = -2
