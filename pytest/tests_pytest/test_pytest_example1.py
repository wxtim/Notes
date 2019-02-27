import pytest

from function import square_plus_10

def test_basic_ok1():
    assert square_plus_10(2) == 14

def test_basic_ok2():
    assert square_plus_10(-2) == 14

def test_blatently_going_to_fail():
    assert square_plus_10(7) == "Bowl of petunias"


