import pytest
from challengs.first_repeated_word.first_repeated_word import *


def test_empty_string():
    """Test that empty string"""
    actual = first_repeated_word('')
    expected = None
    assert actual == expected


def test_two_words():
    """Test string that has two words"""
    actual = first_repeated_word('yousef yousef')
    expected = 'yousef'
    assert actual == expected


def test_no_repeated_word():
    """Test string that has no repeated word"""
    actual = first_repeated_word('hello there')
    expected = None
    assert actual == expected


def test_hard_string():
    """Test that is hard string"""
    actual = first_repeated_word('book pen book pen')
    expected = 'book'
    assert actual == expected


def test_word_with_symbols():
    """Test string that has a symbols"""
    actual = first_repeated_word('hi? is there! hi')
    expected = 'hi'
    assert actual == expected


def test_capital_cases():
    """Tests string that has a capital_cases"""
    actual = first_repeated_word('hello HellO   HELLO')
    expected = 'hello'
    assert actual == expected


def test_case_from_instructions_1():
    """Test from instructions"""
    actual = first_repeated_word('Once upon a time, there was a brave princess who...')
    expected = 'a'
    assert actual == expected


def test_case_from_instructions_2():
    """Test from instructions"""
    actual = first_repeated_word('It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..')
    expected = 'it'
    assert actual == expected


def test_case_from_instructions_3():
    """Test from instructions"""
    actual = first_repeated_word('It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...')
    expected = 'summer'
    assert actual == expected
