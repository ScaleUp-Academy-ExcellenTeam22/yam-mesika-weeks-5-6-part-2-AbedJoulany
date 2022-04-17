
def get_positive_numbers (number):
    """
    function to check if the passed number is positive.
    :param number:
    :return:
    """
    return number >= 0


if __name__ == '__main__':
    inputs = list(map(int, input("Enter numbers : ").strip().split(',')))
    print(list(filter(get_positive_numbers, inputs)))

