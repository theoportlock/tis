import unittest
import string
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


    def test_setfile(self):
        test = set(random.sample(range(1, 1000), 50))
        IO.setfile(obj=test, mode="out", filename=self.testfile)
        self.assertTrue(os.path.exists(self.testfile))
        result = IO.setfile(filename=self.testfile)
        self.assertEqual(type(result), set)
        self.assertEqual(result, test)


    def test_intfile(self):
        test = random.randint(0, 1000)
        IO.intfile(obj=test, mode="out", filename=self.testfile)
        self.assertTrue(os.path.exists(self.testfile))
        result = IO.intfile(filename=self.testfile)
        self.assertEqual(type(result), int)
        self.assertEqual(result, test)


    def test_txtfile(self):
        test = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(0, 100)))
        IO.txtfile(obj=test, mode="out", filename=self.testfile)
        self.assertTrue(os.path.exists(self.testfile))
        result = IO.txtfile(filename=self.testfile)
        self.assertEqual(type(result), str)
        self.assertEqual(result, test)


if __name__ == '__main__':
    unittest.main()
