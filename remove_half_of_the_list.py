"""
binarysearch.com :: Remove Half of the List
jramaswami
"""
from collections import Counter


class Solution:
    def solve(self, nums):
        to_be_removed = len(nums) // 2
        if len(nums) % 2:
            to_be_removed += 1

        ctr = Counter(nums)
        soln = 0
        removed = 0
        for f, k in sorted(((f, k) for k, f in ctr.items()), reverse=True):
            soln += 1
            removed += ctr[k]
            if removed >= to_be_removed:
                break
        return soln


def test_1():
    nums = [7, 9, 9, 7, 3, 4, 5]
    assert Solution().solve(nums) == 2

def test_2():
    nums = [6, 6, 6, 3, 2, 1]
    assert Solution().solve(nums) == 1

def test_3():
    nums = [1, 2, 3, 4, 5, 6]
    assert Solution().solve(nums) == 3

def test_4():
    """WA"""
    nums = [0, 2, 0]
    assert Solution().solve(nums) == 1
