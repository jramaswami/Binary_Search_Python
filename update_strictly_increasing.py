"""
binarysearch.com :: Update List to Make It Strictly Increasing
jramaswami
"""
from math import inf
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque


# From Python docs.
def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    return None


def find_lt(a, x):
    'Find rightmost value less than x'
    i = bisect_left(a, x)
    if i:
        return a[i-1]
    return None


def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    return None


class Solution:
    def solve(self, A, B):
        B = sorted(set(B))
        queue = deque([(0, A[0], -inf, 0)])
        soln = inf
        while queue:
            curr_index, curr_value, prev_value, ops = queue.popleft()
            if curr_index + 1 >= len(A):
                soln = min(soln, ops)
            else:
                next_value = A[curr_index + 1]
                if curr_value >= next_value:
                    curr_value0 = find_lt(B, next_value)
                    next_value0 = find_gt(B, curr_value)
                    # (1) We can change curr_value to be less than next_value, if we have enough
                    #     operations left and the new curr_value is greater than the previous max value
                    if ops + 1 <= len(B):
                        if curr_value0 is not None and curr_value0 > prev_value:
                            queue.append((curr_index + 1, next_value, curr_value0, ops + 1))
                    # (2) We can change the next_value to be greater than the curr value, if we
                    #     have enough operations left.
                    if ops + 1 <= len(B):
                        if next_value0 is not None:
                            queue.append((curr_index + 1, next_value0, curr_value, ops + 1))
                    # (3) It is possible we need to swap the values if we have enough operations.
                    if ops + 2 <= len(B):
                        # If the values aren't the same we can swap them.
                        if curr_value != next_value and index(B, curr_value) is not None and index(B, next_value) is not None:
                            if next_value > prev_value:
                                queue.append((curr_index + 1, next_value0, curr_value0, ops + 2))
                else:
                    # We do not need to change anything.
                    queue.append((curr_index + 1, next_value, curr_value, ops))

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

