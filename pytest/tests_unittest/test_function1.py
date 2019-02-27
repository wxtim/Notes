# A traditional Unittest

import unittest

from function import square_plus_10

TEST_CASES = ([ 2, 14],
              [-2, 14],
              [ 7, "Bowl of petunias"])


# Very simple unittest
class TestSquarePlus10(unittest.TestCase):
    def test_basic_ok1(self):
        self.assertEqual(square_plus_10(2), 14)

    def test_basic_ok2(self):
        self.assertEqual(square_plus_10(-2), 14)

    def test_which_ought_to_fail(self):
        self.assertEqual(square_plus_10(7), "Bowl of petunias")


if __name__=="__main__":
    unittest.main()

