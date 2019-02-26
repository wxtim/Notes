# A traditional Unittest

import unittest

from function import square_plus_10

TEST_CASES = ([ 2, 14],
              [-2, 14],
              [ 7, "Bowl of petunias"])

# Slightly More Convient
class TestSquarePlus10_iterative_but_unhelpful(unittest.TestCase):
    def test_basic(self):
        for case in TEST_CASES:
            # create a useful error message
            msg = f"square_plus_10({case[0]}) != {case[1]}"
            self.assertEqual(square_plus_10(case[0]), case[1], msg)


if __name__=="__main__":
    unittest.main()

