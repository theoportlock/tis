import unittest
import random
import os
import IO

class TestIO(unittest.TestCase):

    def setUp(self):
        self.testfile = "testfile"
        if os.path.isfile(self.testfile):
            os.remove(self.testfile)

    def tearDown(self):
        if os.path.isfile(self.testfile):
            os.remove(self.testfile)

    def test_setfileio(self):
        testset = set(random.sample(range(1, 1000), 50))
        IO.set2file(testset, self.testfile)
        self.assertTrue(os.path.exists(self.testfile))

        result = IO.file2set(self.testfile)
        self.assertEqual(type(result), set)
        self.assertEqual(result, testset)

    def test_text2int(self):
        random_integer = random.randint(0,1000)
        IO.int2text(random_integer, self.testfile)
        self.assertTrue(os.path.isfile(self.testfile))

        result = IO.text2int(self.testfile)
        self.assertEqual(type(result), int)
        self.assertEqual(result, random_integer)

if __name__ == '__main__':
    unittest.main()
