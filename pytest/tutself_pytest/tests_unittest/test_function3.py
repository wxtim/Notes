# A traditional Unittest

import unittest

from function import square_plus_10

TEST_CASES = ([ 2, 14],
              [-2, 14],
              [ 7, "Bowl of petunias"])


# Much nicer (from 3.5 onwards)
class TestSquarePlus10_iterative_nicer(unittest.TestCase):
    def test_basic(self):
        for case in TEST_CASES:
            with self.subTest(case):
                self.assertEqual(square_plus_10(case[0]), case[1])


if __name__=="__main__":
    unittest.main()

