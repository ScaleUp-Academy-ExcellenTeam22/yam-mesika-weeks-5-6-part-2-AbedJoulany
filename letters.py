def get_letters():
    """
       function to return all alphabets letters.
       :return: list of all letters
       """
    lower_case = [chr (i) for i in range (ord ('a'), ord ('z') + 1)]
    upper_case = [chr (i) for i in range (ord ('A'), ord ('Z') + 1)]

    return lower_case + upper_case


if __name__ == '__main__':
    print (get_letters ())
