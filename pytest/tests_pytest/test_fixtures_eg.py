# Example of testing numpy functionality with a fixture
# Since these are testing numpy f(n)'ality they are pointless
import pytest
import numpy
from  colorama import Fore

@pytest.fixture
def numpy_wx_data():
    print(Fore.RED + '\n [NOTE] Setting Up')
    import numpy
    example = numpy.array([[10, 10, 10],
                           [11, 12, 13],
                           [10, 10, 10]])
    yield example
    print(Fore.BLUE + '\n [NOTE] Tearing Down')
    del example


def test_numpy_rot90(numpy_wx_data):
    print(Fore.GREEN + ' [TEST] rot90')
    result = numpy.rot90(numpy_wx_data)
    expected = numpy.array([[10, 11, 10],
                            [10, 12, 10],
                            [10, 13, 10]])
    assert result.all() == expected.all()

def test_numpy_flip(numpy_wx_data):
    print(Fore.GREEN + ' [TEST] flip')
    result = numpy.flip(numpy_wx_data)
    expected = numpy.array([[10, 10, 10],
                            [13, 12, 11],
                            [10, 10, 10]])
    assert result.all() == expected.all()