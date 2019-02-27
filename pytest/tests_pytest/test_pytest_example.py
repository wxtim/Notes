import pytest

from function import square_plus_10

TEST_CASES = ([ 2, 14],
              [-2, 14],
              [ 7, "Bowl of petunias"])

@pytest.mark.parametrize("test_input, expected", TEST_CASES)
def test_pytest_with_parameterization(test_input, expected):
    assert square_plus_10(test_input) == expected

