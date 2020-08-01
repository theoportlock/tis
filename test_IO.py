import unittest
import IO

class TestIO(unittest.TestCase):
    def test_set2file(self):
        testset = set([1,2,3,4,5,6,7,8])
        outfile = "outputfile"
        print(testset)
        print(outfile)
        IO.set2file(testset,outfile)

    def test_file2set(self):
        outfile = "outputfile"
        print("output file is read as ",IO.file2set(outfile))
        assert type(IO.file2set(outfile)) == set
