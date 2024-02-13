from src.algo.dfs import dfs
from src.algo.merge_sort import sort

import pytest
import random

from src.ds.graph import Graph


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


@pytest.fixture
def init_edges():
    vertices = {
        "a": ["b", "c", "d"],
        "b": ["a", "d"],
        "c": ["a"],
        "d": ["a", "b"]
    }
    yield vertices


def test_graph(init_edges):
    g = Graph(edges=init_edges)

    assert g.get_vertices() == ["a", "b", "c", "d"]

    g.add_edge(("e", "f"))

    assert g.get_vertices() == ["a", "b", "c", "d", "e", "f"]


def test_merge_sort(random_lists):
    for arr in random_lists:
        random_list, expected_sorted_list = arr
        print(f"list to sort: {random_list} ==> expected result: {expected_sorted_list}")
        assert sort(random_list) == expected_sorted_list


def test_recursive_dfs(init_edges):
    g = Graph(edges=init_edges)
    g.add_edge(("c", "e"))
    g.add_edge(("e", "f"))

    assert dfs(graph=g, vertex="a") == ["a", "b", "d", "c", "e", "f"]
