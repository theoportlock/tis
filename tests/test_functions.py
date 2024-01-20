import unittest
import random
from src import functions as f


class TestFunctions(unittest.TestCase):
    def test_powerset(self):
        test_arr = list(random.sample(range(1, 100), 10))
        result = f.powerset(test_arr)
        resultlist = list(result)
        self.assertTrue(type(resultlist[0]) == set)
        self.assertEqual(len(resultlist), (2**len(test_arr)) - 1)

    def test_convert(self):
        test_int = 19
        result = f.convert(test_int)
        self.assertEqual([1, 2, 16], list(result))

    def test_file_preparation(self):
        integer = random.randint(1, 10000000000)
        base = random.randint(2, 10000)
        converted_integer = f.basechanger(integer, base)
        catlevel = random.randint(5, 10)
        concat_converted_int = f.concat(converted_integer, catlevel)
        self.assertEqual(type(converted_integer), list)
        self.assertEqual(type(concat_converted_int), list)
        self.assertNotEqual(len(converted_integer), len(concat_converted_int))


if __name__ == "__main__":
    unittest.main()
