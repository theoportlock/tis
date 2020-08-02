import unittest
import os
import IO

class TestIO(unittest.TestCase):
    def test_setfileio(self):
        f = "testfile"
        if os.path.isfile(f):
            os.remove(f)
        testset = set([1,2,3,4,5,6,7,8])
        IO.set2file(testset,f)
        assert os.path.exists(f) == True
        result = IO.file2set(f)
        assert result == testset
        if os.path.isfile(f):
            os.remove(f)

    def test_text2int(self):
        f1 = "testfile1"
        f2 = "testfile2"
        if os.path.isfile(f1):
            os.remove(f1)
        if os.path.isfile(f2):
            os.remove(f2)

        with open(f1,"w") as of:
            of.write("test")

        result1 = IO.text2int(f1)
        assert type(result1) == int
        print("result1 = ", result1)

        IO.int2text(result1, f2)
        result2 = IO.text2int(f2)
        print("result2 = ", result2)
        assert result1 == result2

        if os.path.isfile(f1):
            os.remove(f1)
        if os.path.isfile(f2):
            os.remove(f2)
