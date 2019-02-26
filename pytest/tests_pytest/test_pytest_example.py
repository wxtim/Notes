# A pytest

import unittest
import pytest

from function import square_plus_10

TEST_CASES = ([ 2, 14],
              [-2, 14],
              [ 7, "Bowl of petunias"])

# Much nicer
# No class required, no self required, no subTest required
# class TestSquarePlus10_iterative_nicer(unittest.TestCase):
def test_pure_pytest_example():
    for case in TEST_CASES:
        # Hey look, it's just the inbuilt assert
        assert(square_plus_10(case[0]) == case[1])


# Using Pytest parameterize
@pytest.mark.parametrize("test_input, expected", TEST_CASES)
def test_pytest_with_parameterization(test_input, expected):
    assert square_plus_10(test_input) == expected


# Show the working of pytest.approx lest anyone ask me about
# assertAlmostEqual
def test_pytest_almost_equal():
    pytest.approx(10, abs=0.1) == 9.9999
    pytest.approx(1, rel=0.1) == 1.01
