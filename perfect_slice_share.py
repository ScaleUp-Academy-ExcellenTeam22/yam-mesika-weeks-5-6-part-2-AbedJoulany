# function to check if the number is a perfect slice share
def is_perfect(n):
    return sum ([i for i in range (1, n) if not n % i]) == n


# infinite generator
def print_all_numbers():
    a = 0
    while True:  # תמיד מתקיים
        a = a + 1
        yield a


if __name__ == '__main__':
    # get an iterator for the generator
    generator_iterator = print_all_numbers ()
    # iterate over the numbers
    for number in generator_iterator:
        if is_perfect (number):
            print (number)