# A simple mathematical function on which to try different testing frameworks

def square_plus_10(x):
    """
    Doctest Example (Including one designed to fail)
    >>> square_plus_10(2)
    14
    >>> square_plus_10(-2)
    14
    >>> square_plus_10(7)
    A very surprised sperm whale
    """
    return (x * x) + 10


def main():
    print("This main function doesn\'t do anything")


if __name__ == "__main__":
    main()
