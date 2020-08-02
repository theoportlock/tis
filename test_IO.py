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

    def test_text2arr(self):
        result = IO.text2arr("README.md")
        print("README is = ", result)
        assert type(result) == int
