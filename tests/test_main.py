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
            "inp": "data/temp_input",
            "mem": "data/temp_memory",
            "pre": "data/temp_predict"}
        self.cleanup()

    def tearDown(self):
        self.cleanup()

    def test_load_and_save(self):
        text = "test"
        with open(self.testing_files["inp"], 'w') as of:
            of.write(text)
        self.worker.load(files=self.testing_files, text=True)
        self.worker.save(files=self.testing_files, text=True)
        self.assertTrue(os.path.isfile(self.testing_files["pre"]))

    def test_run(self):
        data = ["abc",
                "ab",
                "b",
                "a"]
        for i in data[1:]:
            with open(self.testing_files["inp"], 'w') as of:
                of.write(data[0])
            with open(self.testing_files["inp"], 'w') as of:
                of.write(i)
            self.worker.load(files=self.testing_files, text=True)
            self.worker.run().save(files=self.testing_files, text=True)
            self.assertTrue(os.path.isfile(self.testing_files["pre"]))


if __name__ == '__main__':
    unittest.main()