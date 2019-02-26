# Run Doctest for a module

import doctest
import function
import sys

try:
    _, verbose = sys.argv
except:
    verbose = False
    pass
else:
    if verbose in ['v', '-v' '--verbose']:
        verbose = True

if verbose:
    print(doctest.testmod(function, verbose=True))
else:
    print(doctest.testmod(function))
