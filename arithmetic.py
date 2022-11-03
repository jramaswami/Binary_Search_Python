"""
binarysearch.com :: Weekly Contest 39 :: Arithmetic Sequence Queries
"""
from bisect import bisect_left, bisect_right

def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return i-1
    raise ValueError

def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect_left(a, x)
    if i != len(a):
        return i
    raise ValueError

class Solution:
    def solve(self, nums, queries):
        deltas = [a - b for a, b in zip(nums[:-1], nums[1:])]
        boundaries = []
        k = None
        for i, v in enumerate(deltas):
            if v != k:
                boundaries.append(i)
                k = v
        boundaries.append(len(nums) - 1)
        soln = 0
        for left, right in queries:
            left0 = find_le(boundaries, left)
            right0 = find_ge(boundaries, right)
            if left0 + 1 == right0 or left0 == right0:
                soln += 1
        return soln


def test_1():
    nums = [1, 3, 5, 7, 6, 5, 4, 1]
    queries = [
        [0, 3],
        [3, 4],
        [2, 4]
    ]
    assert Solution().solve(nums, queries) == 2

def test_2():
    nums = [3]
    queries = [
        [0, 0]
    ]
    assert Solution().solve(nums, queries) == 1
