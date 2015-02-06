import unittest
import cryptoquip

class Test(unittest.TestCase):
    '''Unit test for cryptoquip.'''

    def test_pattern(self):
        '''test the pattern maker'''
        self.assertEqual(cryptoquip.pattern("HELLO"), "ABCCD")
    
    def test_get_puzzle(self):
        '''test the file reader'''
        puzzle_file = "./test/test_puzzle.txt"
        answer = "WN YBKGK HGYG MQIG PVC EWBQGUK HGYG YGC MG P QBU BN ZBVNIKWBV WV LGPC"
        self.assertEqual(cryptoquip.get_puzzle(puzzle_file), answer)

    def test_propagate(self):
        '''test how the results are passed on'''
        alpha_dict = {"A": set(["B", "C", "D"]), 
                      "B": set(["D"])}
        answer = {"A": set(["B", "C"]),
                  "B": set(["D"])}

        self.assertEqual(cryptoquip.propagate(alpha_dict), answer)


if __name__ == "__main__":
    unittest.main()
