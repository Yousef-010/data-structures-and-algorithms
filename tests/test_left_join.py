import pytest
from challengs.hashmap_left_join.left_join import *


def test_exists():
    """
    test the expectancy
    """
    assert left_join


def test_from_instructions():
    """
    test from the instruction
    """

    synonyms = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger",
    }

    antonyms = {
        "diligent": "idle",
        "fond": "averse",
        "guide": "follow",
        "flow": "jam",
        "wrath": "delight",
    }

    expected = [
                ['diligent', 'employed', 'idle'],
                ['fond', 'enamored', 'averse'],
                ['guide', 'usher', 'follow'],
                ['outfit', 'garb', None],
                ['wrath', 'anger', 'delight']
                ]

    actual = left_join(synonyms, antonyms)
    assert actual == expected

