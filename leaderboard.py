"""
binarysearch.com :: Leaderboard
jramaswami
"""


class Solution:

    def solve(self, nums):
        ranking = {x: r for r, x in enumerate(sorted(set(nums), reverse=True))}
        return [ranking[n] for n in nums]


def test_1():
    nums = [50, 30, 50, 90, 10]
    expected = [1, 2, 1, 0, 3]
    assert Solution().solve(nums) == expected