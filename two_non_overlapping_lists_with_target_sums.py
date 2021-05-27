"""
binarysearch.com :: Two Non-Overlapping Lists With Target Sums
jramaswami
"""


from math import inf


class Solution:
    def solve(self, nums, k):
        sums = dict()
        curr_sum = 0
        sums[0] = -1
        best1 = inf
        best2 = inf
        for j, n in enumerate(nums):
            curr_sum += n
            delta = curr_sum - k
            if delta in sums:
                i = sums[delta]
                length = j - i
                if length <= best1:
                    best1, best2 = length, best1
                elif length < best2:
                    best2 = length
            sums[curr_sum] = j

        if best1 == inf or best2 == inf:
            return -1
        return best1 + best2


def test_1():
    nums = [5, 9, -3, -1, 3, 2]
    k = 5
    assert Solution().solve(nums, k) == 3


def test_2():
    nums = []
    k = 5
    assert Solution().solve(nums, k) == -1


def test_3():
    nums = [1,2,3,4,5]
    k = 100
    assert Solution().solve(nums, k) == -1


def test_4():
    nums = [1,2,3,4,5]
    k = 15
    assert Solution().solve(nums, k) == -1


def test_5():
    """WA"""
    nums = [1, 0]
    k = 1
    assert Solution().solve(nums, k) == -1