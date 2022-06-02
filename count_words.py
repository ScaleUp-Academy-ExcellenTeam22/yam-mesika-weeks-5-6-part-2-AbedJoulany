import string


def remove_punctuation(text):
    """
       generator to return word after removing punctuation.
       :param: text
       :return: word
    """
    for word in text.split():
        yield word.translate (str.maketrans ('', '', string.punctuation))


def count_words(text):
    """
           function that return a dictionary of the words and their counts.
           :param: text
           :return: dict
    """
    return {word: len (word) for word in remove_punctuation (text)}


if __name__ == '__main__':
    text = """
You see, wire telegraph is a kind of a very, very long cat.
You pull his tail in New York and his head is meowing in Los Angeles.
Do you understand this?
And radio operates exactly the same way: you send signals here, they receive them there.
The only difference is that there is no cat.
"""
    print (count_words (text))
