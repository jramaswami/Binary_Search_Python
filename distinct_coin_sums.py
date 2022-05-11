"""
binarysearch.com :: Distinct Coin Sums
jramaswami
"""


class Solution:

    def solve(self, coins, quantities):
        prev_dp = set([0])
        for c, q in zip(coins, quantities):
            next_dp = set()
            for k in range(q+1):
                for p in prev_dp:
                    next_dp.add(p + c * k)
            prev_dp = next_dp
        # Remove empty set.
        return len(prev_dp) - 1


def test_1():
    coins = [4, 2, 1]
    quantities = [1, 2, 1]
    expected = 9
    assert Solution().solve(coins, quantities) == expected


def test_2():
    coins = [1]
    quantities = [1]
    expected = 1
    assert Solution().solve(coins, quantities) == expected


def test_3():
    coins = [1]
    quantities = [0]
    expected = 0
    assert Solution().solve(coins, quantities) == expected