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
    def solve(self, A, B):
        B = sorted(set(B))
        # Initial value can be unchanged or the least value in B.
        queue = deque([(1, A[0], 0), (1, B[0], 1)])
        soln = inf
        while queue:
            curr_index, prev_value, ops = queue.popleft()
            if curr_index >= len(A):
                soln = min(soln, ops)
            else:
                curr_value = A[curr_index]
                # Invariant curr value > prev value.  
                # Is it possible to make no changes?
                if curr_value > prev_value:
                    queue.append((curr_index + 1, curr_value, ops))

                # Current value can be changed to next value more than the
                # previous value, if there is one left.
                curr_value0 = find_gt(B, prev_value)
                if curr_value0 is not None and ops + 1 <= len(B):
                    queue.append((curr_index + 1, curr_value0, ops + 1))

        if soln == inf:
            return -1
        else:
            return soln


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

