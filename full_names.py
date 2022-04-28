

def full_names(first_names, last_names, min=0):
    """
       function to return all composition of first and last names .
       :param: first_names
       :param: last_names
       :param: min
       :return: list
    """
    return [first.capitalize()+' '+last.capitalize()
            for first in first_names for last in last_names if len(first+last) >= min]


if __name__ == '__main__':
    first_names = ['avi', 'moshe', 'yaakov']
    last_names = ['cohen', 'levi', 'mizrahi']
    print(full_names(first_names, last_names, 10))
    print(full_names(first_names, last_names))
