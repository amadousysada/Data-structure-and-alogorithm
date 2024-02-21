from itertools import permutations

from src.algo.bfs import bfs
from src.algo.dfs import recursive_dfs, iterative_dfs, find_path
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
        "A": ["B", "C", "E"],
        "B": ["D", "F"],
        "C": ["G"],
        "D": ["B"],
        "E": ["F"],
        "F": ["E"],
        "G": ["C"],


    }
    yield vertices


def test_graph(init_edges):
    g = Graph(edges=init_edges)

    assert g.get_vertices() == ["A", "B", "C", "D", "E", "F", "G"]


def test_merge_sort(random_lists):
    for arr in random_lists:
        random_list, expected_sorted_list = arr
        print(f"list to sort: {random_list} ==> expected result: {expected_sorted_list}")
        assert sort(random_list) == expected_sorted_list


def test_recursive_dfs(init_edges):
    g = Graph(edges=init_edges)

    assert recursive_dfs(graph=g, vertex="A") == ["A", "B", "D", "F", "E", "C", "G"]


def test_iterative_dfs(init_edges):
    g = Graph(edges=init_edges)

    assert iterative_dfs(graph=g, vertex="A") ==  ["A", "B", "D", "F", "E", "C", "G"]


def test_recursive_bfs(init_edges):
    g = Graph(edges=init_edges)

    assert bfs(graph=g, vertex="A") == ["A", "B", "C", "E", "D", "F", "G"]


def test_find_path(init_edges):
    g = Graph(edges=init_edges)

    assert find_path(graph=g, vertex="A", target="F") == ["A", "B", "F"]
    assert find_path(graph=g, vertex="A", target="E") == ["A", "B", "F", "E"]
    assert find_path(graph=g, vertex="A", target="E") == ["A", "B", "F", "E"]