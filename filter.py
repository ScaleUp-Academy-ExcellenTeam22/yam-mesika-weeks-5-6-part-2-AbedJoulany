numbers = [0, 3, 7, 9, 55, 1999, 1998, 2012]
objects = [1, 0, 6, [], -1, 8, None, ""]


def is_odd(number):
    """
    function to check if the passed number is odd or not.
    :param number:
    :return:
    """
    return number % 2 != 0


def identity(x):
    """
    called if the passed function is "None",it yields those items that evaluate to True.
    :param x:
    :return:
    """
    return x


def filterImpl(function, arr):
    """
    function that implements the filter method
    :param function:
    :param arr:
    :return: returns the variables that the passed function returned true for.
    """
    if function is None:
        function = identity
    for obj in arr:
        if function(obj):
            yield obj


if __name__ == '__main__':
    print(list(filterImpl(is_odd, numbers)))
    print(list(filterImpl(None, objects)))