import pytest
from challengs.stack_queue_brackets.stack_queue_brackets import *


def test_1():
    actual = validate_brackets('{}')
    expected = True
    assert actual == expected


def test_2():
    actual = validate_brackets('{}(){}')
    expected = True
    assert actual == expected


def test_3():
    actual = validate_brackets('()[[Extra Characters]]')
    expected = True
    assert actual == expected


def test_4():
    actual = validate_brackets('(){}[[]]')
    expected = True
    assert actual == expected


def test_5():
    actual = validate_brackets('{}{Code}[Fellows](())')
    expected = True
    assert actual == expected


def test_6():
    actual = validate_brackets('[({}]')
    expected = False
    assert actual == expected


def test_7():
    actual = validate_brackets('(](')
    expected = False
    assert actual == expected


def test_8():
    actual = validate_brackets('{(})')
    expected = False
    assert actual == expected


def test_9():
    actual = validate_brackets('{')
    expected = False
    assert actual == expected


def test_10():
    actual = validate_brackets(')')
    expected = False
    assert actual == expected


def test_11():
    actual = validate_brackets('[}')
    expected = False
    assert actual == expected

