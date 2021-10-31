"""
binarysearch.com :: Making Change
jramaswami
"""


class Solution:

    def solve(self, n):
        COINS = [1, 5, 10, 25]
        coins_used = 0
        curr_sum = 0
        while curr_sum != n:
            while COINS[-1] > n - curr_sum:
                COINS.pop()
            coins_used += 1
            curr_sum += COINS[-1]
        return coins_used


def test_1():
    assert Solution().solve(3) == 3


def test_2():
    assert Solution().solve(5) == 1


def test_3():
    assert Solution().solve(6) == 2


def test_4():
    assert Solution().solve(294624) == 11790


def test_5():
    """TLE"""
    assert Solution().solve(69733939) == 2789362