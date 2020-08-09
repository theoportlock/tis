import unittest
import os.path
import IO
import functions as f
from main import comb


class TestMain(unittest.TestCase):
    def cleanup(self):
        self.testing_files = {
            "inp": "temp_input",
            "mem": "temp_memory",
            "pre": "temp_predict"}
        [os.remove(testing_file) for testing_file in self.testing_files if os.path.isfile(testing_file)]

    def setUp(self):
        self.cleanup()

    def tearDown(self):
        self.cleanup()

    def test_abcd(self):
        # Tests ability to recognise binary sequences from file
        worker = comb()
        data = ["10001000011",  # ABCD
                "10001010001",  # ABXD
                "10000000000",  # A
                "10001000000",  # AB
                "10001010000",  # ABX
                "10001000010",  # ABC
                "00000010010"]  # CX
        for i in data:
            with open(self.testing_files["inp"], 'w') as of:
                of.write(i)
            result = worker.load({
                "inp": self.testing_files["inp"],
                "mem": self.testing_files["mem"],
                "pre": self.testing_files["pre"]}).run()

    def test_text(self):
        # same as test_abcd but with text
        worker = comb()
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
            worker.load({
                "inp": self.testing_files["inp"],
                "mem": self.testing_files["mem"],
                "pre": self.testing_files["pre"]})
            worker.run().save({
                "mem": self.testing_files["mem"],
                "pre": self.testing_files["pre"]},
                default=False)
            self.assertTrue(os.path.isfile(self.testing_files["pre"]))

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

    def test_big_text(self):
        worker = comb().load({
            "inp": self.testing_files["inp"],
            "mem": self.testing_files["mem"],
            "pre": self.testing_files["pre"]})
        data = "What is the meaning?"
        with open(self.testing_files["inp"], 'w') as of: of.write(data)
        converted_integer = f.basechanger(IO.textfile2int(self.testing_files["inp"]), 2900)
        for i in f.concat(converted_integer, 2):
            print(i)
            worker.inp_int = i
            worker.run().save({
                "mem": self.testing_files["mem"],
                "pre": self.testing_files["pre"]})


if __name__ == '__main__':
    unittest.main()
