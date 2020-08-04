import unittest
import numpy as np
import os
import functions as f

class TestFunctions(unittest.TestCase):
    def test_powerset(self):
        test_arr = [1, 4, 8, 16]
        '''
        should equal [{16}, {8}, {8, 16}, {4}, {16, 4}, {8, 4}, {8, 16, 4},
        {1}, {16, 1}, {8, 1}, {8, 1, 16}, {1, 4}, {16, 1, 4}, {8, 1, 4},
        {8, 1, 4, 16}]
        '''
        result = f.powerset(test_arr)
        self.assertTrue(type(result) == list)
        self.assertTrue(type(result[0]) == set)
        self.assertEqual(len(result), (len(test_arr)**2) - 1)

    def test_convert(self):
        test_int = 19
        result = f.convert(test_int)
        self.assertEqual([1, 2, 16], result)

    def test_basechanger(self):
        base = 2
        result = f.basechanger(15, base)
        print(result)

if __name__ == "__main__":
    unittest.main()
