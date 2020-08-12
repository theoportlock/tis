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

    def test_bin_abcd(self):
        # Tests ability to recognise binary sequences from file
        data = ["10000000001000000000000011",  # ABCD
                "10000000001000000001000001",  # ABXD
                "10000000000000000000000000",  # A
                "10000000001000000000000000",  # AB
                "10000000001000000001000000",  # ABX
                "10000000001000000000000010",  # ABC
                "00000000000000000001000010"]  # CX
        prediction = 0
        for i in data:
            print(self.worker.inp, prediction)
            accuracy = self.worker.inp - prediction
            print("accuracy = ", accuracy)
            with open(self.testing_files["inp"], 'w') as of: of.write(i)
            self.worker.load(files=self.testing_files, from_text=False)
            self.worker.run()
            prediction = self.worker.pre
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

'''
    def test_big_text(self):
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

    def test_ultimate_goal(self):
        # In order to affect sparceness, it is necessary to convert some of the active
        # bits to 0 from the input string.  This, I believe is done incorrectly by
        # traditional HTM architectures where that effect is mandated manually by
        # external preprocessing algorythms. Conversely, the reverse process of input compression is also necessary.
        df = pd.DataFrame(columns=["inp","pre"])
        data = "Hello Jello"
        with open(self.testing_files["inp"], 'w') as of: of.write(data)
        for i in f.concat(f.basechanger(IO.textfile2int(self.testing_files["inp"]), 8), 4):
            self.worker.load(files=self.testing_files, from_text=True)
            self.worker.inp = i
            self.worker.run().save(files=self.testing_files, to_text=True)
            with open("results", 'a') as of: of.write(bin(self.worker.pre)[:2:-1] + "\n")
            df.loc[i] = [bin(self.worker.inp)[:2:-1], bin(self.worker.pre)[:2:-1]]
        # df.to_csv("outdf.csv")
        df.plot()
'''


if __name__ == '__main__':
    unittest.main()

