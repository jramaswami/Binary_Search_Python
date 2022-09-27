"""
binarysearch.com :: Latin Square
jramaswami
"""

import itertools


class Solution:

    def solve(self, matrix):
        row_letters = [set(row) for row in matrix]
        all_letters = set(itertools.chain(*row_letters))
        return len(all_letters) == len(matrix) and all(all_letters == r for r in row_letters)


def test_1():
    matrix = [
        ["a", "b", "c"],
        ["c", "a", "b"],
        ["b", "c", "a"]
    ]
    expected = True
    assert Solution().solve(matrix) == expected


def test_2():
    matrix = [
        ["a", "b", "c"],
        ["d", "a", "a"],
        ["b", "b", "a"]
    ]
    expected = False
    assert Solution().solve(matrix) == expected


def test_3():
    "WA, not paying attention!"
    matrix = [
        ["a", "b", "c"],
        ["a", "b", "c"],
        ["a", "b", "c"],
    ]
    expected = False
    assert Solution().solve(matrix) == expected
