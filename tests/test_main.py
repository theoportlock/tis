import unittest
import os
from src import IO
from src import functions as f
from src.main import comb


class TestMain(unittest.TestCase):
    def cleanup(self):
        for testing_file in self.testing_files.values():
            if os.path.isfile(testing_file):
                os.remove(testing_file) 

    def setUp(self):
        self.worker = comb()
        self.testing_files = {
            "inp": "data/temp_input",
            "mem": "data/temp_memory",
            "pre": "data/temp_predict"}
        self.cleanup()

    def tearDown(self):
        self.cleanup()

    def test_abcd(self):
        # Tests ability to recognise binary sequences from file
        data = ["10001000011",  # ABCD
                "10001010001",  # ABXD
                "10000000000",  # A
                "10001000000",  # AB
                "10001010000",  # ABX
                "10001000010",  # ABC
                "00000010010"]  # CX
        for i in data:
            with open(self.testing_files["inp"], 'w') as of: of.write(i)
            self.worker.load(files=self.testing_files, from_text=False)
            self.worker.run()
            self.worker.save(files=self.testing_files, to_text=False)

    def test_text(self):
        # same as test_abcd but with text
        data = ["abc",
                "ab",
                "b",
                "bc",
                "ac",
                "abc",
                "b",
                "a"]
        for i in data[1:]:
            with open(self.testing_files["inp"], 'w') as of:
                of.write(data[0])
            with open(self.testing_files["inp"], 'w') as of:
                of.write(i)
            self.worker.load(files=self.testing_files, from_text=True)
            self.worker.run().save(files=self.testing_files, to_text=True)
            self.assertTrue(os.path.isfile(self.testing_files["pre"]))

    def test_big_text(self):
        import pandas as pd
        df = pd.DataFrame(columns=["inp","pre"])
        data = "Hello World"
        with open(self.testing_files["inp"], 'w') as of: of.write(data)
        converted_integer = f.basechanger(IO.textfile2int(self.testing_files["inp"]), 50)
        for i in f.concat(converted_integer, 4):
            self.worker.load(files=self.testing_files, from_text=True)
            self.worker.inp = i
            self.worker.run().save(files=self.testing_files, to_text=True)
            with open("results", 'a') as of: of.write(bin(self.worker.pre)[:2:-1] + "\n")
            df.loc[i] = [bin(self.worker.inp)[:2:-1], bin(self.worker.pre)[:2:-1]]
        df.to_csv("outdf.csv")


    """
    @unittest.expectedFailure
    def test_ultimate_goal(self):
    '''
    In order to affect sparceness, it is necessary to convert some of the active
    bits to 0 from the input string.  This, I believe is done incorrectly by
    traditional HTM architectures where that effect is mandated manually by
    external preprocessing algorythms. Conversely, the reverse process of input compression is also necessary.
    '''
    assert 1 == 2
    """


if __name__ == '__main__':
    unittest.main()

