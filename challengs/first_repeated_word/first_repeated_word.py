from hashmap.hashmap import *


def first_repeated_word(text):
    """
    Function to find the first repeated word in a string
    Arguments: String
    Returns: String
    """
    word_evaluater = ""
    hash_map = HashTable()

    for character in text:
        character_lower = character.lower()
        if ord(character_lower) in range(ord("a"), ord("z") + 1):
            word_evaluater += character_lower
        elif len(word_evaluater):
            if hash_map.contains(word_evaluater):
                return word_evaluater
            else:
                hash_map.set(word_evaluater, None)
                word_evaluater = ""

    if len(word_evaluater) and hash_map.contains(word_evaluater):
        return word_evaluater
    return None


if __name__ == '__main__':
    print(first_repeated_word("Once upon a time, there was a brave princess who..."))
    print(first_repeated_word("It was the best of times,"
                              " it was the worst of times,"
                              " it was the age of wisdom,"
                              " it was the age of foolishness,"
                              " it was the epoch of belief,"
                              " it was the epoch of incredulity,"
                              " it was the season of Light,"
                              " it was the season of Darkness, "
                              "it was the spring of hope,"
                              " it was the winter of despair,"
                              " we had everything before us,"
                              " we had nothing before us,"
                              " we were all going direct to Heaven, "
                              "we were all going direct the other way – in short,"
                              " the period was so far like the present period,"
                              " that some of its noisiest authorities insisted on its being received,"
                              " for good or for evil, in the superlative degree of comparison only..."))
    print(first_repeated_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."))
