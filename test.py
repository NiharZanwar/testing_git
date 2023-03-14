
def add_2_numbers(a, b):
    return (a + b)

def sub_2_numbers(a, b):
    return a - b


def test_add_2_numbers():
    assert add_2_numbers(1, 2) == 3, "Should be 3"

def test_sub_2_numbers():
    """
    this is a test function
    :return:
    """

    assert sub_2_numbers(1, 2) == -1, "Should be -1"


def print_hello():
    print("hello")