"""
binarysearch.com :: Update List to Make It Strictly Increasing
jramaswami
"""
"""
binarysearch.com :: Update List to Make It Strictly Increasing
jramaswami
"""
from math import inf
from bisect import bisect_left, bisect_right
from collections import deque


# From Python docs.
def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    return None


class Solution:
    def solve0(self, curr_index, prev_value, ops):
        """Recursive solution."""
        if curr_index >= len(self.A):
            return ops

        if (curr_index, prev_value) in self.memo:
            return self.memo[(curr_index, prev_value)]

        curr_value = self.A[curr_index]
        result = inf
        if curr_value > prev_value:
            result = min(result, self.solve0(curr_index + 1, curr_value, ops))

        curr_value0 = find_gt(self.B, prev_value)
        if curr_value0 is not None and ops + 1 <= len(self.B):
            result = min(result, self.solve0(curr_index + 1, curr_value0, ops + 1))

        self.memo[(curr_index, prev_value)] = result
        return result


    def solve(self, A, B):
        self.A = A
        self.B = sorted(set(B))
        self.memo = dict()
        result = self.solve0(0, -inf, 0)
        if result == inf:
            return -1
        else:
            return result


def test_1():
    a = [9, 1, 3, 6, 4]
    b = [7, 0, 3]
    assert Solution().solve(a, b) == 2

def test_2():
    a = [0, 0]
    b = [0]
    assert Solution().solve(a, b) == -1

def test_3():
    a = [1, 0]
    b = [0, 0]
    assert Solution().solve(a, b) == -1 

def test_4():
    a = [1, 0]
    b = [1, 0]
    assert Solution().solve(a, b) == 2

def test_5():
    a = [2, 1, 0]
    b = [1, 0]
    assert Solution().solve(a, b) == -1

def test_6():
    a = [0, 2, 2]
    b = [0]
    assert Solution().solve(a, b) == -1

def test_7():
    a = [1, 2, 2]
    b = [1, 0]
    assert Solution().solve(a, b) == 2

