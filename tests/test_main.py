#!/usr/bin/env python3
import unittest
import os
from src.main import worker


class TestMain(unittest.TestCase):
    def cleanup(self):
        for testing_file in self.testing_files.values():
            if os.path.isfile(testing_file):
                os.remove(testing_file)

    def setUp(self):
        self.worker = worker()
        self.testing_files = {
            "inp": "data/test_input",
            "mem": "data/test_memory",
            "pre": "data/test_predict"}
        self.cleanup()

    def tearDown(self):
        self.cleanup()

    def test_file_io(self):
        testtext = "test"
        with open(self.testing_files["inp"], 'w') as of:
            of.write(testtext)
        self.worker.io(files=self.testing_files, mode='in')
        self.cleanup()
        self.worker.io(files=self.testing_files, mode='out')
        with open(self.testing_files["inp"], 'r') as of:
            result = of.read()
        self.assertEqual(testtext, result)

    def test_run(self):
        data = ["abc",
                "ab",
                "b",
                "a"]
        for i in data:
            with open(self.testing_files["inp"], 'w') as of:
                of.write(i)
            self.worker.io(files=self.testing_files)
            self.worker.run().io(files=self.testing_files, mode='out')


if __name__ == '__main__':
    unittest.main()
