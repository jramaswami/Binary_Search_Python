"""
binarysearch.com :: Minimum Dropping Path Sum
jramaswami
"""
from math import inf


class MinValues:
    """Representation of the two minimum values in a row."""
    def __init__(self):
        self.min1_val = inf
        self.min1_index = -1
        self.min2_val = inf
        self.min2_index = -1

    def add(self, index, value):
        """Add value."""
        if value < self.min1_val:
            self.min2_val, self.min2_index = self.min1_val, self.min1_index
            self.min1_val, self.min1_index = value, index
        elif value < self.min2_val:
            self.min2_val, self.min2_index = value, index

    def get(self, index):
        """Get minimum value, excluding current index."""
        if index == self.min1_index:
            return self.min2_val
        else:
            return self.min1_val


class Solution:
    def solve(self, matrix):
        curr_mins, prev_mins = MinValues(), MinValues()
        for r, row in enumerate(matrix):
            if r == 0:
                for c, val in enumerate(row):
                    prev_mins.add(c, val)
            else:
                for c, val in enumerate(row):
                    curr_mins.add(c, val + prev_mins.get(c))
                curr_mins, prev_mins = MinValues(), curr_mins
        return prev_mins.min1_val


def test_1():
    matrix = [
        [4, 5, -2],
        [2, 6, 1],
        [3, 1, 2]
    ]
    assert Solution().solve(matrix) == 1


def test_2():
    matrix = [
        [3, 0, 3],
        [2, 1, 3],
        [-2, 3, 0]
    ]
    assert Solution().solve(matrix) == 1
