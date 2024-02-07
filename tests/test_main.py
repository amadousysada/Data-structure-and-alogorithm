from src.algo.merge_sort import sort

import pytest
import random


def generate_random_list(length):
    return [random.randint(0, 20) for _ in range(length)]


@pytest.fixture
def random_lists():
    list_lengths = [5, 8, 10, 15, 20]
    arrs = []
    for length in list_lengths:
        random_list = generate_random_list(length)
        expected_sorted_list = sorted(random_list)
        arrs.append((random_list, expected_sorted_list))
    yield arrs


def test_merge_sort(random_lists):
    for arr in random_lists:
        random_list, expected_sorted_list = arr
        print(f"list to sort: {random_list} ==> expected result: {expected_sorted_list}")
        assert sort(random_list) == expected_sorted_list
