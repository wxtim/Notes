import pytest
import random

test = """def test_use_parallel{}():
        assert {} == {}

"""


with open('test_parallel.py', 'w') as fh:
    for i in range(5):
        stuff = test.format(i, i, i)
        fh.write(stuff)


