"""
binarysearch.com :: Longest Consecutive Run of 1s in Binary
jramaswami
"""

class Solution:

    def solve(self, n):
        max_streak = 0
        curr_streak = 0
        for i in range(33):
            mask = 1 << i
            if n & mask:
                curr_streak += 1
                max_streak = max(max_streak, curr_streak)
            else:
                curr_streak = 0
        return max_streak


def test_1():
    assert Solution().solve(156) == 3


def test_2():
    assert Solution().solve(0) == 0


def test_3():
    assert Solution().solve((1 << 33) - 2) == 32

