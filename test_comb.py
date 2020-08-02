import unittest
import IO
import comb

class TestComb(unittest.TestCase):
    def test_comb(self):
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
            comb.a(IO.file2int("input"))
