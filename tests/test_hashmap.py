import pytest
from hashmap.hashmap import *


def test_instance_hash_map_with_size(hash_map):
    actual = hash_map.size
    expected = 1024
    assert actual == expected


def test_Setting_a_key_value(hash_map):
    hash_map.set('key_4', 'yasin')
    actual = hash_map.contains('key_4')
    expected = True
    assert actual == expected


def test_Retrieving_based_on_a_key(hash_map):
    actual = hash_map.get('key_1')
    expected = 'yousef'
    assert actual == expected


def test_returns_null_for_a_key_that_does_not_exist_in_the_hashtable(hash_map):
    key = 'key_10'
    keys_array = hash_map.keys()
    if key in keys_array:
        result = key
    else:
        result = 'None'
    actual = result
    expected = 'None'
    assert actual == expected


def test_returns_a_list_of_all_unique_keys(hash_map):
    actual = hash_map.keys()
    print(actual)
    expected = ['key_1', 'key_2', 'key_3']
    assert actual == expected


def test_handle_a_collision_within_the_hashtable(hash_map):
    hash_map.set('key_2', 'mazen')
    actual = hash_map.get('key_2')
    expected = 'mazen'
    assert actual == expected


def test_retrieving_from_a_bucket_with_collision(hash_map):
    hash_map.set('key_1', 'denies')
    hash_map.set('key_1', 'john')
    actual = hash_map.get('key_1')
    expected = 'john'
    assert actual == expected


def test_hash_a_key(hash_map):
    actual = hash_map._HashTable__hash('abcde')
    expected = 821
    assert actual == expected


#################
# fixture
#################
@pytest.fixture
def hash_map():
    hash_map = HashTable()
    hash_map.set('key_1', 'yousef')
    hash_map.set('key_2', 'ahmad')
    hash_map.set('key_3', 'mohammad')
    return hash_map
