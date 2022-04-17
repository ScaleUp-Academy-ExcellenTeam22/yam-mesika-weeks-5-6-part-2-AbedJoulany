import timeit


def timer(f, *args, **kwargs):
    """
    function to measure the time that function takes.
    :param f:
    :param args:
    :param kwargs:
    :return: time
    """
    start = timeit.default_timer ()
    f (*args, **kwargs)
    stop = timeit.default_timer ()
    return stop - start


if __name__ == '__main__':
    print (timer (print, "hello"))

    print (timer (zip, [1, 2, 3], [4, 5, 6]))

    print (timer ('Hi {name}'.format, name="Bug"))
