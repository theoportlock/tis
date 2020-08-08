import unittest
import os
import IO
from main import comb

class TestMain(unittest.TestCase):
    def cleanup(self):
        self.testing_files = {"inp": "test_input", "mem": "test_memory", "pre": "test_predict"}
        [os.remove(testing_file) for testing_file in self.testing_files if os.path.isfile(testing_file)]
        
    def setUp(self):
        self.cleanup()

    def tearDown(self):
        self.cleanup()

    def test_abcd(self):
        # Tests ability to recognise binary sequences from file
        worker = comb()
        data = ["10001000011", #ABCD
                "10001010001", #ABXD
                "10000000000", #A
                "10001000000", #AB
                "10001010000", #ABX
                "10001000010", #ABC
                "00000010010"] #CX
        for i in data:
            with open(self.testing_files["inp"], 'w') as of: of.write(i)
            result = worker.load({"inp":self.testing_files['inp'],
                    "mem":self.testing_files['mem'],
                    "pre":self.testing_files['pre']}).run()
            print(result.pre_int)
        #self.assertTrue(

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
            self.cleanup()
            # remember abc
            with open("input", 'w') as of: of.write(data[0])
            print(worker.load().run().pre_int)

            # run prediction
            with open("input", 'w') as of: of.write(i)
            print(worker.load().run().pre_int)
            with open("predict", "r") as of: print(i, " predicts ", of.read())

    # @unittest.expectedFailure
    # def test_ultimate_goal(self):
    #    '''
    #    In order to affect sparceness, it is necessary to convert some of the active bits to 0 from the input string.  This, I believe is done incorrectly by traditional HTM architectures where that effect is mandated manually by external preprocessing algorythms. Conversely, the reverse process of input compression is also necessary.
    #    '''
    #    assert 1 == 2

if __name__ == '__main__':
    unittest.main(module="test_main")
