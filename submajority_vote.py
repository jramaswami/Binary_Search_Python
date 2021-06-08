"""
binarysearch.com :: Submajority Vote
jramaswami
"""


from collections import Counter


class Solution:
    def solve(self, nums):
        ctr = Counter(nums)
        return sorted(k for k, v in ctr.items() if v > len(nums) // 3)



def test_1():
    nums = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
    expected = [5, 6]
    assert Solution().solve(nums) == expected


def test_2():
    nums = [1, 1, 1, 1, 2, 3]
    expected = [1]
    assert Solution().solve(nums) == expected


def test_3():
    """WA"""
    nums = [4, 0, 4, 0, 0]
    expected = [0, 4]
    assert Solution().solve(nums) == expected
