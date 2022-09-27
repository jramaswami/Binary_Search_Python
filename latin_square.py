"""
binarysearch.com :: Latin Square
jramaswami
"""


import collections


class Solution:

    def solve(self, matrix):
        column_locs = collections.defaultdict(set)
        all_letters = set()
        for row in matrix:
            row_letters = set()
            for c, letter in enumerate(row):
                # Make sure letter is not duplicated in this row.
                if letter in row_letters:
                    return False
                row_letters.add(letter)

                # Make sure we have not exceeded the limit on letters.
                all_letters.add(letter)
                if len(all_letters) > len(matrix):
                    return False

                # Make sure this letter has not appeared in this column before.
                if c in column_locs[letter]:
                    return False
                column_locs[letter].add(c)

        return True


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
