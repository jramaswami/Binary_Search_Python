"""
binarysearch.com :: Sum of Four Numbers
jramaswami
"""


from itertools import combinations


class Solution():
    def solve(self, nums, k):
        for combo in combinations(nums, 4):
            if sum(combo) == k:
                return True
        return False


def test_1():
    nums = [10, 3, 5, 9, 4, 0]
    k = 17
    assert Solution().solve(nums, k) == True


def test_2():
    nums = [2]
    k = 8
    assert Solution().solve(nums, k) == False


def test_3():
    nums = [2, 2, 2, 2]
    k = 8
    assert Solution().solve(nums, k) == True