import timeit


def timer(func, *args, **kwargs):
    """
    This Function measures the time that the passed function
    takes to run on the passed arguments.
    :param func: function to run on passed arguments
    :param args: non keyword argument
    :param kwargs: key word arguments
    :return: time that function takes
    """
    start_timer = timeit.default_timer ()
    f (*args, **kwargs)
    stop_timer = timeit.default_timer ()
    return stop_timer - start_timer


if __name__ == '__main__':
    print (timer (print, "hello"))

    print (timer (zip, [1, 2, 3], [4, 5, 6]))

    print (timer ('Hi {name}'.format, name="Bug"))
