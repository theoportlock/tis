import unittest
import random
import os
from src import IO


class TestIO(unittest.TestCase):
    def cleanup(self):
        self.testfile = "testfile"
        if os.path.isfile(self.testfile):
            os.remove(self.testfile)

    def setUp(self):
        self.cleanup()

    def tearDown(self):
        self.cleanup()

    def test_setfileio(self):
        testset = set(random.sample(range(1, 1000), 50))
        IO.setfile(obj=testset, mode="out", filename=self.testfile)
        self.assertTrue(os.path.exists(self.testfile))
        result = IO.setfile(filename=self.testfile)
        self.assertEqual(type(result), set)
        self.assertEqual(result, testset)

    def test_text2int(self):
        random_integer = random.randint(0, 1000)
        IO.txtfile(obj=random_integer, mode="out", filename=self.testfile)
        self.assertTrue(os.path.isfile(self.testfile))

        result = IO.txtfile(filename=self.testfile)
        self.assertEqual(type(result), int)
        self.assertEqual(result, random_integer)


if __name__ == '__main__':
    unittest.main()
